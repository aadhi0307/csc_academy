from django.db import models

class CourseDetail(models.Model):
    C_name = models.CharField(max_length=100)  # Course name
    C_description = models.TextField()         # Course description
    C_syllabus = models.TextField()            # Course syllabus or topics covered
    C_price = models.DecimalField(max_digits=8, decimal_places=2)  # Course price
    C_image = models.ImageField(upload_to='course_images/')  # Course image upload

    def __str__(self):
        return self.C_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Affiliation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='affiliations_logos/')

    def __str__(self):
        return self.title
