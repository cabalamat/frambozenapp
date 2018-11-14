# multichoicefield.py

from .butil import *
from . import fieldinfo

#---------------------------------------------------------------------

class MultiChoiceField(fieldinfo.FieldInfo):

    def readArgs(self, **kwargs):
        super(MultiChoiceField,self).readArgs(**kwargs)
        self.choices = kwargs.get('choices', [])
        self.separateLines = kwargs.get('separateLines', True)


    def defaultDefault(self):
        """ return the default value for the default value of the
        object.
        """
        return []

    def convert(self, v):
        """ Convert a value from something got from a form to a value
        that can be stored in the database for that field.
        :param: [str]
        :type v: [str]
        :rtype str
        """
        return v # may need changing later

    def convertValue(self, v):
        """ doesn't apply since MultiChoiceField is read-only """
        return None


    def formField_rw(self, v, **kwargs):
        ch = dict(self.choices)
        h = ""
        if self.separateLines:
            span = ""
            endSpan = ""
            br = "<br>"
        else:
            span = "<span class='mcf-keep-together'>"
            endSpan = "</span>"
            br = ""
        for dn, sn in self.choices:
            h += form("""{span}<input type="checkbox" id="id_{fn}_{value}"
                name="{fn}" value="{value}" {checked}>
                {showValue}{endSpan} {br}""",
                fn = self.fieldName,
                value = dn,
                checked = "checked" if (dn in v) else "",
                showValue = sn,
                span = span,
                endSpan = endSpan,
                br = br
            )
        #//for
        return h


    def formField_ro(self, v, **kwargs):
        h = "<span class='read-only'>"
        for dn, sn in self.choices:
            if dn in v:
                icon = "<i class='fa fa-check-square'></i>"
            else:
                icon = "<i class='fa fa-square'></i>"
            h += form("{icon} {showValue}<br>",
                icon = icon,
                showValue = sn)
        #//for
        h = h[:-4] # remove last "<br>"
        h += "</span>"
        return h


    def convertToReadable(self, v):
        """ Convert the internal value in the database (v) to a readable
        value (i.e. a string or unicode that could de displayed in a form
        or elsewhere). This method is the opposite of the convertValue()
        method.

        :param v: value from database
        :type v: [str]
        :rtype str or unicode
        """
        ch = dict(self.choices)
        s = ", ".join(ch.get(dn, dn) for dn in v)
        return s


#---------------------------------------------------------------------

#end
