from re import I
from .models import InfoUser, Jurusan, Kampus
from .serializers import InfoUserSerializer, InfoJurusanSerializer, InfoKampusSerializer
from rest_framework import serializers, viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class jurusanView(viewsets.ModelViewSet):
    queryset = Jurusan.objects.all()
    serializer_class = InfoJurusanSerializer
    permission_classes =[permissions.IsAuthenticated]

class kampusView(viewsets.ModelViewSet):
    queryset = Kampus.objects.all()
    serializer_class = InfoKampusSerializer
    permission_classes =[permissions.IsAuthenticated]

class userViewSetUser(viewsets.ModelViewSet):
    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        info = InfoUser.objects.all()
        return info

    def get(self,request, *args, **kwargs):
        try:
             id = request.query_params["id"]
             if id != None:
                info = InfoUser.objects.get(id=id)
                serializer = InfoUserSerializer(info)
        except:
            info = self.get_queryset()
            serializer = InfoUserSerializer(info, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        info_data = request.data
        new_info = InfoUser.objects.create(
            nama = info_data["nama"],
            prov = info_data["prov"],
            kab = info_data["kab"],
            kec = info_data["kec"],
            des = info_data["des"],
            alamat = info_data["alamat"],
            almamater = info_data["almamater"],
            jurusan = info_data["jurusan"],
            angkatan = info_data["angkatan"],
            email = info_data["email"],
            nomerTel = info_data["nomerTel"],
            idline = info_data["idline"],
            inKerja = info_data["inKerja"],
            sektorKerja = info_data["sektorKerja"],
            sektorUsaha = info_data["sektorUsaha"],
            isTelponSms = info_data["isTelponSms"],
            isWa = info_data["isWa"],
            isEmail = info_data["isEmail"],
            isLine = info_data["isLine"],
        )

        new_info.save()
        serializer = InfoUserSerializer(new_info)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        info_object = InfoUser.objects.get(id=id)

        data = request.data

        info_object.nama = data["nama"]
        info_object.prov = data["prov"]
        info_object.kab = data["kab"]
        info_object.kec = data["kec"]
        info_object.des = data["des"]
        info_object.alamat = data["alamat"]
        info_object.almamater = data["almamater"]
        info_object.jurusan = data["jurusan"]
        info_object.angkatan = data["angkatan"]
        info_object.email = data["email"]
        info_object.nomerTel = data["nomerTel"]
        info_object.idline = data["idline"]
        info_object.inKerja = data["inKerja"]
        info_object.sektorKerja = data["sektorKerja"]
        info_object.sektorUsaha = data["sektorUsaha"]
        info_object.isTelponSms = data["isTelponSms"]
        info_object.isWa = data["isWa"]
        info_object.isEmail = data["isEmail"]
        info_object.isLine = data["isLine"]

        info_object.save()

        serializer = InfoUserSerializer(info_object)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        info_object = InfoUser.objects.get()
        data = request.data
        info_object.nama = data.get('nama', info_object.nama)
        info_object.prov = data.get('prov', info_object.prov)
        info_object.kab = data.get('kab', info_object.kab)
        info_object.kec = data.get('kec', info_object.kec)
        info_object.des = data.get('des', info_object.des)
        info_object.alamat = data.get('alamat', info_object.alamat)
        info_object.almamater = data.get('almamater', info_object.almamater)
        info_object.emaill = data.get('emaill', info_object.emaill)
        info_object.nomerTel = data.get('nomerTel', info_object.nomerTel)
        info_object.idline = data.get('idline', info_object.idline)
        info_object.inKerja = data.get('inKerja', info_object.inKerja)
        info_object.sektorKerja = data.get('sektorKerja', info_object.sektorKerja)
        info_object.sektorUsaha = data.get('sektorUsaha', info_object.sektorUsaha)
        info_object.isTelponSms = data.get('isTelponSms', info_object.isTelponSms)
        info_object.isWa = data.get('isWa', info_object.isWa)
        info_object.isEmail = data.get('isEmail', info_object.isEmail)
        info_object.isLine = data.get('isEmail', info_object.isLine)

        serializer = InfoUserSerializer(info_object)
        return Response(serializer.data)


       









    


