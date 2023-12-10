run:
	python3 -m streamlit run src/interface/login.py
test:
	python3 -m unittest discover -s tests -p "*.py"
