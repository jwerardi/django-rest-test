from django.conf.urls import url, include
from django.conf.urls import include

urlpatterns = [
    url(r'^', include('snippets.urls')),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]