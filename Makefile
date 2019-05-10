init:
	pip3 install -r requirements.txt

test:
	python3 -m unittest $(wildcard tests/*Test.py)
