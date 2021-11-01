from django.views import View
from django.http import JsonResponse

class ResumeSelectorView(View):
    def get(self, request):
        print("get")
        return JsonResponse({'content' : 'get'})
    
    def post(self, request):
        print("post")
        return JsonResponse({'content' : 'post'})

