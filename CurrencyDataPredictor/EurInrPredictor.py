from xml.etree import ElementTree

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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


rate=map(float,rate)
dates = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in time]
dates.pop()

plt.plot_date(x=dates, y=rate,fmt="r-")
plt.title("Currency rate INR in Years")
plt.ylabel("INR")
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.show()

