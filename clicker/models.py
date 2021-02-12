from django.db import models

# Create your models here.
class Clicks(models.Model):
  clicked = models.IntegerField(default=0)

  def __str__(self):
    return f"Id = {self.id}, Clicked= {self.clicked}"
