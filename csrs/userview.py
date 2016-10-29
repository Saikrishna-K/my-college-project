from django import forms
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from pip._vendor.requests.packages.urllib3 import request
from rest_framework.compat import template_render

from models import *


class CreateServiceView(ListView):
    model = Service
    queryset = Service.objects.values('type','name','description').order_by('name')
    template_name = 'user/user.html'


def displayFeatures(request,name):
    result = ServiceFeature.objects.filter(service__name__exact=name).values('feature__id','feature__feature')
    return render_to_response("user/selectfeatures.html", {'result': result, 'name': name})


def p_cal(user_values, count):

    all_rating=[]
    dup=[]
    providers_count= len(user_values)
    for i in range(0,count):
        values=([x[i] for x in user_values])
        values=dict(zip(range(1,providers_count+1),values))
        dup = values.values()
        dup.sort(reverse=True)
        key = []
        for j in range(0,providers_count):
            index = values.keys()[values.values().index(dup[j])]
            values.__setitem__(index,j+1)

        all_rating.append(values.values())
    value=[]
    for i in range(0, providers_count):
            value.append(sum([x[i] for x in all_rating]))
    values2 = dict(zip(range(0,providers_count),value))
    value.sort()
    key = []
    for j in range(0, providers_count):
        index=values2.keys()[values2.values().index(value[j])]
        key.append(index+1)
        values2.__delitem__(index)

    return key


def display_services(request, service):
    result = request.GET.getlist('check')
    try:
        provider=[]
        providers = ProviderService.objects.filter(service_id__name=service).values('provider').distinct()

        for i in range(0,len(providers)):
            provider.append(providers[i]['provider'])
        rating = []

        for j in range(0, len(providers)):
            benchMark = []
            for i in range(0, len(result)):
                benchMark.append(BenchMark.objects.filter(provider_id=provider[j],service_id__name=service,feature=result[i]).values('thirdparty_rating')[0]['thirdparty_rating'])
            rating.append(benchMark)
        user_count, user_values = [], []
        for j in range(0, len(providers)):
            provider_user=[]
            values2 = []

            for i in range(0, len(result)):
                provider_user=UserFeedback.objects.filter(provider_id=provider[j],service_id__name=service,feature=result[i]).values('user_rating')
                values1 = []
                for k in range(0, len(provider_user)):
                    values1.append(provider_user[k]['user_rating'])
                values2.append(sum(values1)/(k+1))
            user_values.append(values2)
            user_count.append(k+1)
        priority = p_cal(user_values,len(result))
        result = []
        for x in priority:
            result.append(Provider.objects.filter(id=x).values('provider')[0])

    except IndexError:
        return render_to_response('user/noEnoughData.html')

    success_url = 'user/ranking.html'
    return render_to_response('user/ranking.html', {'result':result})
