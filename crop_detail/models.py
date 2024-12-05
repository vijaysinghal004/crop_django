from django.db import models

class Wheat(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Sorghum_Jowar(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Chickpeas_Gram(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Red_Gram(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Lentils_Masoor(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Groundnut_Peanut(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Sunflower(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Mustard(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Tomato(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Chili(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Brinjal(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Carrot(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Radish(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Spinach(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Coriander(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)

class Fenugreek(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=50)


