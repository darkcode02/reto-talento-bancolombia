from django.contrib import admin
from .models import Guion

# Register your models here.
class GuionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(Guion, GuionAdmin)
