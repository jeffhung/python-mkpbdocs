# -*- coding: utf-8

"""
Generate mkdocs markdown files from protobuf .proto schema.

foo.proto       pb2json.py       foo.json    json2md.py     foo.md
bar.proto ---------------------> bar.json ----------------> bar.md
xyz.proto  (protoc-gen-pbdocs)   xyz.json                   xyz.md

The mkpbdocs command line utility drives the above process.
"""

__version__     = '0.1.0'
__author__      = 'Jeff Hung'
__email__       = 'jeff.cc.hung@gmail.com'
__license__     = 'BSD'
__copyright__   = 'Copyright (c) 2016, Jeff Hung'

if __name__ == '__main__':
    pass

