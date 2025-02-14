from django.db import models
import PIL
# Create your models here.

class ProjectDetails(models.Model):
    project_name=models.CharField(max_length=50) 
    project_description=models.TextField(max_length=1000) #this goes in the detail view
    project_summary=models.CharField(max_length=100) #this goes in the main page
    project_img=models.ImageField(blank=True,null=True)
    
    #add a way to sort them by assigning a priority to each item
    priority=models.PositiveSmallIntegerField(blank=True,null=True)

    def __str__(self):
        return self.project_name