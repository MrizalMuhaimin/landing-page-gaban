from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .models import InfoUser

from .forms import inputDataForm


from .dataWilayah import dataWilayah

def logoutUser(request):
    logout(request)
    return redirect('/login')


def dashboard(request):
    infouser= InfoUser.objects.all()

    context = {
       
        'count':int(len(infouser)),
        'findData': "",
        'spa':1,
        'maxdata':int(len(infouser)),
        'infoUser' : infouser,
        'allFormField':inputDataForm,
        'notif':"",
        
    }

    if request.method == "POST":
        try:
            
            nama_field = request.POST['nama_field'].title()
            prov_field = request.POST['prov_field']
            kab_field = request.POST['kab_field']
            kec_field = request.POST['kec_field'].title()
            des_field = request.POST['des_field'].title()
            alamat_field = request.POST['alamat_field']
            almamater_field = request.POST['almamater_field']
            jurusan_field = request.POST['jurusan_field']
            angkatan_field = request.POST['angkatan_field']
            email_field = request.POST['email_field'].lower()
            nomerTel_field = request.POST['nomerTel_field']
            idline_field = request.POST['idline_field']
            if(idline_field==""):
                idline_field = "----"
            inKerja_field = request.POST['inKerja_field']
            sektorKerja_field = request.POST['sektorKerja_field'].title()
            sektorUsaha_field = request.POST['sektorUsaha_field'].title()
        
            try:
                isTelponSms_field = request.POST['isTelponSms_field']
                isTelponSms_field = True
            except:
                isTelponSms_field = False

            try:
                isEmail_field = request.POST['isEmail_field']
                isEmail_field = True
            except:
                isEmail_field = False

            try:
                isWa_field = request.POST['isWa_field']
                isWa_field = True

            except:
                isWa_field = False

            try:
                isLine_field = request.POST['isLine_field']
                isLine_field = True
            except:
                isLine_field = False
           
            try:
                InfoUser.objects.create(
                    nama = nama_field,
                    prov = prov_field,
                    kab = kab_field,
                    kec = kec_field,
                    des = des_field,
                    alamat = alamat_field,
                    almamater = almamater_field,
                    jurusan = jurusan_field,
                    angkatan = angkatan_field,
                    email = email_field,
                    nomerTel =nomerTel_field,
                    idline = idline_field,
                    inKerja = inKerja_field,
                    sektorKerja = sektorKerja_field,
                    sektorUsaha = sektorUsaha_field,
                    isTelponSms = isTelponSms_field,
                    isWa = isWa_field,
                    isEmail = isEmail_field,
                    isLine = isLine_field,
                )
            finally:
                infouser= InfoUser.objects.all()

                context = {
                    'count':int(len(infouser)),
                    'findData': "",
                    'maxdata':int(len(infouser)),
                    'spa':int(request.POST['spa2']),
                    'infoUser' : infouser,
                    'allFormField':inputDataForm,
                    'notif':request.POST['notif'],
                }

        except:
            try:
                findData = str(request.POST['Search'])
                findData = findData.split("'")[0]
                nFind = 0
                for i in infouser.values():
                    for a in i.values():
                        data = str(a).lower()
                        cari = findData.lower()
                        if(cari in data):
                            nFind += 1
                            break

            

                context = {
                    
                    'count':int(request.POST['coutdata']),
                    'findData': request.POST['Search'],
                    'maxdata':nFind,
                    'spa':1,
                    'infoUser' : infouser,
                    'allFormField':inputDataForm,
                    'notif':"",
                    
                    }
            
            except:
                try:
                    findData = str(request.POST['Search'])
                    findData = findData.split("'")[0]
                    nFind = 0
                    for i in infouser.values():
                        for a in i.values():
                            data = str(a).lower()
                            cari = findData.lower()
                            if(cari in data):
                                nFind += 1
                                break

                    context = {
                        
                        'count':nFind,
                        'findData': request.POST['Search'],
                        'maxdata':nFind,
                        'spa':1,
                        'infoUser' : infouser,
                        'allFormField':inputDataForm,
                        'notif':"",
                        
                    }
                except:
                   
                    
                    context = {
                    
                        'count':int(len(infouser)),
                        'findData': "",
                        'maxdata':int(len(infouser)),
                        'spa':int(request.POST['spa']),
                        'infoUser' : infouser,
                        'allFormField':inputDataForm,
                        'notif':"",
                        
                        }

    if not request.user.is_authenticated:
        print("User is not logged in :(")
        return redirect('/login')

    request.session.set_expiry(900)
    login(request, request.user)

    # from .updateJurusan import updateJurusan, updateKampus
    # resetDataKampus = False

    # if(resetDataKampus):
    #     updateKampus()
    #     updateJurusan()
    #     print("update")

    return render(request,"dashboard.html",context)


