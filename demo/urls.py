from django.conf.urls import url
from demo import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^captioning', views.captioning, name='captioning'),
    url(r'^upload/using_image_url/$', views.upload_image_using_url, name='upload-url'),
    url(r'^upload/$', views.file_upload, name='upload'),
]
