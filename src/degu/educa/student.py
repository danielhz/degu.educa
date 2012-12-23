# -*- coding: utf-8 -*-

from five import grok
from zope import schema
from plone.directives import form

from zope.interface import Invalid

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage

from plone.app.textfield import RichText

from degu.educa import DeguEducaMessageFactory as _

class IStudent(form.Schema):
    """A contact card.
    """
    
    title = schema.TextLine(
            title=_(u"Nombre"),
            description=_(u"Nombre completo del alumno"),
        )

    birth = schema.Date(
            title=_(u"Fecha de nacimiento"),
            description=_(u"Fecha de nacimiento"),
        )

    rut = schema.TextLine(
            title=_(u"RUT"),
            description=_(u"Por ejemplo 12345678-9."),
        )

    address = schema.TextLine(
            title=_(u"Dirección"),
            description=_(u"Por ejemplo Vicuña Mackenna 123, Depto 456, Santiago."),
        )

    phone = schema.TextLine(
            title=_(u"Teléfono"),
            description=_(u"De la madre o del padre"),
        )

    health = schema.TextLine(
            title=_(u"Previsión de salud"),
            description=_(u"ISAPRE o FONASA"),
        )

    afp = schema.TextLine(
            title=_(u"AFP"),
            description=_(u"AFP del padre o de la madre"),
        )

    programaPuente = schema.Bool(
            title=_(u"Programa Puente"),
        )

    prioritario = schema.Bool(
            title=_(u"Prioritario"),
        )

    vulnerable = schema.Bool(
            title=_(u"Vulnerable"),
        )

    chileSolidario = schema.Bool(
            title=_(u"Chile Solidario"),
        )

    fatherName = schema.TextLine(
            title=_(u"Nombre del padre"),
        )

    fatherStudies = schema.TextLine(
            title=_(u"Escolaridad del padre"),
        )

    motherName = schema.TextLine(
            title=_(u"Nombre de la madre"),
        )

    motherStudies = schema.TextLine(
            title=_(u"Escolaridad de la madre"),
        )

class View(grok.View):
    """Default view (called "@@view"") for a contact.
    
    The associated template is found in contact_templates/view.pt.
    """
    
    grok.context(IStudent)
    grok.require('zope2.View')
    grok.name('view')
