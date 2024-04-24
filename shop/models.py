from django.db import models

class Shop(models.Model):
    image = models.ImageField('photo/')
    description = models.TextField(max_length=1000)


    def __int__(self):
        return self.id


class Laptops(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='laptops/')

    def __str__(self):
        return f"{self.name}"


class Rassrochka(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='rassrochka/')

    def __str__(self):
        return self.name

class Background(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='background/')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Karusel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='acer/')

    def __str__(self):
        return self.name

class About(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='service/')

    def __str__(self):
        return self.name

class Serivce2(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='service2/')

    def __str__(self):
        return self.name

class Kontakty(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='kontakty/')
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.name

class Otzyvy(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='otzyvy/')
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.name


