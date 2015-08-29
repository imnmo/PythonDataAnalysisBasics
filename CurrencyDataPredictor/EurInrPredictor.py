from xml.etree import ElementTree

with open('eurofxref-hist.xml', 'rt') as f:
    tree = ElementTree.parse(f)

time=[]
rate=[]
TIME='2010-01-04'  #A breif history in time
for node in tree.iter('{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube'):
    
    tmpTime=(node.attrib.get('time'))
    currency=node.attrib.get('currency')    
    if None != tmpTime:
        time.append(node.attrib.get('time'))
        if tmpTime == TIME: #go until only the specified time
            break
    if currency == 'INR':
        rate.append(node.attrib.get('rate'))





print "####################################################"
print time
print rate
      
         
         

