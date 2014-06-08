from django.conf.urls import patterns, include, url
from api import QAResource

qa_resource = QAResource()


urlpatterns = patterns("",
    url(r"^api/", include(qa_resource.urls)),
)

