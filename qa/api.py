from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication
from qa.models import QA

class QAResource(ModelResource):
    class Meta:
        queryset = QA.objects.all()
        resource_name = "qa"
        filtering = {}

class AnswerResource(ModelResource):
    class Meta:
        queryset = QA.objects.all()
        resource_name = "answer"
        filtering = {

        }
        authentication = BasicAuthentication()

    def get_object_list(self, request):
        return super(AnswerResource, self).get_object_list(request).filter(type="answer")

class QuestionResource(ModelResource):
    class Meta:
        print("*****************************")
        queryset = QA.objects.all()
        resource_name = "question"
        filtering = {
            "content":ALL,
        }
        ordering = [
            "date_updated",
        ]
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()

    def get_object_list(self, request):
        return super(QuestionResource, self).get_object_list(request).filter(type="question")
