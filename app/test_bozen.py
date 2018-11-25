# test_bozen.py = test the bozen library


from bozen import lintest

group = lintest.TestGroup()

import test_fieldinfo
group.add(test_fieldinfo.group)

import test_timefield
group.add(test_timefield.group)

import test_formdoc
group.add(test_formdoc.group)

import test_mongo
group.add(test_mongo.group)

import test_mondoc
group.add(test_mondoc.group)

if __name__=='__main__': group.run()

#end
