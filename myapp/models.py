from django.db import models

# Create your models here.
GENDER = (
	('M', 'male'),
	('F', 'female'),
)

"""
Create a custom users model for simulation, let the
admin add users for testing since
users authentication was not specified in the test.
"""

class TestUser(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    gender = models.CharField(choices=GENDER, max_length=5)
    status = models.CharField(max_length=254, default="inactive")
    date_created =  models.DateTimeField(auto_now_add=True)