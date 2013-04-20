# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Seat'
        db.create_table('seat_seat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('pay', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seats', to=orm['seat.Tag'])),
        ))
        db.send_create_signal('seat', ['Seat'])

        # Adding model 'Tag'
        db.create_table('seat_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('seat', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Seat'
        db.delete_table('seat_seat')

        # Deleting model 'Tag'
        db.delete_table('seat_tag')


    models = {
        'seat.seat': {
            'Meta': {'object_name': 'Seat'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'pay': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
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