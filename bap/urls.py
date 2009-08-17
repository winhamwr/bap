from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from account.openid_consumer import PinaxConsumer


if settings.ACCOUNT_OPEN_SIGNUP:
    signup_view = "account.views.signup"
else:
    signup_view = "signup_codes.views.signup"


urlpatterns = patterns('',
    #url(r'^$', direct_to_template, {
    #    "template": "homepage.html",
    #}, name="home"),

    url(r'^admin/invite_user/$', 'signup_codes.views.admin_invite_user', name="admin_invite_user"),
    url(r'^account/signup/$', signup_view, name="acct_signup"),

    (r'^about/', include('about.urls')),
    (r'^account/', include('account.urls')),
    (r'^openid/(.*)', PinaxConsumer()),
    (r'^profiles/', include('basic_profiles.urls')),
    (r'^notices/', include('notification.urls')),
    (r'^announcements/', include('announcements.urls')),

    (r'^admin/(.*)', admin.site.root),

    # BAP additions
    (r'^cas/', include('cas_consumer.urls')),

    # For django-page-cms
    url(r'^$', 'pages.views.details', name='pages-root'),
    url(r'^p/(?P<path>.*)$', 'pages.views.details', name='pages-details-by-path'),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'staticfiles.views.serve')
    )
