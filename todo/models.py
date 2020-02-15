from django.db import models

# Create your models here.
PRIORITY = (("light","danger!"),("light","Normal"),("light","Low"))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = PRIORITY
        )
    duedate = models.DateField()
    place = models.CharField(max_length=50)


    def __str__(self):
        return self.title