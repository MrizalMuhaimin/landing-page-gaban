from django.contrib import admin

# Register your models here.

from .models import InfoUser
from .models import Kampus
from .models import Jurusan
admin.site.register(InfoUser)
admin.site.register(Kampus)
admin.site.register(Jurusan)