from django.shortcuts import redirect, render

# Create your views here.
from django.views.generic import TemplateView
from . import forms


class HomePageView(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
     
        user_form = self.form_class(request.POST)

        if user_form.is_valid():
            user_form.save()
        
            return redirect('index')


    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            context["form"].save()
        
            return redirect('index')


        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        form = forms.ContactForm(self.request.POST or None) 

        context["form"] = form

        return context



