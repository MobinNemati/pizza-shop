from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView




class blog(TemplateView):
    template_name = 'menu/blog.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


def about(request):
    return render(request, 'menu/about.html')



def BlogSingle(request):
    return render(request, 'menu/blog.html')



def contact(request):
    return render(request, 'menu/contact.html')



def index(request):
    return render(request, 'menu/index.html')



def menu(request):
    return render(request, 'menu/menu.html')



def services(request):
    return render(request, 'menu/services.html')