# -*- coding: utf-8 -*-

from sinar.miscbehavior import _
from plone import schema
from collective import dexteritytextindexer
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

    dexteritytextindexer.searchable('assessment_notes')
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
                 developed during the project cycle and the usefulness
                 of these in achieving the project's objectives.
                 <br />
                 Describe the involvement of project beneficiaries,
                 during all phases of project implementation.
                 <br />
                 Describe any gender, ethnic and generation gap issues that have impacted positively or negatively your project implementation.
                 <br />
                 Please take the time to reflect about activities that you struggle to implement during the period reported, along with processes and methods originally planned that might need adjustment to achieve your project objectives.
                 </p>
                 <p>
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
