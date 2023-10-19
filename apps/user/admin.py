from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from . import models

@admin.register(models.UserAccount)
class PostAdmin(ImportExportModelAdmin):
    list_display = ('account', 'username', 'verificated', 'is_staff')
    search_fields = ('account', 'username', )
