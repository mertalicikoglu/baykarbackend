# myproject/app/admin.py

from django.contrib import admin
from .models import Team, Personnel, Part, Aircraft

# Modellerin Yönetim Paneline Kayıt Edilmesi
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team')
    search_fields = ('name', 'team__name')
    list_filter = ('team',)

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'aircraft_type', 'team', 'status')
    search_fields = ('type', 'aircraft_type', 'team__name')
    list_filter = ('type', 'aircraft_type', 'team')

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'assembled')
    search_fields = ('type',)
    list_filter = ('type', 'assembled')
