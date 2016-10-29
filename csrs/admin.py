from django.contrib import admin

# Register your models here.
from models import *
# Register your models here.
admin.site.register(Provider)
admin.site.register(Service)
admin.site.register(Feature)
admin.site.register(ProviderService)
admin.site.register(ServiceFeature)
admin.site.register(BenchMark)
admin.site.register(UserFeedback)

