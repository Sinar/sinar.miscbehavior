# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from sinar.miscbehavior import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.autoform import directives
from plone.supermodel.directives import primary
from Products.CMFPlone.utils import safe_hasattr


class IDevelopmentThemesMarker(Interface):
    pass

@provider(IFormFieldProvider)
class IDevelopmentThemes(model.Schema):
    """
    """

    directives.widget(development_themes=SelectFieldWidget)
    development_themes = schema.List(
        title=_(u'Development Themes'),
        description=_(u'General development theme or category.'),
        value_type = schema.Choice(
            vocabulary='sinar.miscbehavior.DevelopmentThemes',),
        required=False,
    )

    model.fieldset(
        'categorization',
        fields=['development_themes']
    )

@implementer(IDevelopmentThemes)
@adapter(IDevelopmentThemesMarker)
class DevelopmentThemes(object):
    def __init__(self, context):
        self.context = context

    @property
    def development_themes(self):
        if safe_hasattr(self.context, 'development_themes'):
            return self.context.development_themes
        return None

    @development_themes.setter
    def development_themes(self, value):
        self.context.development_themes = value
