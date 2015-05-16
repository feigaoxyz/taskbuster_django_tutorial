from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from .views import home, home_files


urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'taskbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    '',
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name="home-files"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'accounts/', include('allauth.urls')),
    url(r'i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
)
