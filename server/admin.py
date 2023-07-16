from django.contrib import admin
from .models import Files
# Register your models here.


admin.site.site_header = "FileServer Admin Dashboard"
admin.site.index_title = "FileServer"
admin.site.site_title = "FileServer"


admin.site.register(Files)
# admin.site.register(FileActivity)
