from django.shortcuts import render
from django.views import generic
from django.utils.translation import get_language, gettext_lazy as _
from django.conf import settings
from django.urls import reverse


class LanguageContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_language = get_language() or settings.LANGUAGE_CODE
        context['APP_LAYOUT_LANGUAGE'] = current_language
        # Set direction based on language - you can customize this list
        rtl_languages = {'ar', 'he', 'fa'}  # Arabic, Hebrew, Persian
        context['APP_LAYOUT_DIRECTION'] = 'rtl' if current_language in rtl_languages else 'ltr'
        return context


class SEOContextMixin:
    page_title = ""
    meta_description = ""
    meta_keywords = ""
    meta_author = _("Amir 77 İnşaat")  # Company name
    robots_content = "index, follow"  # Default robots content
    
    def get_canonical_url(self):
        return self.request.build_absolute_uri(reverse(self.request.resolver_match.view_name))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PAGE_META'] = {
            'PAGE_TITLE': self.page_title,
            'META_DESCRIPTION': self.meta_description,
            'META_KEYWORDS': self.meta_keywords,
            'CANONICAL_URL': self.get_canonical_url(),
            'ROBOTS_CONTENT': self.robots_content,
            'OG_IMAGE_1080x1080_PATH': 'CoreApp/images/og-image.jpg',  # Default OG image
        }
        context['META_AUTHOR'] = self.meta_author
        return context


class HomeView(LanguageContextMixin, SEOContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/index.html'
    page_title = _("Amir 77 İnşaat – Güvenilir ve Kaliteli İnşaat Hizmetleri")
    meta_description = _("Beton dökme, kalıpçılık, demir donatı, duvar örme ve tavan işleri konularında uzman ekibimizle hizmetinizdeyiz. Güçlü referanslarımız ve yılların tecrübesi ile inşaat projelerinize en iyi çözümleri sunuyoruz.")
    meta_keywords = _("inşaat, beton dökme, kalıpçılık, demir donatı, duvar örme, tavan işleri, Yalova inşaat")

    def dispatch(self, request, *args, **kwargs):
        # Any Test Code Here
        # Specific Use Cases:
        # Pre-rendering Data Preparation: Fetching or manipulating data required for the template before rendering.
        # Access Control: Implementing authentication or authorization checks to restrict access to certain users.
        # Dynamic Template Selection: Choosing the appropriate template based on conditions or user input.
        # Custom Rendering Logic: Handling special cases or alternative rendering approaches.

        # Call the parent class's dispatch method to continue processing the request
        return super().dispatch(request, *args, **kwargs)


class AboutView(LanguageContextMixin, SEOContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/about.html'
    page_title = _("Hakkımızda | Amir 77 İnşaat")
    meta_description = _("2021'den beri 15 yılı aşkın sektör deneyimimizle beton dökme, kalıpçılık, demir donatı, duvar örme ve tavan işleri alanlarında profesyonel hizmet sunuyoruz.")
    meta_keywords = _("Amir 77 İnşaat, inşaat şirketi, yapı hizmetleri, Yalova müteahhit, inşaat deneyimi")


class PortfolioItemView(LanguageContextMixin, SEOContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/portfolio-item.html'
    page_title = _("Projelerimiz | Amir 77 İnşaat")
    meta_description = _("Diyarbakır ve çevresinde tamamladığımız ve devam eden inşaat projelerimiz. Beton dökme, kalıpçılık ve demir donatı işlerinde uzman çözümler.")
    meta_keywords = _("inşaat projeleri, tamamlanan projeler, devam eden projeler, Diyarbakır inşaat, yapı projeleri")


class ServicesView(LanguageContextMixin, SEOContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/services.html'
    page_title = _("Hizmetlerimiz | Amir 77 İnşaat")
    meta_description = _("Beton dökme, kalıpçılık, demir donatı işleri, duvar örme ve çatı uygulamaları dahil olmak üzere tüm yapı işleriniz için profesyonel inşaat hizmetleri sunuyoruz.")
    meta_keywords = _("beton dökme, kalıp işleri, demir donatı, duvar örme, çatı işleri, inşaat hizmetleri")


class ContactView(LanguageContextMixin, SEOContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/contact.html'
    page_title = _("İletişim | Amir 77 İnşaat")
    meta_description = _("Amir 77 İnşaat Ticaret Sanayi Limited Şirketi ile iletişime geçin. Yalova'da profesyonel inşaat ve yapı hizmetleri için bize ulaşın.")
    meta_keywords = _("Amir 77 İnşaat iletişim, Yalova inşaat firması, inşaat teklifi, yapı hizmetleri iletişim")


class CaseStudiesView(LanguageContextMixin, SEOContextMixin, generic.TemplateView):
    template_name = 'HomeApp/architect4/case-studies.html'
    page_title = _("Örnek Projeler | Amir 77 İnşaat")
    meta_description = _("İnşaat projelerimizden örnekler ve detaylı süreç analizleri. Beton dökme, kalıpçılık, demir donatı ve duvar örme işlerindeki uzmanlığımızı keşfedin.")
    meta_keywords = _("inşaat örnekleri, proje detayları, yapı süreçleri, inşaat çözümleri, başarı hikayeleri")
