from typing import ValuesView
from django import forms
from django.forms.widgets import Widget

from .dataWilayah import dataWilayah

from .models import Kampus, Jurusan

class inputDataForm(forms.Form):
    kampus = Kampus.objects.order_by('nama')
    jurusan = Jurusan.objects.all()
    idKampusAwal = str(kampus[0])[0]
    
    newlist = []
    for data in kampus.values("nama"):
        data = data["nama"]
        
        datalist = [data,data] 
        newlist.append(tuple(datalist))

    LIST_KAMPUS = tuple(newlist)

    newlist = []
    for data in jurusan.values("kampus","jurusan"):
        data2 = data["kampus"]
        
        if(data2 == 1):
            dataJurusan = data["jurusan"]
            datalist = [dataJurusan,dataJurusan] 
            newlist.append(tuple(datalist))

    LIST_JURUSAN = tuple(newlist)

    

    newlist = []
    for data in dataWilayah.keys():
        datalist = [data,data] 
        newlist.append(tuple(datalist))
    
    LIST_CATEGORY_PROV = tuple(newlist)

   
    nama_field = forms.CharField(
        widget=forms.TextInput(
        attrs={
          'placeholder':'Masukkan Nama Lengkap',
        }
      ),
      label="Nama Lengkap ")
  
    prov_field = forms.ChoiceField(
        choices= LIST_CATEGORY_PROV,
        label="Provinsi ",
    )

    LIST_CATEGORY = ()

    newlist = []
    for data in dataWilayah["Aceh"]:
        datalist = [data,data] 
        newlist.append(tuple(datalist))
    
    LIST_CATEGORY = tuple(newlist)
    

    
    kab_field = forms.ChoiceField(
        choices= LIST_CATEGORY,
        label=" Kabupaten/Kota ",
    )
    kec_field = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(
            attrs={
            'placeholder':'Masukkan Kecamatan',
            }
        ),
        label="Kecamatan ")

    des_field = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(
            attrs={
            'placeholder':'Masukkan Desa',
            }
        ),
        label="Desa/ Kelurahan ")

    alamat_field = forms.CharField(
        widget=forms.TextInput(
        attrs={
        'placeholder':'Nama Jalan/Perumahan nomer dan RT/RW',
        }
        ),
        label="Alamat Lengkap ")

    
    almamater_field = forms.ChoiceField(
        choices = LIST_KAMPUS,
        label="Almamater ")

    jurusan_field = forms.ChoiceField(
        choices = LIST_JURUSAN,
        label="Jurusan ")


    angkatan_field = forms.CharField(
        max_length=4, 
        min_length=4,
        widget=forms.TextInput(
        attrs={
          'placeholder':'Masukkan Angkatan',
          'type': 'number',
          'min':1914
            }
        ),
        label="Angkatan ")

    email_field = forms.EmailField( 
        widget=forms.EmailInput(
        attrs={
          'placeholder':'Masukkan Email',
            }
        ),
        label="Email")
    nomerTel_field = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(
        attrs={
            'placeholder':'Masukkan Nomor Telephone / WA',
            }
        ),
        label="Nomor Telephone / WA ")

    idline_field = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(
            attrs={
            'placeholder':'Masukkan ID Line',
            }
        ),
        label="ID Line ")
    inKerja_field = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(
            attrs={
            'placeholder':'Tempat Bekerja / Nama Kampus',
            }
        ),
        label="Nama institusi tempat bekerja ")
    sektorKerja_field = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(
            attrs={
            'placeholder':'Bidang Pekerjaan /  Mahaiswa',
            }
        ),
        label="Bidang Pekerjaan ")

    sektorUsaha_field = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(
            attrs={
            'placeholder':'Sektor Usaha /  Mahaiswa',
            }
        ),
        label="Sektor usaha ")

    isTelponSms_field = forms.BooleanField( 
        required=False,
       
      )

    isEmail_field = forms.BooleanField(
        required=False,
        
      )

    isWa_field = forms.BooleanField(
        required=False,
       
      )
    isLine_field = forms.BooleanField(
        required=False,
        
      )
