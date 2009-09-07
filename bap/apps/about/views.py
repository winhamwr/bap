from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from django.conf import settings

def members(request, template_name="about/members.html", extra_context=None):
    if extra_context is None:
        extra_context = {}
    members_group = Group.objects.get(name=settings.BAP_MEMBERS_GROUP_NAME)
    faculty_group = Group.objects.get(name=settings.BAP_FACULTY_GROUP_NAME)

    members = User.objects.filter(groups=members_group).order_by('last_name')
    faculty = User.objects.filter(groups=faculty_group).order_by('last_name')

    return render_to_response(template_name, dict({
        'member_list': members,
        'faculty_list': faculty,
    }, **extra_context), context_instance=RequestContext(request))

