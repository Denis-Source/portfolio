from django.views.generic import FormView, TemplateView
from projects.models import Project
from category.models import Category

from certificate.models import Certificate
from skill.models import Skill

from homepage.forms import ContactForm
from homepage.bot import send_form_threaded


class HomePageView(FormView):
    template_name = "homepage.html"
    form_class = ContactForm
    success_url = "/success"

    def get_context_data(self, **kwargs):
        data = {"project_list": Project.objects.all(), "category_list": Category.objects.all(),
                "certificate_list": Certificate.objects.all(), "skill_list": Skill.objects.all(),
                "total_projects": len(Project.objects.all())}
        return data

    def form_valid(self, form):
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            send_form_threaded(subject, message)
        return super(HomePageView, self).form_valid(form)


class SuccessPageView(TemplateView):
    template_name = "success.html"
