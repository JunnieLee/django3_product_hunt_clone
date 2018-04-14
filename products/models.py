from django.db import models
from django.contrib.auth.models import User # We're importing another model and using it in this models file

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=255)
	url = models.TextField()
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='icons/')
	body = models.TextField()   
	                                # if the user is deleted, we're also gonna delete this product
	hunter = models.ForeignKey(User, on_delete=models.CASCADE) 
	        # This is how you can connect multiple models inside of a database
	        # ForeignKey -> Go and get the user object from another model 
	pub_date = models.DateTimeField()
	votes_total = models.IntegerField(default=1)           

	def __str__(self):
		return self.title # django admin에서의 각 object display방식을 title로 나타내게 설정하기!

	def summary(self):
		return self.body[:100]	

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y') # customizing the date details

# Create a migration

# Migrate

# Add to the Admin		