from django.conf.urls import url
# Notice we added include

from . import views

urlpatterns = [
    url(r'^$', views.index), # And now we use the include function to pull in our first_app.urls...
    
    url(r'^display/$', views.display), # And now we use the include function to pull in our first_app.urls...
    
    url(r'^new/$', views.new),

    url(r'^create/$', views.create),

    url(r'^new/$', views.new),
    
    url(r'^(?P<number>\d+)$', views.show),

    url(r'^(?P<number>\d+)/edit$', views.edit),

    url(r'^(?P<number>\d+)/delete$', views.destroy)
    ]

