#
#
#
#

CMAKE_OPTIONS=-DCMAKE_SKIP_RPATH:BOOL=TRUE -DCMAKE_INSTALL_PREFIX:PATH="$(CURDIR)/install"
INSTALL_DIR=./install
BINARIES=$(INSTALL_DIR)/bin
BUILD_DIR=./build

configure:
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) && cmake $(CMAKE_OPTIONS) ../niftyreg

compile: configure
	cd $(BUILD_DIR) && make

install: configure
	mkdir -p $(INSTALL_DIR)
	cd $(BUILD_DIR) && make $(INSTALL_DIR)

gen:
	python cli2msml/c2m -o $(CURDIR)/alphabet  $(BINARIES)/*

html:
	cd alphabet && (for i in *.rst; do rst2html $i $i.html;  done)


.PHONY: testmsml
testmsml:
	PYTHONPATH=/home/weigl/workspace/msml/src/ \
	    /home/weigl/.virtualenvs/msml/bin/python \
    	    /home/weigl/workspace/msml/src/msml.py -vvv exec --package . -e base -- share/niftyreg-test.msml.xml
