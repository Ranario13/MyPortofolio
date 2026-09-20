from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, NumberInput, DateInput
from main.models import Project, Experience, Education, Skill

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
                    "placeholder": "https://...",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Judul / Posisi",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Software Engineer Intern",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan peran dan pencapaianmu",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "start_year",
            "end_year",
            "description",
        ]

        labels = {
            "institution": "Nama Institusi",
            "degree": "Jenjang Pendidikan",
            "start_year": "Tahun Mulai",
            "end_year": "Tahun Selesai",
            "description": "Deskripsi",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                }
            ),
            "degree": Select(),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "2022",
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "Kosongkan jika masih menempuh pendidikan",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Detail jurusan atau pencapaian",
                    "rows": 3,
                }
            ),
        }

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "name",
            "category",
            "description",
            "proficiency_level",
        ]

        labels = {
            "name": "Nama Keahlian",
            "category": "Kategori",
            "description": "Deskripsi Keahlian",
            "proficiency_level": "Tingkat Kemahiran (1-100)",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Python / Django",
                }
            ),
            "category": Select(),
            "description": Textarea(
                attrs={
                    "placeholder": "Penjelasan singkat",
                    "rows": 3,
                }
            ),
            "proficiency_level": NumberInput(
                attrs={
                    "placeholder": "85",
                    "min": 1,
                    "max": 100,
                }
            ),
        }