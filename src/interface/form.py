import streamlit as st

class Form:
    def __init__(self, title, description, fields):
        self.title: str = title
        self.description: str = description
        self.fields: str = fields
    
    def render(self):
        """Renders the form on the page."""
        st.title(self.title)
        st.markdown(self.description)
        with st.form(key='form'):
            for field in self.fields:
                field.render()
            st.form_submit_button(label='Submit')
