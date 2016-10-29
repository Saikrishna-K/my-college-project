from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from models import *


@method_decorator(login_required,name='dispatch')
class CreateProviderForm(CreateView):
    model=Provider
    fields=['provider']
    success_url = '/csrs/list_service/'

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super(CreateProviderForm, self).form_valid(form)

    def get_queryset(self):
        queryset = CreateProviderForm.objects.filter(owner_id=self.request.user)
        return queryset


@method_decorator(login_required,name='dispatch')
class CreateServiceForm(CreateView):
    model=Service
    fields=['type','name','description']
    success_url='/csrs/list_service/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateServiceForm, self).form_valid(form)


@method_decorator(login_required,name='dispatch')
class CreateFeature(CreateView):
    model=Feature
    fields=['feature']
    success_url='/csrs/list_service/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateFeature, self).form_valid(form)


@method_decorator(login_required,name='dispatch')
class CreateProviderService(CreateView):
    model=ProviderService
    fields=['provider','service']
    success_url='/csrs/list_service/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateProviderService, self).form_valid(form)


@method_decorator(login_required,name='dispatch')
class CreateServiceFeature(CreateView):
    model=ServiceFeature
    fields=['service','feature']
    success_url='/csrs/list_service/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateServiceFeature, self).form_valid(form)


@method_decorator(login_required,name='dispatch')
class CreateBenchMarkValues(CreateView):
    model = BenchMark
    fields=['provider','service','feature','thirdparty_rating']
    success_url='/csrs/list_service/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateBenchMarkValues, self).form_valid(form)


@method_decorator(login_required,name='dispatch')
class CreateUserValues(CreateView):
    model = UserFeedback
    fields=['provider','service','feature','user_rating']
    success_url='/csrs/user_feedback/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateUserValues, self).form_valid(form)


@method_decorator(login_required,name='dispatch')
class CreateListView(ListView):
    model = Provider
    template_name = 'csrs/list_service_providers.html'

    def get_queryset(self):
        queryset = Provider.objects.filter(owner_id=self.request.user).values('provider')
        return queryset

@login_required
def providersView(request):
    queryset = Provider.objects.values('id','provider')
    return render_to_response("listview.html", {'index': queryset})


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login')

