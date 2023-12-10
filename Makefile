run:
	python3 -m streamlit run src/interface/index.py
test:
	python3 -m unittest discover -s tests -p "*.py"
