# MkPbDocs

Protobuf documentation with MkDocs.

# Overview

MkPbDocs is a Protobuf documentation generator which convert the `.proto`
schema files to `.md` markdown files, for generating static documentation site
by [MkDocs](http://www.mkdocs.org/) later.

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


