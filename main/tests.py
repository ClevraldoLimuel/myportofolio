from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from main.models import Experience, Interest, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            started_at=date(2025, 1, 1),
        )
        self.interest = Interest.objects.create(
            name="Tempe Goreng",
            description="Tempe Goreng yang keemasan bermandikan minyak sawit",
            category="leisure",
        )
        self.education = Education.objects.create(
            school_name="SMAN 99 Ngawi",
            location="Ngawi, Jawa Tengah",
            degree="high",
            admission_year=6767,
            ongoing=True,
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    # TestCases for Experience
    # Data experience dirender lewat AJAX, jadi isi datanya dites di
    # tests_experience_api.py. Di sini hanya model dan kerangka halamannya.

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertEqual(self.experience.started_at, date(2025, 1, 1))
        self.assertTrue(self.experience.is_ongoing)

    def test_completed_experience(self):
        self.experience.ended_at = date(2025, 6, 1)
        self.experience.save()
        self.experience.refresh_from_db()

        self.assertFalse(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="experience-search-form"')
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:experience-list"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        # Data diambil via fetch(), tidak ikut dirender server.
        self.assertNotContains(response, self.experience.title)

    def test_empty_experience_list_from_api(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("api:experience-list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_add_experience_button_only_for_superuser(self):
        url = reverse("main:show_experience")
        self.assertNotContains(self.client.get(url), "Tambah Pengalaman")

        User.objects.create_superuser(username="owner", password="test-password")
        self.client.login(username="owner", password="test-password")
        self.assertContains(self.client.get(url), "Tambah Pengalaman")

    # TestCases for Interests

    def test_interest_model(self):
        self.assertEqual(str(self.interest), "Tempe Goreng")
        self.assertEqual(self.interest.name, "Tempe Goreng")
        self.assertEqual(self.interest.category, "leisure")
        self.assertEqual(self.interest.description, "Tempe Goreng yang keemasan bermandikan minyak sawit")

    def test_interest_page(self):
        response = self.client.get(reverse("main:show_interest"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interest.html")
        self.assertContains(response, self.interest.name)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_interest_page(self):
        Interest.objects.all().delete()
        response = self.client.get(reverse("main:show_interest"))

        self.assertContains(response, "Umm..")

    # TestCases for Education

    def test_education_model(self):
        self.assertEqual(str(self.education), "SMAN 99 Ngawi")
        self.assertEqual(self.education.school_name, "SMAN 99 Ngawi")
        self.assertEqual(self.education.location, "Ngawi, Jawa Tengah")
        self.assertEqual(self.education.degree, "high")
        self.assertEqual(self.education.admission_year, 6767)
        self.assertEqual(self.education.ongoing, True)

    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.school_name)
        self.assertContains(response, self.education.location)
        self.assertContains(response, "Current")
        self.assertContains(response, self.education.admission_year)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "NO DATA")