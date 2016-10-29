from django.conf.urls import url, include
from csrs import cloudview,userview


urlpatterns = [

    url(r'^create_provider/$', cloudview.CreateProviderForm.as_view(), name='create-provider'),
    url(r'^create_service/$', cloudview.CreateServiceForm.as_view(), name='create-service'),
    url(r'^create_feature/$', cloudview.CreateFeature.as_view(), name='create-feature'),
    url(r'^create_providerservice/$', cloudview.CreateProviderService.as_view(), name='provider-service'),
    url(r'^create_servicefeature/$', cloudview.CreateServiceFeature.as_view(), name='service-feature'),
    url(r'^benchmark/$', cloudview.CreateBenchMarkValues.as_view(), name='benchmark-value'),
    url(r'^user_feedback/$', cloudview.CreateUserValues.as_view(), name='user-value'),
    url(r'^logout/$',cloudview.logout_page,name='logout-view'),

    url(r'^list_providers/$', cloudview.CreateListView.as_view(), name='list-providers'),
    url(r'^list_service/$', cloudview.providersView, name='list-providers-benchmark'),
    url(r'^list_services/$', userview.CreateServiceView.as_view(), name='list-services'),
    url(r'^list_features/(?P<name>[\w|\W]+)', userview.displayFeatures, name='select-features'),
    url(r'^ranking/(?P<service>[\w|\W]+)/', userview.display_services, name='display-ranking'),

]
