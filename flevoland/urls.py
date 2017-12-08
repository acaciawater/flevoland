from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.decorators.cache import cache_page

from .views import HomeView, LocationView, FirstDetailView, SecondDetailView, history_JS, info
from acacia.data.views import DashGroupView

admin.autodiscover()

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/', include('acacia.data.urls',namespace='acacia')),
    url(r'^detail1/(?P<pk>[0-9]+)/$', FirstDetailView.as_view(), name='detail1'),
    url(r'^detail2/(?P<pk>[0-9]+)/$', SecondDetailView.as_view(), name='detail2'),
    url(r'^(?P<pk>[0-9]+)/$', cache_page(60*15)(LocationView.as_view()), name='location'),
    url(r'^history/(?P<pk>[0-9]+)/$', history_JS, name='history'),
    url(r'^info$', info, name='info')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.IMG_URL, document_root=settings.IMG_ROOT)

from django.contrib.auth import views as auth_views
urlpatterns += [
    url(r'^password/change/$',
                    auth_views.password_change,
                    name='password_change'),
    url(r'^password/change/done/$',
                    auth_views.password_change_done,
                    name='password_change_done'),
    url(r'^password/reset/$',
                    auth_views.password_reset,
                    name='password_reset'),
    url(r'^accounts/password/reset/done/$',
                    auth_views.password_reset_done,
                    name='password_reset_done'),
    url(r'^password/reset/complete/$',
                    auth_views.password_reset_complete,
                    name='password_reset_complete'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                    auth_views.password_reset_confirm,
                    name='password_reset_confirm'),
    url(r'^accounts/', include('registration.backends.default.urls'))    
]
