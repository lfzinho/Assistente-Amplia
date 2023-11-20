import unittest
import numpy as np

from cpf_class_and_run import CPFVerifier

CPF_INVALIDO = "090.089.237-00"
CPF_VALIDO = "3.4.5.1.1.5.8.9.8.1.0"
MAMAE_FALEI = "34511589810"
JAIR = "45317828791"
FAZUELI = "07068093868"

MAMAE_FALEI_ARR = np.fromiter(MAMAE_FALEI, dtype=int)
JAIR_ARR = np.fromiter(JAIR, dtype=int)
FAZUELI_ARR = np.fromiter(FAZUELI, dtype=int)
CPF_CURTO = FAZUELI[:-1]


class CPFTestCase(unittest.TestCase):

    def test_wrong_length(self):
        cpf_valid = CPFVerifier.validate_cpf(CPF_CURTO)
        self.assertEqual(cpf_valid, False)

    def test_remove_special_characters_1(self):
        cpf_output = CPFVerifier.remove_special_characters(CPF_INVALIDO)
        self.assertEqual(cpf_output, "09008923700")

    def test_remove_special_characters_2(self):
        cpf_output = CPFVerifier.remove_special_characters(CPF_VALIDO)
        self.assertEqual(cpf_output, "34511589810")

    def test_compute_first_veryfing_digit_1(self):
        ver_digit = CPFVerifier.compute_verifying_digit(MAMAE_FALEI_ARR[:9])
        self.assertEqual(ver_digit, int(MAMAE_FALEI[9]))

    def test_compute_second_veryfing_digit_1(self):
        ver_digit = CPFVerifier.compute_verifying_digit(MAMAE_FALEI_ARR[:10])
        self.assertEqual(ver_digit, int(MAMAE_FALEI_ARR[10]))

    def test_compute_first_veryfing_digit_2(self):
        ver_digit = CPFVerifier.compute_verifying_digit(JAIR_ARR[:9])
        self.assertEqual(ver_digit, int(JAIR[9]))

    def test_compute_second_veryfing_digit_2(self):
        ver_digit = CPFVerifier.compute_verifying_digit(JAIR_ARR[:10])
        self.assertEqual(ver_digit, int(JAIR_ARR[10]))

    def test_compute_first_veryfing_digit_3(self):
        ver_digit = CPFVerifier.compute_verifying_digit(FAZUELI_ARR[:9])
        self.assertEqual(ver_digit, int(FAZUELI[9]))

    def test_compute_second_veryfing_digit_3(self):
        ver_digit = CPFVerifier.compute_verifying_digit(FAZUELI_ARR[:10])
        self.assertEqual(ver_digit, int(FAZUELI_ARR[10]))

    def test_invalid_cpf(self):
        cpf_clear = CPFVerifier.remove_special_characters(CPF_INVALIDO)
        cpf_valid = CPFVerifier.validate_cpf(cpf_clear)
        self.assertFalse(cpf_valid, False)

    def test_valid_cpf(self):
        cpf_clear = CPFVerifier.remove_special_characters(CPF_VALIDO)
        cpf_valid = CPFVerifier.validate_cpf(cpf_clear)
        self.assertTrue(cpf_valid, True)


if __name__ == "__main__":
    unittest.main()
