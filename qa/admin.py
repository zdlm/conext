from django.contrib import admin

from models import QA

class QAAdmin(admin.ModelAdmin):
    pass
admin.site.register(QA, QAAdmin)

