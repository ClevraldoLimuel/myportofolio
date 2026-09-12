from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Interest, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
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

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")
        
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
    
    # Testcases for Education
    
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