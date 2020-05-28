from django.db import models
from django.utils.translation import gettext_lazy as _
from cms.models import BasePage, BaseSection, Numbered, VarCharField
from cms.decorators import page_model, section_model

@page_model
class Page(BasePage):
    '''Add custom fields here. Already existing fields: title, slug,
    number, menu

    '''

@section_model
class Section(BaseSection):
    '''Add custom fields here. Already existing fields: title, type,
    number, content, image, video, href

    '''
    page = models.ForeignKey(Page, related_name='sections', on_delete=models.PROTECT)

class SectionImage(models.Model):
    section = models.ForeignKey(Section, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(_('Image'))

    class Meta:
        ordering = ['pk']

class SectionTeaser(models.Model):
    section = models.ForeignKey(Section, related_name='teasers', on_delete=models.CASCADE)
    title = VarCharField('titel')
    image = models.ImageField(_('image'), blank=True)
    content = models.TextField(_('content'), blank=True)
    href = VarCharField(_('link'), blank=True)

    class Meta:
        ordering = ['?']

class SectionCalendar(Numbered, models.Model):
    section = models.ForeignKey(Section, related_name='calendar_items', on_delete=models.CASCADE)
    title = VarCharField('titel')
    initiative = VarCharField('naam initiatief')
    position = models.PositiveIntegerField('positie', blank=True)
    date = VarCharField('datum')
    time = VarCharField('tijd')
    subscript = VarCharField('onderschrift')
    location = VarCharField('locatie')
    image = models.ImageField(_('image'), blank=True)
    href = VarCharField(_('link'), blank=True)

    def number_with_respect_to(self):
        return self.section.calendar_items.all()

    class Meta:
        ordering = ['position']
