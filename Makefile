init:
	pip3 install -r requirements.txt

test:
	python3 -m unittest -v $(wildcard src/test/*Test.py)

run:
	src/main/main.py

INSTALL_DIR = /usr/local/bin/servo-server.d/
install:
	mkdir $(INSTALL_DIR)
	find src -type f | grep -v __pycache__ | sed 's|src/||' | xargs -I {} install -D src/{} $(INSTALL_DIR){}
	ln -s $(INSTALL_DIR)/main.py /usr/local/bin/servo-server
