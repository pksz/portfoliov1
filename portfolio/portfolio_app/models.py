from django.db import models
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_delete
import os
# Create your models here.

class ProjectDetails(models.Model):
    project_name=models.CharField(max_length=50) 
    project_description=models.TextField(max_length=10000) #this goes in the detail view
    project_summary=models.CharField(max_length=300) #this goes in the main page
    project_img=models.ImageField(blank=True,null=True,upload_to='project_images/',default='project_images/default.webp')
    #resume=models.FileField(blank=True,null=True,upload_to='project_images/')
    #add a way to sort them by assigning a priority to each item
    priority=models.PositiveSmallIntegerField(blank=True,null=True)

    def __str__(self):
        return self.project_name
    
    #resize the image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.project_img:
            img_path = self.project_img.path
            img = Image.open(img_path)
            if img.height > 400 or img.width > 300:
                output_size = (400, 300)
                img.thumbnail(output_size, Image.LANCZOS)
                img.save(img_path)

# Signal to delete the image file when the project is deleted
@receiver(post_delete, sender=ProjectDetails)
def delete_project_img(sender, instance, **kwargs):
    if instance.project_img and instance.project_img.name!='project_images/default.webp':
        if os.path.isfile(instance.project_img.path) :
            os.remove(instance.project_img.path)