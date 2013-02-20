# -*- coding: utf-8 -*-

from five import grok
from zope import schema
from plone.directives import form

from zope.interface import Invalid

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage
from plone.namedfile.field import NamedBlobFile

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.textfield import RichText

from degu.educa import DeguEducaMessageFactory as _

class IEducativeExperience(form.Schema):
    """An educative experience to share.
    """
    creador = schema.TextLine(
        title=_(u"Creadores"),
        description=_(u"Las personas que desarrollaron la experiencia"),
    )
    
    establecimiento = schema.Choice(
        title=_(u"Establecimiento"),
        description=_(u"Dónde se realizó la experiencia"),
        vocabulary=SimpleVocabulary(
            [SimpleTerm(value=u'Liceo San Francisco de Placilla', title=_(u'Liceo San Francisco de Placilla')),
             SimpleTerm(value=u'Escuela Raul Caceres Pacheco', title=_(u'Escuela Raúl Cáceres Pacheco')),
             SimpleTerm(value=u'Escuela F-474 La Dehesa', title=_(u'Escuela F-474 La Dehesa')),
             SimpleTerm(value=u'Escuela Dany Gonzalez Soto', title=_(u'Escuela Dany González Soto')),
             SimpleTerm(value=u'Escuela Amanecer de lo Moscoso', title=_(u'Escuela Amanecer de lo Moscoso')),
             SimpleTerm(value=u'Escuela de la Tuna', title=_(u'Escuela de la Tuna')),
             SimpleTerm(value=u'Escuela G-470 San Luis de Manantiales', title=_(u'Escuela G-470 San Luis de Manantiales')),
             SimpleTerm(value=u'Jardin Sala Cuna Pampanitos', title=_(u'Jardín Sala Cuna Pampanitos'))]
            ),
        required=True,
        )

    nivel = schema.TextLine(
            title=_(u"Nivel"),
        )

    asignatura = schema.TextLine(
            title=_(u"Asignatura"),
        )

    unidad = schema.TextLine(
            title=_(u"Unidad"),
        )

    objetivo = schema.Text(
            title=_(u"Objetivo"),
        )

    duracion = schema.TextLine(
            title=_(u"Duración"),
            description=_(u"Cuánto duró la experiencia"),
        )

    descripcion = RichText(
            title=_(u"Descripción detallada de la experiencia"),
        )

    logros = RichText(
            title=_(u"Logros"),
        )

class View(grok.View):
    """Default view (called "@@view"") for a contact.
    
    The associated template is found in educativeexperience_templates/view.pt.
    """
    
    grok.context(IEducativeExperience)
    grok.require('zope2.View')
    grok.name('view')
