from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"
    
class Participant(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.email}"
    
class Meeting(models.Model):
    title = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default="noimage.jpg")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant,blank=True)
    
    def __str__(self):
        return f"{self.title}"
    