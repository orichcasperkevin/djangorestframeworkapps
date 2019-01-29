from django.contrib import admin

# Register the models to the admin .. before we make a UI this is how we make changes to the database
from .models import *

admin.site.register(Task)
admin.site.register(SubTask)
