from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description =models.TextField()
    link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def save_project(self):
        self.save
        
    def delete_project(self):
        self.delete   
        
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects    
    
    def __str__(self):
        return self.title     