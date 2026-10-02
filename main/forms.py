from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError

from main.models import Project, Interest, Experience

class InterestForm(ModelForm):
    class Meta:
        model = Interest
        fields = [
            "name",
            "description",
            "category"
        ]
        
        labels = {
            "name" : "Nama Minat",
            "description" : "Deskripsi Peminatan",
            "category" : "Kategori Peminatan"
        }
        
        widgets = {
            "name" : TextInput(
                attrs={
                    "placeholder": "Web Development",
                    "max_length": 255
                }
            ),
            
            "description" : Textarea(
                attrs={
                    "placeholder": "Ceritakan minatmu",
                    "rows": 2,
                }
            ),
            
            "category" : Select(
                attrs={
                    "required" : True,
                    "class": "category-select",
                }
            )
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
    
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title", "description", "category", "thumbnail", "started_at", "ended_at"
        ]
        labels = {
            "title" : "Nama Pengalaman",
            "description" : "Deskripsi pengalaman",
            "category" : "Kategori pengalaman",
            "thumbnail" : "URL gambar thumbnail",
            "started_at" : "Tanggal mulai pengalaman",
            "ended_at" : "Tanggal akhir pengalaman"
        }
        widgets = {
            "title" : TextInput(
                attrs={
                    "placeholder":"Apa pengalamanmu",
                    "maxlength":255,
                }
            ),
            "description" : Textarea(
                attrs={
                    "placeholder":"Ceritakan pengalamanmu",
                    "rows":3,
                }  
            ),
            "category" : Select(
                attrs={
                    "required" : True,
                    "class": "category-select",
                }
            ),
            "thumbnail" : URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "started_at" : DateInput(
                attrs={
                    "type" : "date",
            }),
            "ended_at" : DateInput(
                attrs={
                    "type" : "date",
                    "required" : False,
                }
            )
        }
    
    def clean_date(self):
        cleaned_date= super().clean()

        start_date = cleaned_date.get('start_date')
        end_date = cleaned_date.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError(
                    "Start date cannot be later than end date."
                )
        return cleaned_date
    
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama pengalaman tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()