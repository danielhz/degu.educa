from zope.interface import Interface
from zope import schema

from degu.educa import DeguEducaMessageFactory as _

# Marker interfaces

class IHasDAMCode(Interface):
    """Marker interface for content with the DAM code field, which is enabled
    via a schema extender.
    
    This is applied to relevant types in content/configure.zcml.
    """

# Settings stored in the registry

class IDeguSettings(Interface):
    """Describes registry records
    """
    
    damCodes = schema.Tuple(
            title=_(u"Digital Asset Management codes"),
            description=_(u"Allowable values for the DAM code field"),
            value_type=schema.TextLine(),
        )
