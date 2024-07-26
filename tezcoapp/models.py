from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/project')
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/service')
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    options = (
        ("unread", "unread"),
        ("viewed", "viewed")
    )
    status = models.CharField(max_length=15, choices=options, default="unread")

    def __str__(self):
        return self.name

class Subscription(models.Model):
    email = models.EmailField(null=True)

class Enquiry(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    options = (
        ("unread", "unread"),
        ("viewed", "viewed")
    )
    status = models.CharField(max_length=15, choices=options, default="unread")

    def __str__(self):
        return self.name  # Adjust based on what identifies the enquiry

class Blog(models.Model):
    image = models.ImageField(upload_to='gallery/blog')
    images = models.ImageField(upload_to='gallery/blog', null=True)
    blogersphoto = models.ImageField(upload_to='gallery/bloguser')
    description = models.CharField(max_length=200)
    details = models.TextField()
    detailsof = models.TextField()
    name = models.CharField(max_length=20)
    caption = models.CharField(max_length=100)
    industry = models.CharField(max_length=50)
    blogersquote = models.TextField()

    def __str__(self):
        return self.name

class Testimo(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='gallery/testimonials', null=True)
    job = models.CharField(max_length=20)
    testimonial = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    caption = models.CharField(max_length=50)
    description = models.CharField(max_length=40)
    images = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.caption
