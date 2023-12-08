import re
import numpy as np


class CPFVerifier:
    """
    Verificador de validez de CPF.

    Parâmetros
    ----------
    cpf : str
        CPF a ser validado.
    """
    VER_INDEX_1: int = 9
    VER_INDEX_2: int = 10

    def __init__(self, cpf: str):
        self.cpf = cpf

    @staticmethod
    def remove_special_characters(cpf: str) -> str:
        """
        Remove caracteres especiais do CPF.

        Parâmetros
        ----------
        cpf : str
            CPF com caracteres especiais.

        Retorna
        -------
        str
            CPF sem caracteres especiais.
        """
        return re.sub(r"[^0-9]", "", cpf)

    @staticmethod
    def compute_verifying_digit(array: np.ndarray) -> int:
        """
        Computa o dígito verificador multiplicando os elementos
        do array pelos pesos e somando os resultados.

        Parâmetros
        ----------
        array : numpy.ndarray
            Array com os números do CPF.

        Retorna
        -------
        int
            Dígito verificador.
        """
        weights = np.arange(len(array) + 1, 1, -1)
        ver_digit = (np.dot(array, weights) * 10) % 11
        if ver_digit > 9:
            ver_digit = 0

        return ver_digit

    @classmethod
    def validate_cpf(cls, cpf: str) -> bool:
        """
        Valida os dois dígitos verificadores do CPF.

        Parâmetros
        ----------
        cpf : str
            CPF a ser validado.

        Retorna
        -------
        bool
            True se o CPF for válido, False caso contrário.
        """
        # Transforma o CPF em um array de inteiros
        cpf_arr: np.ndarray[int] = np.fromiter(cpf, dtype=int)
        if len(cpf_arr) != 11:
            return False

        ver_digit_1 = cls.compute_verifying_digit(cpf_arr[:cls.VER_INDEX_1])
        if cpf_arr[cls.VER_INDEX_1] != ver_digit_1:
            return False

        ver_digit_2 = cls.compute_verifying_digit(cpf_arr[:cls.VER_INDEX_2])
        if cpf_arr[cls.VER_INDEX_2] != ver_digit_2:
            return False
        return True

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        cpf = CPFVerifier.remove_special_characters(cpf)
        if CPFVerifier.validate_cpf(cpf):
            self._cpf = cpf
        else:
            raise ValueError("CPF inválido")


if __name__ == "__main__":
    cpf_input = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
    try:
        cpf = CPFVerifier(cpf_input)
        print("CPF válido")
    except ValueError as e:
        print(e)
