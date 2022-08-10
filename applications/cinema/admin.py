from django.contrib import admin

# Register your models here.
from applications.cinema.models import Category, Cinema, Image

admin.site.register(Category)
admin.site.register(Cinema)
# admin.site.register(Preview)
#
#
class PreviewInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 1