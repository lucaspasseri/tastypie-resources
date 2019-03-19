from tastypie.resources import ModelResource
from api_1.models import Hits
from tastypie.authorization import Authorization

class HitsResource(ModelResource):
    class Meta:
        queryset = Hits.objects.all()
        resource_name = 'hits'
        authorization=Authorization()