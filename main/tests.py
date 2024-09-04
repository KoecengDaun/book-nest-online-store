from django.test import TestCase
from django.urls import reverse

class ShowMainViewTest(TestCase):
    def test_show_main_view_status_code(self):
        # Menguji apakah view show_main dapat diakses dengan status 200 OK
        response = self.client.get(reverse('show_main'))
        self.assertEqual(response.status_code, 200)

    def test_show_main_view_template(self):
        # Menguji apakah view show_main menggunakan template yang benar
        response = self.client.get(reverse('show_main'))
        self.assertTemplateUsed(response, 'main.html')

    def test_show_main_view_context(self):
        # Menguji apakah context yang dikirimkan view mengandung 'products' (meski kosong)
        response = self.client.get(reverse('show_main'))
        self.assertIn('products', response.context)
        self.assertEqual(len(response.context['products']), 0)  # Menguji bahwa tidak ada produk
