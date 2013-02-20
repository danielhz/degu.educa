# -*- coding: utf-8 -*-

from five import grok
from zope import schema
from plone.directives import form

from zope.interface import Invalid

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage
from plone.app.textfield import RichText

from degu.educa import DeguEducaMessageFactory as _

class IStudentFolder(form.Schema):
    """A container for students
    """

class View(grok.View):
    """Default view (called "@@view"") for a contact.
    
    The associated template is found in student_templates/view.pt.
    """
    
    grok.context(IStudentFolder)
    grok.require('zope2.View')
    grok.name('view')

