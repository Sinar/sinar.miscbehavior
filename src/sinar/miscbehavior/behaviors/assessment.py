# -*- coding: utf-8 -*-

from sinar.miscbehavior import _
from plone import schema
try:
    from plone.app.dexterity import textindexer
except ImportError:
    from collective import dexteritytextindexer as textindexer
from plone.app.textfield import RichText
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.autoform import directives
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


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
                             '''),
        default=_('''
                 <p class="callout">
                 Describe any partnerships with other organizations,
                 researchers and community leaders that have been
                 developed and the usefulness
                 of these in achieving objectives.
                 </p>
                 <p>notes ...</p>
                 <p class="callout">
                 Describe the involvement of beneficiaries,
                 during all phases of implementation.
                 </p>
                 <p>notes ... </p>
                 <p class="callout">
                 Describe any gender, ethnic and generation gap issues
                 that have impacted implementation, positively or
                 negatively.</p>
                 <p>notes ... </p>
                 <p class="callout">
                 Please take the time to reflect about activities that you struggle to implement, along with processes and methods originally planned that might need adjustment to achieve objectives.
                 </p>
                 '''),
        required=False,
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
