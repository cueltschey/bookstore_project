PY=python3

PFLAGS=-Wall

all: run

run:
	$(PY) User.py $(PFLAGS) 
	$(PY) Cart.py $(PFLAGS)
	$(PY) Inventory.py $(PFLAGS)
	$(PY) main.py $(PFLAGS)
