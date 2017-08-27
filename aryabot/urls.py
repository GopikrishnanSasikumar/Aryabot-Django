from django.conf.urls import include, url
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from aryabot.views import ChatterBotAppView


urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
]
