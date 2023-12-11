import unittest
from datetime import date
from unittest.mock import patch

from src.models.EventManager import EventManager
from src.models.Payment import Payment
from src.models.PaymentEventListener import PaymentEventListener


class TestPayment(unittest.TestCase):
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Payment conferindo se os
        atributos foram definidos corretamente.
        """
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        self.assertIsInstance(payment, Payment)
        self.assertEqual(payment.id_payment, '1')
        self.assertEqual(payment.value, 10.0)
        self.assertEqual(payment.payment_date, date(2021, 1, 1))
        self.assertEqual(payment.reference_date, date(2021, 1, 1))
        self.assertEqual(payment.id_administrator, '1')
        self.assertEqual(payment.id_beneficiary, '1')
        self.assertTrue(payment.paid)

    def test_getters(self) -> None:
        """
        Testa os getters da classe Payment conferindo se
        eles retornam os valores corretos.
        """
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        self.assertEqual(payment.id_payment, '1')
        self.assertEqual(payment.value, 10.0)
        self.assertEqual(payment.payment_date, date(2021, 1, 1))
        self.assertEqual(payment.reference_date, date(2021, 1, 1))
        self.assertEqual(payment.id_administrator, '1')
        self.assertEqual(payment.id_beneficiary, '1')
        self.assertTrue(payment.paid)

    def test_setters(self) -> None:
        """
        Testa os setters da classe Payment conferindo se
        eles atribuem os valores corretos.
        """
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        payment.id_payment = '2'
        payment.value = 20.0
        payment.payment_date = date(2021, 1, 2)
        payment.reference_date = date(2021, 1, 3)
        payment.id_administrator = '2'
        payment.id_beneficiary = '2'
        payment.paid = False
        self.assertEqual(payment.id_payment, '2')
        self.assertEqual(payment.value, 20.0)
        self.assertEqual(payment.payment_date, date(2021, 1, 2))
        self.assertEqual(payment.reference_date, date(2021, 1, 3))
        self.assertEqual(payment.id_administrator, '2')
        self.assertEqual(payment.id_beneficiary, '2')
        self.assertFalse(payment.paid)

    def test_payment_date_setter_limitation(self) -> None:
        """
        Testa o setter da classe Payment conferindo se
        ele não permite que o atributo payment_date seja
        menor que o atributo reference_date.
        """
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 3),
            reference_date=date(2021, 1, 3),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        with self.assertRaises(ValueError):
            payment.payment_date = date(2021, 1, 2)
        self.assertEqual(payment.payment_date, date(2021, 1, 3))

    def test_value_setter_limitation(self) -> None:
        """
        Testa o setter da classe Payment conferindo se ele não
        permite que o atributo value seja menor que zero.
        """
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        with self.assertRaises(ValueError):
            payment.value = -1.0
        self.assertEqual(payment.value, 10.0)

    def test_is_event_manager_subclass(self):
        """
        Testa se a classe Payment é subclasse da classe
        EventManager.
        """
        self.assertTrue(issubclass(Payment, EventManager))

    def test_if_payment_event_listener_is_added_on_constructor(self) -> None:
        """
        Testa se um listener do tipo PaymentEventListener é adicionado
        no construtor da classe Payment.
        """
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        self.assertTrue(any(isinstance(listener, PaymentEventListener) for listener in payment.listeners))

    @patch.object(Payment, 'notify')
    def test_value_setter_calls_notify(self, mock_notify):
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        payment.value = 10.0
        self.assertTrue(mock_notify.called)

    @patch.object(Payment, 'notify')
    def test_payment_date_setter_calls_notify(self, mock_notify):
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        payment.payment_date = date(2021, 1, 2)
        self.assertTrue(mock_notify.called)

    @patch.object(Payment, 'notify')
    def test_reference_date_setter_calls_notify(self, mock_notify):
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        payment.reference_date = date(2021, 1, 2)
        self.assertTrue(mock_notify.called)

    @patch.object(Payment, 'notify')
    def test_id_administrator_setter_calls_notify(self, mock_notify):
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2020, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        payment.id_administrator = '2'
        self.assertTrue(mock_notify.called)

    @patch.object(Payment, 'notify')
    def test_id_beneficiary_setter_calls_notify(self, mock_notify):
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2020, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        payment.id_beneficiary = '2'
        self.assertTrue(mock_notify.called)

    @patch.object(Payment, 'notify')
    def test_paid_setter_calls_notify(self, mock_notify):
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 2),
            reference_date=date(2020, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        payment.paid = False
        self.assertTrue(mock_notify.called)

    @patch.object(PaymentEventListener, 'update')
    def test_payment_event_listener_update_is_called(self, mock_update):
        payment = Payment(
            id_payment='1',
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
            id_administrator='1',
            id_beneficiary='1',
            paid=True,
        )
        payment.value = 20.0
        self.assertTrue(mock_update.called)


if __name__ == "__main__":
    unittest.main()
