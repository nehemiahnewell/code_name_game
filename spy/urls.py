from django.conf.urls import url
from .views import spy_page

urlpatterns = [
    url(r'^$', spy_page),
]
