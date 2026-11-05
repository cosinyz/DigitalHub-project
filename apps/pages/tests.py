from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class ContactViewTests(TestCase):
    def test_get_displays_contact_form(self):
        response = self.client.get(reverse('pages:contacts'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'method="post"')
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_valid_post_saves_message_and_redirects(self):
        response = self.client.post(
            reverse('pages:contacts'),
            {
                'name': 'Алексей',
                'email': 'alex@example.com',
                'phone': '+7 123 456-78-90',
                'message': 'Нужен сайт для компании',
            },
        )

        self.assertRedirects(
            response,
            reverse('pages:contacts'),
            fetch_redirect_response=False,
        )
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.get().email, 'alex@example.com')

        response = self.client.get(reverse('pages:contacts'))
        self.assertContains(response, 'Спасибо! Ваша заявка отправлена.')

    def test_invalid_post_does_not_save_message(self):
        response = self.client.post(
            reverse('pages:contacts'),
            {'name': '', 'email': 'not-an-email', 'phone': '', 'message': ''},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertContains(response, 'Введите корректный email')
