# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from seat.models import *

def index(request):
	seats = Seat.objects.exclude(status = Seat.statusEnd)
	tags = Tag.objects.all()
	done = Seat.objects.filter(status = Seat.statusEnd)
	pay = 0
	for seat in done:
		pay += seat.secretPay
	payString = ""
	while pay != 0:
		payString = str(pay % 1000) + payString
		pay /= 1000
		if pay != 0: payString = "," + payString
	info = {}
	info['count'] = len(done)
	info['pay'] = payString
	return render_to_response('index.html', {'seats': seats, 'tags': tags, 'info': info})
	
def about(request):
	return render_to_response('about.html', {})
	
def seat(request, id):
	seat = Seat.objects.get(id = id)
	if seat.status == Seat.statusEnd:
		return render_to_response('end.html', {})
	return render_to_response('seat.html', {'seat': seat})