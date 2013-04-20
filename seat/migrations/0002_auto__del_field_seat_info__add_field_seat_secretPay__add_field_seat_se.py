# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Seat.info'
        db.delete_column('seat_seat', 'info')

        # Adding field 'Seat.secretPay'
        db.add_column('seat_seat', 'secretPay',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Seat.secretTag'
        db.add_column('seat_seat', 'secretTag',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=140),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Seat.info'
        db.add_column('seat_seat', 'info',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=140),
                      keep_default=False)

        # Deleting field 'Seat.secretPay'
        db.delete_column('seat_seat', 'secretPay')

        # Deleting field 'Seat.secretTag'
        db.delete_column('seat_seat', 'secretTag')


    models = {
        'seat.seat': {
            'Meta': {'object_name': 'Seat'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'secretPay': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'secretTag': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seats'", 'to': "orm['seat.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'})
        },
        'seat.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['seat']