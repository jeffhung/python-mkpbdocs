# MkPbDocs

Protobuf documentation with MkDocs.

# Overview

MkPbDocs is a Protobuf documentation generator which convert the `.proto`
schema files to `.md` markdown files, for generating static documentation site
by [MkDocs](http://www.mkdocs.org/) later.

# Development

## Bootstrap

You need GNU make, Python, Curl, and Protobuf to bootstrap development.
Run the following command to install them:

```console
(debian)$ apt-get install protobuf python make curl
(centos)$     yum install protobuf python make curl
(macosx)$    brew install protobuf
```

Once you have them in your environment, you could initiate developing by:

```console
$ make init
```

MkPbDocs will automatically bootstrap a python runtime environment in the
`runtime` folder with [python.make](https://github.com/jeffhung/python.make).

## Testing

Please run the following command to run MkPbDocs test cases written with
[pytest](http://pytest.org):

```console
$ make test
```

## Example

The building of the MkPbDocs website also demonstrates how MkPbDocs works.  The
site will be built from `example/*.proto` and `docs/*.md` files. Please run the
following command to build and serve the site:

```console
$ make site
```

# Use

## Prerequisites

## Install

MkPbDocs supports Python 2.7+.

Install the `mkpbdocs` package using pip:

```
pip install mkpbdocs
```

You should now have the `mkpbdocs` command installed on your system. Run
`mkpbdocs --version` to check that everything worked okay.

```console
$ mkpbdocs --version
mkpbdocs, version 0.1
```

## Run

Take the bundled `example` folder for example:

```console
$ tree example
example
├── addressbook.proto
└── person.proto

0 directories, 2 files
```

Getting started is easy, just like MkDocs:

```console
$ mkpbdocs new example
$ cd example
```


