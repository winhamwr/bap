from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from account.openid_consumer import PinaxConsumer
from pages.models import Page


if settings.ACCOUNT_OPEN_SIGNUP:
    signup_view = "account.views.signup"
else:
    signup_view = "signup_codes.views.signup"

try:
    root_page = Page.objects.root()[0]
except IndexError:
    root_page = None

urlpatterns = patterns('',
    # Using context requirements from pages.views.details so that we can use the pages templatetags
    url(r'^$', direct_to_template, {
        "template": "homepage.html",
        'extra_context': {
            'current_page': root_page,
            'lang': 'en',
            'path': None,
            'pages': Page.objects.navigation().order_by("tree_id"),
        },
    }, name="home"),

    url(r'^admin/invite_user/$', 'signup_codes.views.admin_invite_user', name="admin_invite_user"),
    url(r'^account/signup/$', signup_view, name="acct_signup"),

    (r'^about/', include('about.urls')),
    (r'^account/', include('account.urls')),
    (r'^openid/(.*)', PinaxConsumer()),
    (r'^profiles/', include('basic_profiles.urls')),
    (r'^notices/', include('notification.urls')),
    (r'^announcements/', include('announcements.urls')),

    (r'^admin/', include(admin.site.urls)),

    # BAP additions
    (r'^cas/', include('cas_consumer.urls')),

    # For django-page-cms
    (r'^p/', include('pages.urls')),

    (r'^schedule/', include('schedule.urls')),
    (r'^attendance/', include('django_attendance.urls')),
    (r'^reservations/', include('django_reservations.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site_media/', 'staticfiles.urls')
    )
