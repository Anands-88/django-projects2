from django.contrib import admin
from .models import *

admin.site.register(Parent)
admin.site.register(Contribution) # registering the models in admin panel
