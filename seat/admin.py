# -*- coding: utf-8 -*-

from django.contrib import admin
from seat.models import *


# Admin Classes

class SeatAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description', 'type', 'status', 'duration', 'pay', 'tag')
	list_filter = ('tag', 'status', )
	
class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')


# Registration

admin.site.register(Seat, SeatAdmin)
admin.site.register(Tag, TagAdmin)
