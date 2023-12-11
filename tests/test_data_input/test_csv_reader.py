from datetime import datetime
import io
from typing import Any
import unittest

from src.data_input.csv_reader import CSV
from src.exceptions.data_input import InvalidCSV


class TestCSVReader(unittest.TestCase):
    keys = ['class_name', 'reference_date', 'payment_date', 'value']
    header = 'Cabeçalhos\nDescrições\n'
    data = (
        header +
        '2001/11/08,2024/01/02,"R$ 123,45"\n'
        '2002/09/16,2024/01/02,"R$ 420,69"\n'
        '2003/02/04,2024/02/29,"11.11"\n'
    )

    broken_data = (
        header +
        '2001/11/08,"R$ 00,00"\n'
        '2000/01/01,2010/10/10,"R$ 10,00"\n'
    )

    invalid_data = (
        header +
        '2002/01/09,2023/12/31,"R $ 00,00"\n'
        '2001/10/22,1970/01/01,"R$ 10.00"\n'
    )

    def __create_reader(self, msg: str) -> CSV:
        return CSV(
            io.BytesIO(msg.encode('utf-8')),
            'test', 'test', []
        )

    def __dict_from_values(self, values: list) -> dict[str, Any]:
        return dict(zip(self.keys, values))

    def test_get_form_values(self) -> None:
        csv = self.__create_reader(self.data)

        # Testa os valores de cada linha dos dados váliods
        self.assertEqual(
            csv.get_form_values(),
            self.__dict_from_values([
                'Payment', datetime(2001, 11, 8), datetime(2024, 1, 2), 123.45
            ])
        )
        self.assertEqual(
            csv.get_form_values(),
            self.__dict_from_values([
                'Payment', datetime(2002, 9, 16), datetime(2024, 1, 2), 420.69
            ])
        )
        self.assertEqual(
            csv.get_form_values(),
            self.__dict_from_values([
                'Payment', datetime(2003, 2, 4), datetime(2024, 2, 29), 11.11
            ])
        )
        # Testa se a iteração termina e retorna dicionários vazios
        self.assertEqual(csv.get_form_values(), {})

    def test_broken_csv(self) -> None:
        """Testa CSV com número desigual de colunas."""
        with self.assertRaises(InvalidCSV):
            self.__create_reader(self.broken_data)

    def test_invalid_csv(self) -> None:
        """
        Testa a leitura de valores não formatados corretamente
        e se a iteração continua na próxima linha após o erro.
        """
        csv = self.__create_reader(self.invalid_data)
        self.assertRaises(InvalidCSV, csv.get_form_values)
        self.assertNotEqual(csv.get_form_values(), {})


if __name__ == '__main__':
    unittest.main()
