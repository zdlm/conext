# -*- coding: utf-8 -*-
from django.views.generic.base import View
from django.shortcuts import render_to_response

class HomeView(View):
    def get(self, *args, **kwargs):
        return render_to_response("home.html")

class QaView(View):
    def get(self, *args, **kwargs):
        return render_to_response("qa.html")
    