import datetime
from abc import ABC, abstractmethod

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
    def __init__(self, label: str, type_: str) -> None:
        self.label = label
        self.type = type_

    def get_type(self) -> str:
        """
        Returns the type of the field.

        Returns
        -------
        str
            The type of the field.
        """
        return self.type

    @abstractmethod
    def render(self) -> None:
        """Renders the field on the page."""
        pass


class TextField(Field):
    def __init__(self, label: str, value: str) -> None:
        super().__init__(label, 'text')
        self.value: str = value

    def render(self) -> None:
        """Renders the text field on the page."""
        self.value = st.text_input(label=self.label, value=self.value)


class DateField(Field):
    def __init__(self, label: str, value: datetime.datetime) -> None:
        super().__init__(label, 'date')
        self.value = value

    def render(self) -> None:
        """Renders the date field on the page."""
        self.value = st.date_input(
            label=self.label,
            value=self.value,
            format='DD/MM/YYYY'
        )


class SelectBoxField(Field):
    def __init__(self, label, options: list[str], value: str = None) -> None:
        super().__init__(label, 'selectbox')
        self.options = options
        self.value = value

    def render(self) -> None:
        """Renders the select box field on the page."""
        self.value = st.selectbox(
            label=self.label,
            options=self.options,
            index=None if self.value is None else self.options.index(self.value)
        )


class NumberField(Field):
    def __init__(self, label: str, value: float) -> None:
        super().__init__(label, 'number')
        self.value = value

    def render(self) -> None:
        """Renders the number field on the page."""
        self.value = st.number_input(
            label=self.label,
            value=self.value,
            step=0.01
        )
