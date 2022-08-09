# -*- coding: utf-8 -*-

from plone import schema
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from Products.CMFPlone.utils import safe_hasattr
from sinar.miscbehavior import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class ICountriesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ICountries(model.Schema):
    """
    """
    directives.widget(countries=SelectFieldWidget)
    countries = schema.List(
        title=_(u'Countries'),
        description=_(u'Countries applicable to this content type'),
        required=False,
        value_type=schema.Choice(
            vocabulary="collective.vocabularies.iso.countries",
        ),
    )

    # fieldset set the tabs on the edit form

    fieldset(
            'categorization',
            fields=[
                'countries',
                ],
            )


@implementer(ICountries)
@adapter(ICountriesMarker)
class Countries(object):
    def __init__(self, context):
        self.context = context

    @property
    def countries(self):
        if safe_hasattr(self.context, 'countries'):
            return self.context.countries
        return None

    @countries.setter
    def countries(self, value):
        self.context.countries = value
