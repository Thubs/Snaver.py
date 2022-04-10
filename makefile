PREFIX ?= /usr/local
DOCDIR ?= $(PREFIX)/share/snaver/doc

all:
	@echo Run \'make install\' to install snaver.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p snaver.py $(DESTDIR)$(PREFIX)/bin/snaver
	@mkdir -p $(DESTDIR)$(DOCDIR)
	@cp -p README.md $(DESTDIR)$(DOCDIR)
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/snaver

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/snaver
	@rm -rf $(DESTDIR)$(DOCDIR)
	@rm -rf $(DESTDIR)$(PREFIX)/share/snaver