from django.contrib import admin
from .models import Image, BdayComment, UserComments
# Register your models here.

admin.site.register(Image)
admin.site.register(BdayComment)
admin.site.register(UserComments)
