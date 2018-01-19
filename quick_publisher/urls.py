from django.conf.urls import include, url
from django.contrib import admin
from publish.views import view_post
from main.views import home, verify
urlpatterns = [
    # Examples:
    # url(r'^$', 'quick_publisher.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^verify/(?P<uuid>[a-z0-9\-]+)/', verify, name='verify'),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)', view_post, name='view_post'),
]
