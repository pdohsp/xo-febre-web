from django.contrib import admin
from .models import (
    Pessoa,
    Consulta
)    
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Consulta)