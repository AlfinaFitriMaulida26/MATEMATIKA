from django.db import models

# Create your models here.

class Matakuliah(models.Model):
    kode= models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    dosen = models.CharField(max_length=100)
    sks = models.CharField(max_length=50)

    def _str_(self):
        return "{}".format(self.nama)
