from django.contrib import admin
from .models import User, Projekt
from admin_confirm import AdminConfirmMixin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.

# class ArchitektAdmin(AdminConfirmMixin, admin.ModelAdmin):
# 	fieldsets = [
# 		('Dane podstawowe',	{'fields': ['imie', 'nazwisko', 'data_ur',]}),
# 	]
# 	confirm_add = True
# 	confirmation_fields = ['imie', 'nazwisko', 'projekty',]
# 	list_display = ('username', 'imie', 'nazwisko', 'projekty')
# 	class Meta:
# 		model = get_user_model()

# class MyModelAdmin(AdminConfirmMixin, ModelAdmin):
#     confirm_add = True
#     confirmation_fields = ['field1', 'field2']

class ProjektAdmin(AdminConfirmMixin, admin.ModelAdmin):
	fieldsets = [
		('Dane podstawowe',	{'fields': ['nazwa', 'rok_powstania', 'architekt', 'grafika']}),
	]
	list_display = ('nazwa', 'rok_powstania', 'architekt')

UserAdmin.list_display = ('username', 'imie', 'nazwisko', 'email', 'projekty')

admin.site.register(User, UserAdmin)
admin.site.register(Projekt, ProjektAdmin)

