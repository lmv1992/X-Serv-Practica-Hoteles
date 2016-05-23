from django.contrib import admin

# Register your models here.
from models import PaginaUsuario
from models import Hotel
from models import HotelesUsuario
from models import Imagen
from models import Comentario
# Register your models here.
admin.site.register(Hotel)
admin.site.register(PaginaUsuario)
admin.site.register(HotelesUsuario)
admin.site.register(Imagen)
admin.site.register(Comentario)
