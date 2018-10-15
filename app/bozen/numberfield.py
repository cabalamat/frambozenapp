# numberfield.py = numeric fields

"""
<numberfield.py> contains fields (FieldInfo subclasses)
for date and time. These are:

- IntField
- FloatField
- BoolField

"""


from .butil import *

from . import fieldinfo

#---------------------------------------------------------------------

class IntField(fieldinfo.FieldInfo):
    """ a field holding a Python int """

    #def readArgs(self, **kwargs):
    #    super(IntField, self).readArgs(**kwargs)

    def defaultDefault(self):
        """ return the default value for the default value of the
        object.
        """
        return 0

    def convertValue(self, v):
        try:
            i = int(v)
        except:
            i = self.defaultValue
        return i

#---------------------------------------------------------------------


#end
