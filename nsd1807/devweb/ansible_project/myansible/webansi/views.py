from django.shortcuts import render
from .models import HostGroup

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def addhosts(request):
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        group = request.POST.get('group')
        if group:
            # get_or_create返回元组(实例, 0/1)
            hostgroup = HostGroup.objects.get_or_create(groupname=group)[0]
            if hostname and ip:
                hostgroup.host_set.get_or_create(hostname=hostname, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})
