from django.views.generic import FormView, TemplateView
from projects.models import Project
from category.models import Category

from certificate.models import Certificate
from discipline.models import Discipline
from skill.models import Skill

from homepage.forms import ContactForm
from homepage.bot import send_form_threaded


class HomePageView(FormView):
    """
    Main page view
    Based on The Built-in FormView Class
    As the bottom of the page contains contact form

    The form is expected to be sent via ajax request so the success url
    does not really matters

    The form is based on ContactForm Class defined in the corresponding file

    The page contains following database queries:
        Projects
        Project Categories
        Certificates
        Disciplines
        Skills
    All objects are sorted by their priority field
    """
    template_name = "homepage.html"
    form_class = ContactForm
    success_url = "/success"

    def get_context_data(self, **kwargs):
        """
        Adds database objects to the template context
        """
        data = {"project_list": Project.objects.all().order_by("-priority"),
                "category_list": Category.objects.all().order_by("-priority"),
                "certificate_list": Certificate.objects.all().order_by("-priority"),
                "discipline_list": Discipline.objects.all().order_by("-priority"),
                "skill_list": Skill.objects.all().order_by("-priority")}
        return data

    def form_valid(self, form):
        """
        If the form is valid sends the filled form by the telegram bot
        """
        if form.is_valid():
            # Concatenates name, email and message to send it as one message
            subject = form.cleaned_data["subject"]
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            # Calls the threaded function to send the request to Telegram API
            send_form_threaded(subject, message)
        return super(HomePageView, self).form_valid(form)


class SuccessPageView(TemplateView):
    """
    If the form is filled correct
    The request is redirected to the success page
    It is expected that form is sent via ajax request
    so the page does not really matter
    """
    template_name = "success.html"
