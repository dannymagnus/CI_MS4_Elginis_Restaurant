from django.contrib import admin
from .models import About, Reason, Chef, Comment

# Register your models here.
admin.site.register(About)
admin.site.register(Reason)
admin.site.register(Chef)
admin.site.register(Comment)