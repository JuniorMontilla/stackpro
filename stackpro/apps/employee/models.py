from django.db import models
from django.utils import timezone

class advert(models.Model):
	def avatarcompany(self,filename):
		mediaroute = 'MultimediaData/{0}/{1}'.format(self.company,filename)
		return mediaroute 

	status      	 = models.BooleanField(blank=True) 
	avatar      	 = models.ImageField(upload_to=avatarcompany, null=False,blank=False)
	company     	 = models.CharField(max_length=100)
	website     	 = models.CharField(max_length=100)
	titleofemployee  = models.CharField(max_length=200) 
	place       	 = models.CharField(max_length=100)
	salary      	 = models.PositiveIntegerField()
	descriptionofjob = models.TextField(max_length=50000)	
	prove       	 = models.TextField(max_length=50000)
	pub_date         = models.DateTimeField(default=timezone.now())

class answer(models.Model):
	links      = models.CharField(max_length=200)
	email      = models.CharField(max_length=50)
	fk         = models.ForeignKey(advert)

	def __unicode__(self):
		return self.links