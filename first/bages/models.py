from django.db import models
 
# Create your models here.

""""
Create user model ( see how to extend user model - 3 ways ) find the best to our case.
Create message model

Find the relation between the 2 models ( user, message)
Add models to admin site
"""


# Create message model
class Message(models.Model):
    msg = models.TextField()
    
    def __str__(self):
        return self.msg

# Create user model
class User(models.Model):
    name = models.CharField(max_length=25 , null = True)
    active = models.BooleanField(default= False)
    date = models.DateTimeField(null = True)

    sms = models.ForeignKey(Message,on_delete = models.CASCADE)
    def __str__(self):

        return self.name