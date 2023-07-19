from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *
# Register your models here.

@admin.register(Elevator)

class Elevator(admin.ModelAdmin):
    list_display = ('id','name','current_floor','max_floor','is_operational')

@admin.register(ElevatorRequest)

class ElevatorRequest(admin.ModelAdmin):
    list_display = ('id','request_floor','request_time','elevator')
