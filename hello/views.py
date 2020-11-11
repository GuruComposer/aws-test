from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request, name):

        ctx = {
            'name': name,
        }
        return render(request, "hello/index.html", ctx)