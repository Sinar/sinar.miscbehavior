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
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.autoform import directives
from plone.supermodel import model


class IDigitalRightsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IDigitalRights(model.Schema):
    """
    """
    directives.widget(digital_rights_categories=SelectFieldWidget)
    digital_rights_categories = schema.List(
        title=_('Digital Rights Categories'),
        description=_('''
        Digital rights categorues applicable to the
        content.'''),
        value_type=schema.Choice(
            vocabulary='sinar.miscbehavior.DigitalRights',),
        required=False,
    )

    model.fieldset(
        'categorization',
        fields=['digital_rights_categories']
    )


@implementer(IDigitalRights)
@adapter(IDigitalRightsMarker)
class DigitalRights(object):
    def __init__(self, context):
        self.context = context

    @property
    def digital_rights_categories(self):
        if safe_hasattr(self.context, 'digital_rights_categories'):
            return self.context.digital_rights_categories
        return None

    @digital_rights_categories.setter
    def digital_rights_categories(self, value):
        self.context.digital_rights_categories = value
