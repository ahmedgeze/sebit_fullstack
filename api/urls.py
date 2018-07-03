from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    # url(r"get/$",views.getAll,name='get'),
    # url(r"put/$",views.put,name='get'),
    # url(r"post/$",views.post,name='get'),
    # url(r'^put/(?P<id>\w{0,50})/(?P<name>\w{0,50})/(?P<city>\w{0,50})/(?P<country>\w{0,50})$',views.put,name='post'),

    url(r'clearDB/$',views.clearDB,name='get'),
    url(r'getAll/$',views.getAll,name='get'),
    url(r'addNew/$',views.addNew,name='get'),
    url(r'queryData/$',views.queryData,name='get'),


]
