# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QA'
        db.create_table(u'qa_qa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('categary', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('at_who', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')()),
            ('answer_count', self.gf('django.db.models.fields.IntegerField')()),
            ('like_count', self.gf('django.db.models.fields.IntegerField')()),
            ('dislike_count', self.gf('django.db.models.fields.IntegerField')()),
            ('keep_count', self.gf('django.db.models.fields.IntegerField')()),
            ('delete_count', self.gf('django.db.models.fields.IntegerField')()),
            ('stars', self.gf('django.db.models.fields.IntegerField')()),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_duplicate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('duplicate_ids', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('updated_by', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'qa', ['QA'])


    def backwards(self, orm):
        # Deleting model 'QA'
        db.delete_table(u'qa_qa')


    models = {
        u'qa.qa': {
            'Meta': {'object_name': 'QA'},
            'answer_count': ('django.db.models.fields.IntegerField', [], {}),
            'at_who': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'categary': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delete_count': ('django.db.models.fields.IntegerField', [], {}),
            'dislike_count': ('django.db.models.fields.IntegerField', [], {}),
            'duplicate_ids': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_duplicate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keep_count': ('django.db.models.fields.IntegerField', [], {}),
            'like_count': ('django.db.models.fields.IntegerField', [], {}),
            'stars': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_by': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['qa']