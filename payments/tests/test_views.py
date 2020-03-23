from django.test import TestCase, Client
from django.urls import reverse
from payments.views import HomeView
from payments.models import Obliged, Payment

class TestHomeView(TestCase):
    def test_view_url_exists(self):
        response = self.client.get('/payments/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse(('payments:HomeView')))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('payments:HomeView'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/home.html')

class TestIndexView(TestCase):
    def test_view_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse(('payments:HomeView')))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('payments:HomeView'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/home.html')

class TestPaymentById(TestCase):
    def setUp(self):
        self.obliged =Obliged.objects.create(
            full_name='Test Name', email='testName@test.com'
        )
        Payment.objects.create(
            name='testName', payment_code='100-200-300', description='test',
            amount=20.32, obliged=self.obliged, date='2020-02-02'
        )
        self.payment = Payment.objects.get(id=1)

    def test_valid_id(self):
        self.assertEqual(self.payment.name, 'testName')

    def test_invalid_id(self):
        with self.assertRaises(Payment.DoesNotExist):
            Payment.objects.get(id=2)

    def test_view_url_exists(self):
        response = self.client.get(reverse('payments:payment_by_id',
                                           kwargs={'id': self.payment.id}))
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('payments:payment_by_id',
                                            kwargs={'id': self.payment.id}))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('payments:payment_by_id',
                                           kwargs={'id': self.payment.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/payment.html')