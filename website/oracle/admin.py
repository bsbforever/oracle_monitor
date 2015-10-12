from django.contrib import admin
from oracle.models import oraclelist
from oracle.models import oracledglist
from oracle.models import Blog
from oracle.models import alertevent
from oracle.models import oraclestatus
from oracle.models import Mssqllist
from oracle.models import linuxlist
from oracle.models import topsql

admin.site.register(oraclelist)
admin.site.register(oracledglist)
admin.site.register(Blog)
admin.site.register(alertevent)
admin.site.register(oraclestatus)
admin.site.register(Mssqllist)
admin.site.register(linuxlist)
admin.site.register(topsql)
# Register your models here.
