from django.db import models

class Wheat(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Sorghum_Jowar(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Chickpeas_Gram(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Red_Gram(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Lentils_Masoor(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Groundnut_Peanut(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=5000)

class Sunflower(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Mustard(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Tomato(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Chili(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Brinjal(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Carrot(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Radish(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Spinach(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Coriander(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)

class Fenugreek(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    image=models.CharField(max_length=500)


