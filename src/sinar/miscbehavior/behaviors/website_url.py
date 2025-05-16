# -*- coding: utf-8 -*-

from sinar.miscbehavior import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IWebsiteUrlMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IWebsiteUrl(model.Schema):
    """
    """

    website_url = schema.URI(
        title=_('Website URL'),
        description=_('Link to website or external content'),
        required=False,
    )


@implementer(IWebsiteUrl)
@adapter(IWebsiteUrlMarker)
class WebsiteUrl(object):
    def __init__(self, context):
        self.context = context

    @property
    def website_url(self):
        if safe_hasattr(self.context, 'website_url'):
            return self.context.website_url
        return None

    @website_url.setter
    def website_url(self, value):
        self.context.website_url = value
