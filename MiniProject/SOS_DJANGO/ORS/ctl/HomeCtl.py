from django.shortcuts import render
from .BaseCtl import BaseCtl



class HomeCtl(BaseCtl):
    def display(self, request, id = 0):
        # print("homctlprint")
        return render(request,self.get_template())

    def register(self, request, id = 0):
        # print("register here")
        return render(request, self.get_register())

    def get_template(self):
        return "Home.html"
