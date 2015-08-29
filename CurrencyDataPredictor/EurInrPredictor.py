from xml.etree import ElementTree


with open('eurofxref-hist-90d.xml', 'rt') as f:
    tree = ElementTree.parse(f)


for node in tree.iter('{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube'):
    time=node.attrib.get('time')
    currency=node.attrib.get('currency')    
    if None != time:
        print time
    if currency == 'INR':
        rate=node.attrib.get('rate')
        print currency,rate


         
         
         

