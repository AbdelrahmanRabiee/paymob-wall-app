from django.views.generic import TemplateView


class TimeLine(TemplateView):
    template_name = 'posts/index.html'


class AddPost(TemplateView):
    template_name = 'posts/add_post.html'
