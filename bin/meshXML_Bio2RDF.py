import sys
import os
import itertools
from datetime import datetime
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree


def main(xmlFile, outputFile):
  startTime = datetime.now()
  count = 1
  print "Parsing XML file %s..."%(xmlFile)
  tree = etree.parse(xmlFile)
  print "Done."
  print "Iterating over the model"
  descriptorRecordSet = tree.getroot()
  bufsize = 2000
  f = open(outputFile, 'w', bufsize)

  for descriptorRecord in descriptorRecordSet:
    if count % 1000 == 0 :
      endTime = datetime.now()
      print str(count) + " descriptors parsed in %s seconds"%str((endTime-startTime).seconds)
    startTime = endTime
    descriptorUI = descriptorRecord.find("DescriptorUI")
    descriptorName = descriptorRecord.find("DescriptorName")
    treeNumberList = descriptorRecord.find("TreeNumberList")
    conceptList = descriptorRecord.find("ConceptList")

    print(descriptorUI.text, "|", descriptorName.getchildren()[0].text, "|", treeNumberList.getchildren()[0].text, "\n")

    f.write(descriptorUI.text, "|", descriptorName.getchildren()[0].text, "|", treeNumberList.getchildren()[0].text)
    f.flush()

    #5) Iterate over conceptList
    for concept in conceptList.getchildren():
      conceptUI 				= concept.find("ConceptUI")
      conceptName 			= concept.find("ConceptName")
      termList 				= concept.find("TermList")
      conceptRelationList 	= concept.find("conceptRelationList")

      if conceptUI is None:
        continue

      if conceptRelationList is not None:
        for conceptRelation in conceptRelationList.getchildren():
          if conceptRelation.attrib["RelationName"] == "NRW":
            pass
          elif conceptRelation.attrib["RelationName"] == "BRD":
            pass
      termNodes = []
      for term in termList.getchildren():
        termUI			= term.find("TermUI")
        termName		= term.find("String")
        termLexicalTag	= term.attrib["LexicalTag"]

        if termUI is None :
          continue
    count+=1
  f.close()
  print "Done."
  print "Saving n-triple to file..."
  print "Done."

def help():
  print "Usage: python meshXML2RDF.py [desc2014.xml] [output rdf file]"
  print ""
  print "This script parse the MESH xml dump file and turn it into an rdf triple file following partially the bio2rdf convention."
  print "Please go to http://bio2rdf.org/ for more information"
  print "Author : Kevin Francoisse (https://github.com/kfrancoi)"
  print "Company : Sagacify (http://sagacify.com)"


if __name__ == '__main__':
  if (len(sys.argv) != 3):
    help()
  else :
    print "Input : " + sys.argv[1]
    print "Output :" + sys.argv[2]
    main(sys.argv[1], sys.argv[2])
