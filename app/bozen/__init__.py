# __init__.py = initialisation for Bozen

# For relative imports to work in Python 3.6
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))


#---------------------------------------------------------------------
# utility and debugging modules

#import butil


#---------------------------------------------------------------------
# bozen main classes

from .formdoc import FormDoc

from .fieldinfo import FieldInfo, StrField
from .keychoicefield import ChoiceField
from .numberfield import IntField

                       
#---------------------------------------------------------------------



#end
