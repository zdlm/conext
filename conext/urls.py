from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from views import HomeView

from tastypie.api import Api
from qa.api import QAResource, AnswerResource

v1_api = Api(api_name='v1')
v1_api.register(QAResource())
v1_api.register(AnswerResource())


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^home/$', HomeView.as_view(), name='myHome'),
    url(r"^base/", TemplateView.as_view(template_name="base.html"), name="base"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^api/", include(v1_api.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
