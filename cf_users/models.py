from django.db import models

class CFUser(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  user_email = models.CharField(max_length=200)
  def __str__(self):
    return "%s %s" % (self.first_name, self.last_name)


