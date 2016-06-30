# Notes

# protoc-gen-pbdocs

Like Javadoc and Doxygen, `protoc-gen-pbdocs` is a Protobuf compiler plugin
that reads the `.proto` files in and generate corresponding documents in JSON
format.

## Usage

```console
$ protoc --pbdocs_out=<outdir> input1.proto input2.proto ...
```

## Post-Processing

The output JSON file could be further processed in the following ways:

* feed into [jinja2-cli](https://pypi.python.org/pypi/jinja2-cli)/[j2cli](https://github.com/kolypto/j2cli)/[jin2cli](https://pypi.python.org/pypi/jin2cli/0.2) to transform into another format like markdown, html

## Reference

* [How to write my own code generator of protobuf](http://stackoverflow.com/questions/28958135/how-to-write-my-own-code-generator-of-protobuf)
  on stackoverflow
* [protoc-gen-doc](https://github.com/estan/protoc-gen-doc)
* [Create a plugin for Google Protocol Buffer](http://www.expobrain.net/2015/09/13/create-a-plugin-for-google-protocol-buffer/)
* [Compiler Plugins](https://developers.google.com/protocol-buffers/docs/reference/other):
	"A plugin is just a program which reads a `CodeGeneratorRequest` protocol
	buffer from standard input and then writes a `CodeGeneratorResponse` protocol
	buffer to standard output."
* [plugin.h](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.compiler.plugin)
  &
	[code_generator.h](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.compiler.code_generator)
* [protoc-gen-json](https://github.com/sourcegraph/prototools/tree/master/cmd/protoc-gen-json) in go,
	see its [document](https://github.com/sourcegraph/prototools/blob/master/README.json.md)
* [protoc-gen-json](https://github.com/mickem/json-protobuf/blob/master/protoc-gen-json) in python
* [protoc-gen-json](https://github.com/square/protob/blob/master/bin/protoc-gen-json) in nodejs
* [Other Utilities](https://github.com/google/protobuf/blob/master/docs/third_party.md#other-utilities)
	in [Third-Party Add-ons for Protocol Buffers](https://github.com/google/protobuf/blob/master/docs/third_party.md)
* [SourceCodeInfo](https://github.com/google/protobuf/blob/master/src/google/protobuf/descriptor.proto#L648)
	in [`src/google/protobuf/descriptor.proto`](https://github.com/google/protobuf/blob/master/src/google/protobuf/descriptor.proto)
	in protobuf source code.

