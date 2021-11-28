from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create user model ( see how to extend user model - 3 ways ) find the best to our case.
# Create message model

# Find the relation between the 2 models ( user, message)
# Add models to admin site


 

# Create message model
       
    

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msgs = models.TextField(blank=True)
    def __str__(self):
        return self.msg
    

@receiver(post_save, sender=User)
def create_user_Messages(sender, instance, created, **kwargs):
    if created:
        Messages.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_Messages(sender, instance, **kwargs):
    instance.messages.save()
 

    
    class Meta:
        ordering = ['name']

class Write_msg(models.Model):
    urname = models.CharField(max_length = 50 , null = True)
    urmsg = models.TextField(null = True)
    

