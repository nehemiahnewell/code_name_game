from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'code_name.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^spy/', include('spy.urls')),

    # new url patterns should be coded above
    url(r'^', include('game.urls')),
]
