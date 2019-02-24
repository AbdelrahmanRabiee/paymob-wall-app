from django.views.generic import TemplateView


class SignUp(TemplateView):
    template_name = 'account/signup.html'


class SignIn(TemplateView):
    template_name = 'account/login.html'
