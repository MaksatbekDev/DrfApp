from django.contrib import admin

# Register your models here.
from .models import Category,Branch,Contact,Course

admin.site.register(Category)
admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Course)