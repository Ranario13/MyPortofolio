import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    DEGREE_CHOICES = [
        ('highschool', 'High School'),
        ('bachelor', 'Bachelor Degree (S1)'),
        ('certification', 'Certification/Course'),        
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    start_year = models.IntegerField()
    # Menggunakan blank=True, null=True agar bisa dikosongkan jika belum lulus
    end_year = models.IntegerField(blank=True, null=True) 
    description = models.TextField()

    def __str__(self):
        return f"{self.institution} - {self.get_degree_display()}"
        
    @property
    def is_ongoing(self):
        return self.end_year is None

class Skill(models.Model):
    # Menggunakan Choices untuk Kategori Keahlian
    CATEGORY_CHOICES = [
        ('frontend', 'Front-End Development'),
        ('backend', 'Back-End Development'),
        ('design', 'UI/UX Design'),
        ('softskill', 'Soft Skill'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='softskill')
    description = models.TextField()
    proficiency_level = models.IntegerField(help_text="Tingkat kemahiran (1-100)")

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
