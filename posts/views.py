from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render

class MyView(View):
    def get(self, request):
        data = {
            'name': 'Pierre Chavez',
            'age': 27,
            'hobbies': ['coding', 'reading', 'gaming']

        }
        return render(request, 'hello_world.html', context=data)
        
