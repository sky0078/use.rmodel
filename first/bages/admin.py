from django.contrib import admin
from .models import User , Message, Write_msg

# Register your models here.

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Write_msg)