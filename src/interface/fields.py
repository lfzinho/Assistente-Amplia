from abc import ABC, abstractmethod
import datetime
import streamlit as st


# class Field(ABC):
#     def __init__(self, label, type):
#         self.label: str = label
#         self.type: str = type

#     @abstractmethod
#     def render(self):
#         """Renders the field on the page."""
#         pass

class Field(ABC):
    def __init__(self, label, type):
        self.label: str = label
        self.type: str = type
    
    def get_type(self):
        """Returns the type of the field."""
        return self.type

    @abstractmethod
    def render(self):
        """Renders the field on the page."""
        pass


class TextField(Field):
    def __init__(self, label, value):
        super().__init__(label, 'text')
        self.value: str = value
    
    def render(self):
        """Renders the text field on the page."""
        self.value = st.text_input(label=self.label, value=self.value)


class DateField(Field):
    def __init__(self, label, value):
        super().__init__(label, 'date')
        self.value: datetime.date = value
    
    def render(self):
        """Renders the date field on the page."""
        self.value = st.date_input(label=self.label, value=self.value)
