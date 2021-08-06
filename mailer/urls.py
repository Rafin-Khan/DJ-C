
from django.conf.urls import include, url
from django.views.decorators.cache import cache_page
from mailer.views import IndexView

app_name = 'mailer'

urlpatterns = [
    url(r'^$', cache_page(60*15)(IndexView.as_view()), name="index"),
]
