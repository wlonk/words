# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'wordlist_language', (
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True)),
        ))
        db.send_create_signal(u'wordlist', ['Language'])

        # Adding model 'Word'
        db.create_table(u'wordlist_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wordlist.Language'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('profane', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'wordlist', ['Word'])

        # Adding unique constraint on 'Word', fields ['language', 'value']
        db.create_unique(u'wordlist_word', ['language_id', 'value'])


    def backwards(self, orm):
        # Removing unique constraint on 'Word', fields ['language', 'value']
        db.delete_unique(u'wordlist_word', ['language_id', 'value'])

        # Deleting model 'Language'
        db.delete_table(u'wordlist_language')

        # Deleting model 'Word'
        db.delete_table(u'wordlist_word')


    models = {
        u'wordlist.language': {
            'Meta': {'ordering': "('iso',)", 'object_name': 'Language'},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True'})
        },
        u'wordlist.word': {
            'Meta': {'ordering': "('language', 'value')", 'unique_together': "(('language', 'value'),)", 'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wordlist.Language']"}),
            'profane': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['wordlist']