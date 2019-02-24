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

class FloatField(fieldinfo.FieldInfo):
    """ a field holding a Python float.

    Note that if you want fixed-point output then setting:

        formatStr="{:.2f}"

    gives you fixed point, 2 digits after the decimal point.
    """


    def defaultDefault(self):
        """ return the default value for the default value of the
        object.
        """
        return 0.0

    def convertValue(self, v):
        try:
            f = float(v)
        except:
            f = self.defaultValue
        return f

#---------------------------------------------------------------------

class BoolField(fieldinfo.FieldInfo):
    """ a field holding a Python bool """


    def readArgs(self, **kwargs):
        super().readArgs(**kwargs)
        self.widget = kwargs.get('widget', 'checkbox')
        self.offText = kwargs.get('offText', "Off")
        self.onText = kwargs.get('onText', "On")
        
    def defaultDefault(self):
        """ return the default value for the default value of the
        object.
        """
        return False

    def convertValue(self, v):
        return bool(v)

    def convertToScreen(self, v):
        s = "yes" if v else "no"
        return s

    def formField_rw(self, v, **kwargs):
        """ return  html for a form field for this fieldInfo, read-write
        """
        checked = ""
        if v: checked = " checked"
        if self.widget=='checkbox':
            h = form('''<input id="id_{fieldName}" type="checkbox"
                name="{fieldName}"{checked}>''',
                fieldName = self.fieldName,
                checked = checked,
            )
        elif self.widget=='toggleSwitch':
            h = form('''<label class="switch">
                <input id="id_{fieldName}" type="checkbox"
                name="{fieldName}"{checked}>
                <span class="slider round"></span></label>''',
                fieldName = self.fieldName,
                checked = checked,
            ) 
        else:
            raise ShouldntGetHere
        #endif        
        return h



#---------------------------------------------------------------------



#end
