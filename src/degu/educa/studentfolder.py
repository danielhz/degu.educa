from five import grok
from zope import schema
from plone.directives import form

class IStudentFolder(form.Schema):
    """A container for students
    """

# Note that we use the standard folder_listing view for this type, so there
# is no specific view here
