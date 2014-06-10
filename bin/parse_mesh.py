#!/usr/bin/python

import xml.etree.ElementTree as ET
print 'Parsing XML'
tree = ET.parse('desc2014.xml')
root = tree.getroot()
outfile = open("meshtrees.txt","w")
print 'output ...'
for child in root:
  id = child.find('DescriptorUI').text
  name = child.find('DescriptorName').find('String').text
  tlist = child.find('TreeNumberList')
  if tlist != None:
    treenums = tlist.findall('TreeNumber')
    for treenum in treenums:
      outfile.write('%s\t%s\t%s\n'% ( id, name, treenum.text))
outfile.close()
print 'done'
