from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# import django.db.models.signals.pre_save
# import django.dispatch.receiver



# Create your models here.

class User(AbstractUser):
	imie = models.CharField('Imię', max_length = 100)
	nazwisko = models.CharField(max_length = 100)
	# login = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	data_ur = models.DateField('Data urodzenia', blank = True, null = True)
	# adres = models.CharField(max_length = 100, blank = True)
	# adres2 = models.CharField(max_length = 100, blank = True)
	# nr_tel = models.CharField(max_length = 100, blank = True)
	# nr_tel2 = models.CharField(max_length = 100, blank = True)
	projekty = models.TextField(blank=True)

	def __str__(self):
		return self.imie + ' ' + self.nazwisko
	pass

# class Architekt(models.Model):

# 	imie = models.CharField('Imię', max_length = 100)
# 	nazwisko = models.CharField(max_length = 100)
# 	data_ur = models.DateField('Data urodzenia', blank = True, null = True)
# 	adres = models.CharField(max_length = 100, blank = True)
# 	adres2 = models.CharField(max_length = 100, blank = True)
# 	nr_tel = models.CharField(max_length = 100, blank = True)
# 	nr_tel2 = models.CharField(max_length = 100, blank = True)
# 	projekty = models.TextField()

# 	def project_count(self):
# 		return 'to_do'

# 	def __str__(self):
# 		return self.imie

class Projekt(models.Model):
	grafika = models.ImageField(upload_to='images/')
	nazwa = models.CharField(max_length = 100)
	rok_powstania = models.CharField(max_length = 100, blank = True)
	architekt = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.nazwa


# @receiver(pre_save, sender=Projekt)
# def instantiate_arhitect(sender, instance, raw, using, **kwargs):
# 	pass
# 	# instance.arhitekt