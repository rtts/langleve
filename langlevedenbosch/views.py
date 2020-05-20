from django.utils.translation import gettext_lazy as _
from cms.views import SectionView, SectionFormView
from cms.decorators import section_view
from cms.forms import ContactForm

@section_view
class Text(SectionView):
    verbose_name = _('Text')
    fields = ['content']
    template_name = 'text.html'

@section_view
class Introduction(SectionView):
    verbose_name = 'Introductie'
    fields = ['content']
    template_name = 'introduction.html'

@section_view
class Teasers(SectionView):
    verbose_name = 'Teasers'
    fields = ['teasers']
    template_name = 'teasers.html'

@section_view
class Images(SectionView):
    verbose_name = 'Afbeelding(en)'
    fields = ['images']
    template_name = 'images.html'

@section_view
class LargeHeader(SectionView):
    verbose_name = 'Header (groot)'
    fields = ['content']
    template_name = 'header_large.html'

@section_view
class SmallHeader(SectionView):
    verbose_name = 'Header (klein)'
    fields = []
    template_name = 'header_small.html'

@section_view
class Video(SectionView):
    verbose_name = _('Video')
    fields = ['video']
    template_name = 'video.html'

@section_view
class Contact(SectionFormView):
    verbose_name = _('Contact')
    fields = []
    form_class = ContactForm
    success_url = '/thanks/'
    template_name = 'contact.html'
