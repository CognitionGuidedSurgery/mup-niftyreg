#
#
#
#

CMAKE_OPTIONS=-DCMAKE_SKIP_RPATH:BOOL=TRUE -DCMAKE_INSTALL_PREFIX:PATH="$(CURDIR)/install"

configure:
	mkdir -p build
	cd build && cmake $(CMAKE_OPTIONS) ../niftyreg

compile: configure
	cd build && make

install: configure
	mkdir -p install
	cd build && make install
