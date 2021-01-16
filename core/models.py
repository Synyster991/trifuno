from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    link = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def summary(self):
        return self.description[:75]


class News(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    link = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def summary(self):
        return self.description[:50]


class Feedback(models.Model):
    person = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.person, self.company)


class Retailers(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name 


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField(default="")
    email = models.EmailField()
    company = models.CharField(max_length=255, default="")
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return "{} - {} ({})".format(self.full_name, self.company, self.date)