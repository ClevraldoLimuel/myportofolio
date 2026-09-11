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
    
class Interest(models.Model):
    INTEREST_CATEGORY = [
        ('technology', 'Tech'),
        ('creative', 'Creative'),
        ('leisure', 'Leisure')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.CharField(max_length=32, choices=INTEREST_CATEGORY)
    
    def __str__(self):
        return self.name
    
class Education(models.Model):
    DEGREE_CHOICE = [('elementary', 'Sekolah Dasar'), ('middle', 'Sekolah Menengah Pertama'), ('high', 'Sekolah Menengah Atas'),
                    ('bachelor', 'S1'), ('master', 'S2'), ('doctorate', 'S3')]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=16, choices=DEGREE_CHOICE)
    admission_year = models.PositiveSmallIntegerField()
    ongoing = models.BooleanField(default=False)
    def __str__(self):
        return self.school_name