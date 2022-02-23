from django.shortcuts import render
from django.views import View

# Create your views here.

class setView(View):
    def context(self, **kwargs):
        context = super().context(**kwargs)
        return context
