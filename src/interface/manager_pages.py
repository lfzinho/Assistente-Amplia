import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from abc import ABC, abstractmethod
import pandas as pd
import streamlit as st
from src.interface.form import Form
from src.interface.fields import TextField, DateField
from src.interface.form_classes import CreationForm, UpdateForm, DeletionForm
from src.interface.beneficiary_form_classes import *
from src.interface.person_form_classes import *
from src.interface.student_form_classes import *
from src.interface.teacher_form_classes import *
from src.interface.analyst_form_classes import *
from src.interface.director_form_classes import *
from src.interface.administrator_form_classes import *


class ManagerPage(ABC):
    def __init__(
        self, title, description, creation_form, update_form, deletion_form
    ):
        self.title: str = title
        self.description: str = description
        self.creation_form: CreationForm = creation_form
        self.update_form: UpdateForm = update_form
        self.deletion_form: DeletionForm = deletion_form

    @abstractmethod
    def show_table(self):
        """Shows the table of the managed elements on the page."""
        pass

    def show_creation_form(self):
        """Shows the creation form on the page."""
        self.creation_form.render()

    def show_update_form(self):
        """Shows the update form on the page."""
        self.update_form.render()

    def show_deletion_form(self):
        """Shows the deletion form on the page."""
        self.deletion_form.render()

    def show_form_tabs(self):
        """Shows all forms in a tab organization."""
        creation_tab, update_tab, deletion_tab = st.tabs(
            ['Criação', 'Atualização', 'Deleção']
        )
        with creation_tab:
            self.show_creation_form()
        with update_tab:
            self.show_update_form()
        with deletion_tab:
            self.show_deletion_form()
    
    def render(self):
        """Renders the page in the usual organization."""
        st.title(self.title)
        st.write(self.description)
        self.show_table()
        self.show_form_tabs()


class PersonPage(ManagerPage):
    def __init__(self):
        super().__init__(
            title="Página de Beneficiário",
            description="Gerencie os beneficiários do sistema.",
            creation_form=PersonCreationForm(),
            update_form=PersonUpdateForm(),
            deletion_form=PersonDeletionForm()
        )

    def show_table(self):
        """Shows the table of the managed elements on the page."""
        pass  # TODO mostra a tabela de beneficiários


class BeneficiaryPage(ManagerPage):
    def __init__(self):
        super().__init__(
            title="Página de Beneficiário",
            description="Gerencie os beneficiários do sistema.",
            creation_form=BeneficiaryCreationForm(),
            update_form=BeneficiaryUpdateForm(),
            deletion_form=BeneficiaryDeletionForm()
        )

    def show_table(self):
        """Shows the table of the managed elements on the page."""
        pass  # TODO mostra a tabela de beneficiários


class StudentPage(ManagerPage):
    def __init__(self):
        super().__init__(
            title="Página de Estudante",
            description="Gerencie os estudantes do sistema.",
            creation_form=StudentCreationForm(),
            update_form=StudentUpdateForm(),
            deletion_form=StudentDeletionForm()
        )

    def show_table(self):
        """Shows the table of the managed elements on the page."""
        pass


class TeacherPage(ManagerPage):
    def __init__(self):
        super().__init__(
            title="Página de Professor",
            description="Gerencie os professores do sistema.",
            creation_form=TeacherCreationForm(),
            update_form=TeacherUpdateForm(),
            deletion_form=TeacherDeletionForm()
        )

    def show_table(self):
        """Shows the table of the managed elements on the page."""
        pass


class AnalystPage(ManagerPage):
    def __init__(self):
        super().__init__(
            title="Página de Analista",
            description="Gerencie os analistas do sistema.",
            creation_form=AnalystCreationForm(),
            update_form=AnalystUpdateForm(),
            deletion_form=AnalystDeletionForm()
        )

    def show_table(self):
        """Shows the table of the managed elements on the page."""
        pass


class DirectorPage(ManagerPage):
    def __init__(self):
        super().__init__(
            title="Página de Diretor",
            description="Gerencie os diretores do sistema.",
            creation_form=DirectorCreationForm(),
            update_form=DirectorUpdateForm(),
            deletion_form=DirectorDeletionForm()
        )

    def show_table(self):
        """Shows the table of the managed elements on the page."""
        pass


class AdministratorPage(ManagerPage):
    def __init__(self):
        super().__init__(
            title="Página de Administrador",
            description="Gerencie os administradores do sistema.",
            creation_form=AdmnistratorCreationForm(),
            update_form=AdmnistratorUpdateForm(),
            deletion_form=AdmnistratorDeletionForm()
        )

    def show_table(self):
        """Shows the table of the managed elements on the page."""
        pass
