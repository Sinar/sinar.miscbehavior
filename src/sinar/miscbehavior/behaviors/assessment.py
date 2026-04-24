# -*- coding: utf-8 -*-

from sinar.miscbehavior import _


try:
    from plone.app.dexterity import textindexer
except ImportError:
    from collective import dexteritytextindexer as textindexer

from plone.app.textfield import RichText
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IAssessmentMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IAssessment(model.Schema):
    """
    """

    textindexer.searchable('assessment_notes')
    directives.read_permission(assessment_notes='cmf.ModifyPortalContent')
    directives.write_permission(assessment_notes='cmf.ModifyPortalContent')
    assessment_notes = RichText(
        title=_('Assessment Notes'),
        description=_('''
                    Notes related to the assessment of this project or
                    activity.
                             '''),
        default=_('''
## Improvement

_How would you rate the results of this project,
given the challenges mentioned in concept or project
document?_

No improvement, moderate or considerable
improvement?

## Reflections

_Please write 1-3 paragraphs on your experience_

- _What did you learn during process of
  implementation?_

- _What would partner about organisations facing
  similar challenges?_

## Misc

_Any other comments?_


                 '''),
        default_mime_type='text/x-web-markdown',
        output_mime_type='text/html',
        allowed_mime_types=('text/x-web-markdown', 'text/plain'),
        required=False,
    )

    # fieldset set the tabs on the edit form
    fieldset('MEL',
             label=_('MEL'),
             fields=['assessment_notes'],
             )


@implementer(IAssessment)
@adapter(IAssessmentMarker)
class Assessment(object):
    def __init__(self, context):
        self.context = context

    @property
    def assessment_notes(self):
        if safe_hasattr(self.context, 'assessment_notes'):
            return self.context.assessment_notes
        return None

    @assessment_notes.setter
    def assessment_notes(self, value):
        self.context.assessment_notes = value
