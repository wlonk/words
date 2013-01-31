# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'words_language', (
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True)),
        ))
        db.send_create_signal(u'words', ['Language'])

        # Adding model 'Word'
        db.create_table(u'words_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['words.Language'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('profane', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'words', ['Word'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'words_language')

        # Deleting model 'Word'
        db.delete_table(u'words_word')


    models = {
        u'words.language': {
            'Meta': {'object_name': 'Language'},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True'})
        },
        u'words.word': {
            'Meta': {'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['words.Language']"}),
            'profane': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['words']