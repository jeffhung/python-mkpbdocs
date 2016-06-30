# -*- coding: utf-8

# References:
# - http://www.expobrain.net/2015/09/13/create-a-plugin-for-google-protocol-buffer/

from google.protobuf.compiler import plugin_pb2 as plugin
from google.protobuf import descriptor_pb2 as descriptor

import sys
import logging
import pprint
import json
import itertools
import re
import optparse

logging.basicConfig(
        level=logging.DEBUG)
#       format='%(asctime)s %(message)s', datefmt='%Y-%m-%dT%H:%M:%SZ',

# ----------------------------------------------------------------------------

class Traversaller1:

    def traverse(self, proto_file):
        types = []
        for item, package, path in itertools.chain(
                self._traverse(proto_file.package, proto_file.message_type, [4]),
                self._traverse(proto_file.package, proto_file.enum_type, [5])):
#           logging.debug(item)
#           logging.debug(package)
            data = {
                'package': package,
                'filename': proto_file.name,
                'name': item.name,
                'path': path,
            }
            if isinstance(item, descriptor.DescriptorProto):
                data.update({
                    'type': 'Message',
                    'fields': [ self._field(f) for f in item.field ],
                })
            if isinstance(item, descriptor.EnumDescriptorProto):
                data.update({
                    'type': 'Enum',
                    'values': [ { 'name': v.name, 'value': v.number }
                                for v in item.value ],
                })
            types.append(data)
        return types

    # yeilds (item, package, path)
    def _traverse(self, package, items, path):
        for (i, item) in enumerate(items):
#           logging.debug(item)
            yield item, package, path + [ i ]
            if isinstance(item, descriptor.DescriptorProto):
                for (j, enum) in enumerate(item.enum_type):
#                   logging.debug(enum)
                    nested_package = package + '.' + item.name
                    nested_path = path + []
                    yield enum, nested_package, path
                if item.nested_type:
                    for nested_item, nested_package, nested_path in self._traverse(package, item.nested_type, path):
#                       logging.debug(nested_item)
#                       logging.debug(nested_package)
                        yield nested_item, nested_package, nested_path

    def _field(self, field):
        Label = descriptor.FieldDescriptorProto.Label
        label_name = Label.keys()[Label.values().index(field.label)][6:].lower()

        Type = descriptor.FieldDescriptorProto.Type
        type_name = Type.keys()[Type.values().index(field.type)][5:].lower()

#       logging.debug(type_name)
        if type_name == 'message' or type_name == 'enum':
            type_name = field.type_name[1:]
        return {
            'label': label_name,
            'type': type_name,
            'name': field.name,
            'number': field.number,
        }

# ----------------------------------------------------------------------------

#def dict_set(d, k, v=None):
#    if v:
#        d[k] = v
#    elif d.has_key(k):
#        del d[k]

class Traversaller2:
    def traverse(self, proto_file):
#       self._dump_locations(proto_file)
        self.sci = proto_file.source_code_info
        data = {
            'filename': proto_file.name,
            'package': proto_file.package if proto_file.package else 'root',
            'items': [],
        }
        for (i, x) in enumerate(proto_file.message_type):
            for message in self._traverse(x, [ 4, i ]):
                data['items'].append(message)
        for (i, x) in enumerate(proto_file.enum_type):
            for enum in self._traverse(x, [ 5, i ]):
                data['items'].append(enum)
        return data

    def _traverse(self, item, path, parent=''):
#       logging.debug('path: %s', path)
        data = {
            'name': re.sub(r'^\.', '', '.'.join([ parent, item.name ])),
#           'path': path,
            'doc': self._comments(path)
        }

        if isinstance(item, descriptor.DescriptorProto):
            data.update({ 'type': 'message' })
            for (i, x) in enumerate(item.field):
                Type = descriptor.FieldDescriptorProto.Type
                Label = descriptor.FieldDescriptorProto.Label
                field = {}
                field['name'] = x.name
                field['type'] = Type.keys()[Type.values().index(x.type)][5:].lower()
                if field['type'] == 'message' or field['type'] == 'enum':
                    field['type'] = x.type_name[1:]
                field['label'] = Label.keys()[Label.values().index(x.label)][6:].lower()
                field['number'] = x.number
                if x.default_value:
                    field['default'] = x.default_value
                field_path = path + [ 2, i ]
                field['doc'] = self._comments(field_path)
                if not data.has_key('fields'):
                    data['fields'] = []
                data['fields'].append(field)

            for (i, x) in enumerate(item.nested_type):
                nested_path = path + [ 3, i ]
                for nested in self._traverse(x, nested_path, data['name']):
                    yield nested

            for (i, x) in enumerate(item.enum_type):
                enum_path = path + [ 4, i ]
                for enum in self._traverse(x, enum_path, data['name']):
                    yield enum

        if isinstance(item, descriptor.EnumDescriptorProto):
            data.update({ 'type': 'enum', 'values': [] })
            for (i, x) in enumerate(item.value):
                value = {
                    'name': x.name,
                    'number': x.number,
                    'doc': self._comments(path + [ 2, i ]),
                }
                data['values'].append(value)

        yield data

    def _dump_locations(self, proto_file):
        for loc in proto_file.source_code_info.location:
            path = []
            for p in loc.path:
                path.append(p)
            logging.debug('%s %s %s', path,
                    loc.leading_comments, loc.trailing_comments)

    def _comments(self, path):
        for i, x in enumerate(self.sci.location):
            if x.path == path:
                return "\n".join([
                    re.sub(r'^[\*/]', '', x.leading_comments),
                    re.sub(r'^[\*/]', '', x.trailing_comments)
                ]).strip()
        return None

# ----------------------------------------------------------------------------

def pb_dump(msg):
    for field in msg.ListFields():
        # label_name
        l = descriptor.FieldDescriptorProto.Label
        label_name = l.keys()[l.values().index(field[0].label)][6:].lower()

        # type_name
        t = descriptor.FieldDescriptorProto.Type
        type_name = t.keys()[t.values().index(field[0].type)][5:].lower()

        logging.debug('{ %s %s %s = %d }: %s',
                label_name, type_name, field[0].name, field[0].number, field[1])

def generate_code(request, response):
#   logging.debug('parameter: %s', pprint.pformat(request.parameter))

    for proto_file in request.proto_file:
        output_file = response.file.add()
        output_file.name = proto_file.name[:-6] + '.json'

        traversaller = Traversaller2()
        data = traversaller.traverse(proto_file)
#       logging.debug(data)
        output_file.content = json.dumps(data)
#       pb_dump(output_file)

def main():
#   logging.debug(sys.argv)
#   parser = optparse.OptionParser()
#   parser.add_option('--out', dest='outdir')
#   parser.add_option('--parameter', dest='parameter')
#   options = parser.parse_args()
#   outdir = ''
#   parameter = ''
#   logging.debug('options: %s', options)
#   logging.debug('outdir: %s', outdir)
#   logging.debug('param: %s', parameter)

    # Read request message from stdin
    input = sys.stdin.read()

    # Parse request
    request = plugin.CodeGeneratorRequest()
    request.ParseFromString(input)

    # Create response
    response = plugin.CodeGeneratorResponse()

    # Generate code
    generate_code(request, response)

    # Serialise response message
    output = response.SerializeToString()

    # Write to stdout
    sys.stdout.write(output)


