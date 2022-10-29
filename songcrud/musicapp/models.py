from django.db import models

# Create your models here.
class Artiste(models.Model):
	first_name = models.CharField(max_length=28)
	last_name = models.CharField(max_length=28)
	age = models.IntegerField(default=0)
 
def __str__(self) -> str:
    return self.first_name
    
    			
class Song(models.Model):
	title = models.CharField(max_length=28)
	date_released = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0)
	artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
 
def __str__(self) -> str:
    return self.title

			
class Lyric(models.Model):
	content = models.CharField(max_length=255)
	song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
 
def __str__(self) -> str:
    return self.content


 
