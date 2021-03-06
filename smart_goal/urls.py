from django.conf.urls import url
from django.contrib import admin
from mainapp.views import *
from userManagmentApp.views import *
from adminApp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^index', index),
    url(r'^registration', registration)
]

urlpatterns += [
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
    url(r'^user/registration/$', registration),
    url(r'^admin_page/$', admin_page),
    url(r'^dashboard/$', task),
    url(r'^overview/$', overview),
    url(r'^create/$', create),
    url(r'^settings/$', setting),
    url(r'^team_work/$', team_work),
    url(r'^admin_page/delete/user/(\d+)$', delete_user),
    url(r'^admin_page/get_user_form/(\d+)$', get_user_form),
    url(r'^admin_page/create/user/(\d*)$', create_user),
    url(r'^([0-9]+)/$', detail, name='detail'),
    url(r'^subtask-([0-9]+)/$', subtask_detail, name='subtask_detail'),
    url(r'^filter/(\d+)/$', category),
    url(r'^category_filter', category_filter),
    url(r'^state_filter', state_filter),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
