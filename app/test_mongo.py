# test_mongo.py = tests <mongo.py>


from bozen.butil import *
from bozen import lintest

from bozen.mongo import isObjectIdStr

#---------------------------------------------------------------------

class T_functions(lintest.TestCase):
    """ test various functions """
    
    def test_isObjectIdStr(self):
        r = isObjectIdStr("123") 
        self.assertFalse(r, "too short")
        r = isObjectIdStr("123aaaaabbbbbcccccdddddeeeeefffff") 
        self.assertFalse(r, "too long")
        r = isObjectIdStr("aaaaabbbbb0123456789ffff") 
        self.assertTrue(r, "right length")
        r = isObjectIdStr("aaaaabbbbb0123456789xxxx") 
        self.assertFalse(r, "illegal character 'x'")

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_functions)

if __name__=='__main__': group.run()


#end
