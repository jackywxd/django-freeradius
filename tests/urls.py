from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from openwisp_utils.admin_theme.admin import admin, openwisp_admin

openwisp_admin()
admin.autodiscover()

urlpatterns = [
    url(r'^', include('django_freeradius.urls', namespace='freeradius')),
    url(r'^admin/', admin.site.urls),
    # django_freeradius urls
    # keep the namespace argument unchanged
]

urlpatterns += staticfiles_urlpatterns()
