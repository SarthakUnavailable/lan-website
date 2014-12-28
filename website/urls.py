from django.conf.urls import patterns, include, url
from django.contrib import admin
from lan import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.register, name='index'),
    url(r'^submit',views.submit),
    url(r'^order',views.placeorder),
    url(r'^placeorder',views.placeorder),
)
