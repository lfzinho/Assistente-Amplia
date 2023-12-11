# Exemplo de uso: make test FOLDER=test_interface
run:
	python3 -m streamlit run src/interface/login.py
test:
	python3 -m unittest discover -s tests/$(FOLDER) -p "*.py"
