
.PHONY: all
all: help

.PHONY: help
help:

.PHONY: clean
clean:
	rm -rf tmp
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm  -f README.rst
	rm  -f docs/*.json
	rm -rf tests/__pycache__

.PHONY: init
init: python.make
	$(MAKE) -f python.make python-runtime
	$(MAKE) -f python.make python-protobuf
	$(MAKE) -f python.make python-pytest
	$(MAKE) -f python.make python-watchdog
#	$(MAKE) -f python.make python-pandoc
	$(MAKE) -f python.make python-mkdocs
	. runtime/bin/activate; \
	python setup.py develop --prefix runtime

python.make:
	curl -L -o python.make https://bit.ly/python-make

.PHONY: test
test:
	. runtime/bin/activate; \
	py.test --basetemp=tmp  --ignore runtime

# Need:
# - (python) pip install watchdog
.PHONY: watch
watch:
	. runtime/bin/activate; \
	watchmedo shell-command \
		--command='make test' \
		--ignore-directories \
		--patterns './GNUmakefile;./bin/protoc-gen-pbdocs;*.py' \
		--ignore-patterns './tmp/*' \
		--recursive .

## Need:
## - (debian) apt-get install inotify-tools
## - (centos)     yum install inotify-tools
## - (macosx)    brew install fswatch
## TODO: Enable notification on vagrant guest while editing on vagrant host.
## TODO: Use fswatch to monitor source change on Mac.
## References:
## - http://www.systutorials.com/5484/running-a-command-upon-files-or-directories-changes-on-linux/
## - http://blogs.operationaldynamics.com/andrew/software/haskell/rebuilding-via-inotify
## - https://raw.githubusercontent.com/afcowie/buildtools/master/inotifymake.sh
## - https://github.com/rvoicilas/inotify-tools/wiki
#.PHONY: watch0
#watch0: $(wildcard bin/* tests/*.py)
#	@while true; do \
#		inotifywait -q -q -e close_write \
#		            --exclude '^\..*\.sw[px]*$|4913|~$|.git/.*\.lock$|.*i\.log$|tmp/*' \
#		            -r ./; \
#		sleep 1; clear; \
#		$(MAKE) test; \
#	done;

.PHONY: sdist
sdist: README.rst
	python setup.py sdist

.PHONY: bdist
bdist: README.rst
	python setup.py bdist

.PHONY: bdist_egg
bdist_egg: README.rst
	python setup.py bdist_egg

# See: https://bfroehle.com/2013/04/26/converting-md-to-rst/
README.rst:
	pandoc --from=markdown --to=rst --output=README.rst README.md

.PHONY: pbdocs
pbdocs:
	. runtime/bin/activate; \
	protoc --pbdocs_out=docs --proto_path=example \
		example/addressbook.proto example/person.proto;
	cat docs/addressbook.json | jq .

#.PHONY: vagrant-pbdocs
#vagrant-pbdocs:
#	clear;
#	vagrant ssh --command "make -C /vagrant pbdocs";

