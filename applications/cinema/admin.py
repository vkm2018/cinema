from django.contrib import admin

# Register your models here.
from applications.cinema.models import Category, Cinema, Preview, Favorite, Video


class PreviewInAdmin(admin.TabularInline):
    model = Preview
    fields = ['image']
    max_num = 1

# class VideoInAdmin(admin.TabularInline):
#     model = Video
#     fields = ['video']
#     max_num = 1



class CinemaAdmin(admin.ModelAdmin):
    inlines = [PreviewInAdmin]

class VideoAdmin(admin.ModelAdmin):
    pass
    # inlines = [VideoInAdmin]



admin.site.register(Category)
admin.site.register(Cinema,CinemaAdmin)
admin.site.register(Video)
# admin.site.register(Preview)
admin.site.register(Favorite)
admin.site.register(Preview)
