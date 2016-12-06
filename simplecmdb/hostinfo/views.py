from django.shortcuts import render
from django.http import HttpResponse
from hostinfo.models import Host, HostGroup
import pickle
import json
# Create your views here.

def collect(req):
    if req.POST:
        # obj = pickle.loads(req.body)
        obj = json.loads(req.body)
        hostname = obj['hostname']
        ip = obj['ip']
        cpu_model = obj['cpu_model']
        cpu_num = obj['cpu_num']
        memory = obj['memory']
        osver = obj['osver']
        vendor = obj['vendor']
        product = obj['product']
        sn = obj['sn']
        try:
            host = Host.objects.get(sn=sn)
        except:
            host = Host()
        host.hostname = hostname
        host.ip = ip
        host.cpu_model = cpu_model
        host.cpu_num = cpu_num
        host.memory = memory
        host.osver = osver
        host.vendor = vendor
        host.product = product
        host.sn = sn
        host.save()
        return HttpResponse('OK')
    else:
        return HttpResponse('not data')

def getjson(req):
    ret_list = []
    hg = HostGroup.objects.all()
    for g in hg:
        ret = {'groupname': g.groupname, 'members': []}
        for h in g.member.all():
            ret_h = {'hostname': h.hostname, 'ip': h.ip}
            ret['members'].append(ret_h)
        ret_list.append(ret)
    return HttpResponse(json.dumps(ret_list))