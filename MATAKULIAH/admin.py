from django.contrib import admin
from MATAKULIAH.models import Matakuliah

# Register your models here.

class MatakuliahAdmin(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'dosen', 'sks']
    search_fields = ['kode', 'nama']

admin.site.register(Matakuliah, MatakuliahAdmin)