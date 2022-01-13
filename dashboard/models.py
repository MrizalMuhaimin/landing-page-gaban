from django.db import models

# Create your models here.

class InfoUser(models.Model):
    nama = models.CharField(max_length=255)
    prov = models.CharField(max_length=255)
    kab = models.CharField(max_length=255)
    kec = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    alamat = models.TextField()
    almamater = models.CharField(max_length=255)
    jurusan = models.CharField(max_length=255)
    angkatan = models.CharField(max_length=4)
    email = models.EmailField(max_length=255)
    nomerTel = models.CharField(max_length=100)
    idline = models.CharField(max_length=255)
    inKerja = models.CharField(max_length=255)
    sektorKerja = models.CharField(max_length=255)
    sektorUsaha = models.CharField(max_length=255)
    LIST_CATEGORY = (
		('False', 'false'),
		('True', 'true'),
		)
    isTelponSms = models.CharField(
		max_length=100,
		choices = LIST_CATEGORY,
		default = 'False',
		)

    isWa = models.CharField(
		max_length=100,
		choices = LIST_CATEGORY,
		default = 'False',
		)

    isEmail = models.CharField(
		max_length=100,
		choices = LIST_CATEGORY,
		default = 'False',
		)

    isLine = models.CharField(
		max_length=100,
		choices = LIST_CATEGORY,
		default = 'False',
		)

    def __str__(self):
        return "{}.{}".format(self.id,self.nama)


class Kampus(models.Model):
  nama = models.CharField(max_length=255)

  def __str__(self):
        return "{}.{}".format(self.id,self.nama)


class Jurusan(models.Model):
  kampus = models.ForeignKey(Kampus,on_delete= models.CASCADE)
  jurusan = models.CharField(max_length=255)

  def __str__(self):
        return "{}.{}".format(self.id,self.jurusan)



