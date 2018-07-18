from django.conf.urls import url

from .views import CookieView

urlpatterns = [
    url(r'^cookies/$', CookieView.as_view(), name='cookie'),
]
