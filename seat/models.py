# -*- coding: utf-8 -*-

from django.db import models



# Seat

class Seat(models.Model):
	
	# Type Choice
	typeRecruit 	= 1
	typeOutSourcing = 2
	SeatType 		= (
		(typeRecruit, "채용"),
		(typeOutSourcing, "외주"),
	)
		
	# Status Choice
	statusNotReady 	= 1
	statusReady 	= 2
	statusSitting 	= 3
	statusDone 		= 4
	statusEnd		= 5
	SeatStatus 		= (
		(statusNotReady, "기획단계"),
		(statusReady, "공석"),
		(statusSitting, "착석중"),
		(statusDone, "수주완료"),
		(statusEnd, "안보이게하기"),
	)
	
	# Fields
	type 		= models.PositiveSmallIntegerField(choices = SeatType, default = typeOutSourcing)
	status	 	= models.PositiveSmallIntegerField(choices = SeatStatus, default = statusNotReady)
	secretPay	= models.IntegerField(default = 0)
	title 		= models.CharField(max_length = 40)
	description = models.CharField(max_length = 140)
	duration	= models.CharField(max_length = 40)
	pay 		= models.CharField(max_length = 40)
	secretTag	= models.CharField(max_length = 140)
	tag 		= models.ForeignKey('Tag', related_name = 'seats')
	
	# Functions
	def __unicode__(self):
		return "[%d] %s" % (self.id, self.title)
		

# Tag

class Tag(models.Model):
	title		= models.CharField(max_length = 40)
	def __unicode__(self):
		return "%s" % self.title
