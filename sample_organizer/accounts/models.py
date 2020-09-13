from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Executor(models.Model):
    DEGREE = (
        ('Prof.', 'Prof.'),
        ('PhD', 'PhD'),
        ('MSc', 'MSc'),
        ('Eng.', 'Eng.'),
        ('---', '---')
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, choices=DEGREE, null=True)
    phone = models.FloatField(max_length=9, null=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(default="profile1.png", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.degree} {self.first_name} {self.last_name}"

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Sample(models.Model):
    CATEGORY = (
        ('10 x 10 x 10', '10 x 10 x 10'),
        ('15 x 15 x 15', '15 x 15 x 15'),
        ('10 x 10 x 50', '10 x 10 x 50'),
        ('15 x 15 x 70', '15 x 15 x 70'),
    )
    MODIFICATION = (
        ('steel fibers', 'steel fibers'),
        ('glass fibers', 'glass fibers'),
        ('polypropylene fibers', 'polypropylene fibers'),
        ('kaoline', 'kaoline'),
        ('zeolite', 'zeolite'),
    )
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    modification = models.CharField(max_length=100, null=True, choices=MODIFICATION)
    description = models.CharField(max_length=400, null=True)
    date_of_production = models.DateField(default=datetime.now())
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.name} {self.category} modificated with {self.modification} at {self.date_of_production}"

class Test(models.Model):
    STATUS = (
        ('In Production', 'In Production'),
        ('In Research', 'In Research'),
        ('Tested', 'Tested'),
    )
    executor = models.ForeignKey(Executor, null=True, on_delete=models.SET_NULL)
    sample = models.ForeignKey(Sample, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, null=True, choices=STATUS)

    def __str__(self):
        return f"{self.sample.name}"
