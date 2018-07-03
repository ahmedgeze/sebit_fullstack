from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r"get/$",views.get,name='get'),
    url(r"put/$",views.put,name='get'),
    url(r"post/$",views.post,name='get'),
    url(r'^put/(?P<id>\w{0,50})/(?P<name>\w{0,50})/(?P<city>\w{0,50})/(?P<country>\w{0,50})$',views.put,name='post'),
]
