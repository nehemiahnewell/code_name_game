from django.conf.urls import url
import game.views
import spymaster.views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^$', game.views.start_index_page),
    url(r'^select/', game.views.select_player, name='select_player'),
    url(r'^spymaster/', spymaster.views.spymaster_page, name='spymaster'),
]
