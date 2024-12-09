from django.db import models

class Ikan(models.Model):
	nama = models.CharField(max_length=50)
	gambar = models.CharField(max_length=500)
	harga = models.IntegerField()
	type = models.CharField(max_length=55,default='emas')

	def __str__(self):
		return f'{self.nama} {self.harga} {self.gambar}'
		
