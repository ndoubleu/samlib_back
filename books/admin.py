from django.contrib import admin
from .models import *

admin.site.register(BooksModel)
admin.site.register(BookTypesModel)
admin.site.register(NewsModel)