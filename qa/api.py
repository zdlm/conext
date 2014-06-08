from tastypie.resources import ModelResource
from qa.models import QA

class QAResource(ModelResource):
    class Meta:
        queryset = QA.objects.all()
        resource_name = "qa"