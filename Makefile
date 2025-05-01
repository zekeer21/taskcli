# Makefile for taskcli project

.PHONY: install-dev uninstall reinstall clean help

# Install in editable mode (local source is used)
install-dev:
	pip install -e .

# Uninstall taskcli
uninstall:
	pip uninstall -y taskcli

# Reinstall taskcli from local source
reinstall: uninstall install-dev

# Clean build artifacts
clean:
	rm -rf build dist *.egg-info taskcli.egg-info __pycache__

# Help: shows all available commands
help:
	@echo "Available make commands:"
	@echo "  make install-dev   - Install taskcli in editable (dev) mode"
	@echo "  make uninstall     - Uninstall taskcli"
	@echo "  make reinstall     - Uninstall and reinstall taskcli"
	@echo "  make clean         - Remove build and egg-info folders"
