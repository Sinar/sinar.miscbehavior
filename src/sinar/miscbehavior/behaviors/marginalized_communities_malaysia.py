# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from sinar.miscbehavior import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IMarginalizedCommunitiesMalaysiaMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IMarginalizedCommunitiesMalaysia(model.Schema):
    """
    """

    project = schema.TextLine(
        title=_(u'Project'),
        description=_(u'Give in a project name'),
        required=False,
    )


@implementer(IMarginalizedCommunitiesMalaysia)
@adapter(IMarginalizedCommunitiesMalaysiaMarker)
class MarginalizedCommunitiesMalaysia(object):
    def __init__(self, context):
        self.context = context

    @property
    def project(self):
        if safe_hasattr(self.context, 'project'):
            return self.context.project
        return None

    @project.setter
    def project(self, value):
        self.context.project = value
