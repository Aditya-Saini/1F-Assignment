from .models import RequestCounterModel
class CounterMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        try:
            queryset = RequestCounterModel.objects.get(pk=1)
            queryset.counter+=1
            queryset.save()
        except Exception as e:
            counter = RequestCounterModel(counter=1)
            counter.save()
        response = self.get_response(request)
        return response
