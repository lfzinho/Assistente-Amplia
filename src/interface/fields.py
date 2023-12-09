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
        self.value: datetime.datetime = value

    def render(self):
        """Renders the date field on the page."""
        self.value = st.date_input(
            label=self.label,
            value=self.value,
            format='DD/MM/YYYY'
        )


class SelectBoxField(Field):
    def __init__(self, label, value, options):
        super().__init__(label, 'selectbox')
        self.value: str = value
        self.options: list = options

    def render(self):
        """Renders the select box field on the page."""
        self.value = st.selectbox(
            label=self.label,
            options=self.options,
            index=self.options.index(self.value)
        )


class NumberField(Field):
    def __init__(self, label, value):
        super().__init__(label, 'number')
        self.value: float = value

    def render(self):
        """Renders the number field on the page."""
        self.value = st.number_input(
            label=self.label,
            value=self.value,
            step=0.01
        )
