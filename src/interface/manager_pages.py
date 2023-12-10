from abc import ABC

import pandas as pd
import streamlit as st

from forms import *
from src.authentication.authentication import Authentication

# class ManagerPage(ABC):
#     def __init__(
#         self,
#         title: str,
#         description: str,
#         creation_form: CreationForm,
#         update_form: UpdateForm,
#         deletion_form: DeletionForm,
#         db_collection: str = None
#     ):
#         self.title = title
#         self.description = description
#         self.creation_form = creation_form
#         self.update_form = update_form
#         self.deletion_form = deletion_form
#         self.db_collection = db_collection

#     @abstractmethod
#     def show_table(self):
#         """Shows the table of the managed elements on the page."""
#         pass

#     def show_creation_form(self):
#         """Shows the creation form on the page."""
#         self.creation_form.render()

#     def show_update_form(self):
#         """Shows the update form on the page."""
#         self.update_form.render()

#     def show_deletion_form(self):
#         """Shows the deletion form on the page."""
#         self.deletion_form.render()

#     def show_form_tabs(self):
#         """Shows all forms in a tab organization."""
#         creation_tab, update_tab, deletion_tab = st.tabs(
#             ['Criação', 'Atualização', 'Deleção']
#         )
#         with creation_tab:
#             self.show_creation_form()
#         with update_tab:
#             self.show_update_form()
#         with deletion_tab:
#             self.show_deletion_form()

#     def render(self):
#         """Renders the page in the usual organization."""
#         st.title(self.title)
#         st.write(self.description)
#         self.show_table()
#         self.show_form_tabs()


class ManagerPage(ABC):
    def __init__(
        self,
        title: str,
        description: str,
        creation_form: CreationForm,
        update_form: UpdateForm,
        deletion_form: DeletionForm,
        db_collection: str = None
    ) -> None:
        self.title = title
        self.description = description
        self.creation_form = creation_form
        self.update_form = update_form
        self.deletion_form = deletion_form
        self.db_collection = db_collection
        self.db_manager = DatabaseManager.instance()
        self.auth = Authentication()

    def show_table(self) -> None:
        """Shows the table of the managed elements on the page."""
        st.subheader("Tabela de Elementos")
        query = self.db_manager.get_all(self.db_collection)
        if query == {}:
            st.write("Ainda não há nenhum elemento cadastrado.")
        else:
            df = pd.DataFrame(query)
            st.dataframe(df.T)

    def show_creation_form(self) -> None:
        """Shows the creation form on the page."""
        self.creation_form.render()

    def show_update_form(self) -> None:
        """Shows the update form on the page."""
        self.update_form.render()

    def show_deletion_form(self) -> None:
        """Shows the deletion form on the page."""
        self.deletion_form.render()

    def show_form_tabs(self) -> None:
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

    def render(self) -> None:
        """Renders the page in the usual organization."""
        if (
            "uid" in st.session_state
            and self.auth.get_user_by_uid(st.session_state["uid"]) is not None
        ):
            st.title(self.title)
            st.write(self.description)
            self.show_table()
            self.show_form_tabs()
        else:
            st.warning("Você precisa estar autenticado "
                       "para acessar esta página.")


class PersonPage(ManagerPage):
    def __init__(self) -> None:
        super().__init__(
            title="Página de Pessoa",
            description="Gerencie as pessoas do sistema.",
            creation_form=PersonCreationForm(),
            update_form=PersonUpdateForm(),
            deletion_form=PersonDeletionForm(),
            db_collection="person"
        )


class BeneficiaryPage(ManagerPage):
    def __init__(self) -> None:
        super().__init__(
            title="Página de Beneficiário",
            description="Gerencie os beneficiários do sistema.",
            creation_form=BeneficiaryCreationForm(),
            update_form=BeneficiaryUpdateForm(),
            deletion_form=BeneficiaryDeletionForm(),
            db_collection="beneficiary"
        )


class StudentPage(ManagerPage):
    def __init__(self) -> None:
        super().__init__(
            title="Página de Estudante",
            description="Gerencie os estudantes do sistema.",
            creation_form=StudentCreationForm(),
            update_form=StudentUpdateForm(),
            deletion_form=StudentDeletionForm(),
            db_collection="student"
        )


class TeacherPage(ManagerPage):
    def __init__(self) -> None:
        super().__init__(
            title="Página de Professor",
            description="Gerencie os professores do sistema.",
            creation_form=TeacherCreationForm(),
            update_form=TeacherUpdateForm(),
            deletion_form=TeacherDeletionForm(),
            db_collection="teacher"
        )


class AnalystPage(ManagerPage):
    def __init__(self) -> None:
        super().__init__(
            title="Página de Analista",
            description="Gerencie os analistas do sistema.",
            creation_form=AnalystCreationForm(),
            update_form=AnalystUpdateForm(),
            deletion_form=AnalystDeletionForm(),
            db_collection="analyst"
        )


class DirectorPage(ManagerPage):
    def __init__(self) -> None:
        super().__init__(
            title="Página de Diretor",
            description="Gerencie os diretores do sistema.",
            creation_form=DirectorCreationForm(),
            update_form=DirectorUpdateForm(),
            deletion_form=DirectorDeletionForm(),
            db_collection="director"
        )


class AdministratorPage(ManagerPage):
    def __init__(self) -> None:
        super().__init__(
            title="Página de Administrador",
            description="Gerencie os administradores do sistema.",
            creation_form=AdministratorCreationForm(),
            update_form=AdministratorUpdateForm(),
            deletion_form=AdministratorDeletionForm(),
            db_collection="administrator"
        )


class PresenceListPage(ManagerPage):
    def __init__(self) -> None:
        super().__init__(
            title="Página de Lista de Presença",
            description="Gerencie as listas de presença do sistema.",
            creation_form=PresenceListCreationForm(),
            update_form=PresenceListUpdateForm(),
            deletion_form=PresenceListDeletionForm(),
            db_collection="presence_list"
        )


class PaymentPage(ManagerPage):
    def __init__(self) -> None:
        super().__init__(
            title="Página de Pagamento",
            description="Gerencie os pagamentos do sistema.",
            creation_form=PaymentCreationForm(),
            update_form=PaymentUpdateForm(),
            deletion_form=PaymentDeletionForm(),
            db_collection="payment"
        )
