# keychoicefield.py = key and choice fields

from . import butil
from .butil import *
from . import bozenutil

from .fieldinfo import fieldIndex, FieldInfo, StrField

#---------------------------------------------------------------------


class ChoiceField(StrField):
    """ A ChoiceField takes a choices argument of the form:
        choices=[('C', 'collection'),
                 ('D', 'delivery'),
                 ('N', 'none')]
    The 0th element of the tuple is the value of the field;
    the 1st is the displayed value. The default is the value of
    the initial tuple, unless a specific default is set.
    """

    def readArgs(self, **kwargs):
        super(ChoiceField, self).readArgs(**kwargs)
        choices = kwargs.get('choices',
            (('N','No'),('Y','Yes'))
        )
        choices2 = []
        for ch in choices:
            if isinstance(ch,tuple):
                v = ch
            else:
                v = (ch,ch)
            choices2.append(v)
        #for
        self.choices = choices2
        if 'default' not in kwargs:
            self.defaultValue = self.choices[0][0]

        # if true, includes a null option on the form
        self.showNull = kwargs.get('showNull', False)
        if self.showNull:
            self.defaultValue = ''

        # if true, allow user to select the null option on the form
        self.allowNull = kwargs.get('allowNull', True)

    def formField_rw(self, v, **kwargs):
        """ return html for a form field for this fieldInfo
        @param v [ObjectId] the value in the field for the MonDoc
        @return [str] containing html
        """
        return renderChoices(self.fieldName, self.getChoices(v), v)

    def getChoices(self, v):
        """
        :param str v: the current value
        :rtype choices: [(dbValue::str, screenValue::str)]
        """
        choices = self.choices
        #prvars("v choices")
        if self.showNull:
            choices = [('',"- select one -")] + choices
        #prvars("choices")
        return choices

    def convertToReadable(self, v):
        """
        @param v::str
        @return::str
        """
        for value, show in self.choices:
            if v==value:
                return show
        #//for
        return v


    def errorMsg(self, v):
        """
        :return an error message, or "" if there are no errors
        :rtype str
        """
        msg = ""
        if not self.allowNull and not v:
            msg += "You must select an option"
        return msg

#---------------------------------------------------------------------

class FK: pass

class FKeys: pass

#---------------------------------------------------------------------
# convenience function for ChoiceField and FK

def renderChoices(fieldName, choices, chosen):
    """
    :param str fieldName: the field name
    :param choices: the chocies presented to the user
    :param choices: [(dbValue::str, screenValue::str)]
    :param chosen: the pre-selected choice (or None if none)
    :type chosen: str | None
    :return str containing an html <select> control
    :rtype str
    """

    h = form("<select id='id_{fieldName}' name='{fieldName}'>\n",
        fieldName = fieldName)
    for choiceVal, choiceStr in choices:
        selected = ""
        if chosen == choiceVal:
            selected = " selected='selected'"
        h += form("<option value='{cv}'{selected}>{cs}</option>\n",
            cv = choiceVal,
            cs = choiceStr,
            selected = selected)
    #//for
    h += "</select>\n"
    return h


#---------------------------------------------------------------------



#end
