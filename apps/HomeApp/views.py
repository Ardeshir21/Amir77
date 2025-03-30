from django.shortcuts import render
from django.views import generic
from django.utils.translation import get_language
from django.conf import settings


class LanguageContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_language = get_language() or settings.LANGUAGE_CODE
        context['APP_LAYOUT_LANGUAGE'] = current_language
        # Set direction based on language - you can customize this list
        rtl_languages = {'ar', 'he', 'fa'}  # Arabic, Hebrew, Persian
        context['APP_LAYOUT_DIRECTION'] = 'rtl' if current_language in rtl_languages else 'ltr'
        return context


class HomeView(LanguageContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/index.html'

    def dispatch(self, request, *args, **kwargs):
        # Any Test Code Here
        # Specific Use Cases:
        # Pre-rendering Data Preparation: Fetching or manipulating data required for the template before rendering.
        # Access Control: Implementing authentication or authorization checks to restrict access to certain users.
        # Dynamic Template Selection: Choosing the appropriate template based on conditions or user input.
        # Custom Rendering Logic: Handling special cases or alternative rendering approaches.

        # Call the parent class's dispatch method to continue processing the request
        return super().dispatch(request, *args, **kwargs)


class AboutView(LanguageContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/about.html'


class PortfolioItemView(LanguageContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/portfolio-item.html'


class ServicesView(LanguageContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/services.html'


class ContactView(LanguageContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/contact.html'


class CaseStudiesView(LanguageContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/case-studies.html'
