import xml.etree.ElementTree as ET
mytree = ET.parse('starterClasses.xml')
myroot = mytree.getroot()


import xml.etree.ElementTree as ET
mytree = ET.parse('starterClasses.xml')
myroot = mytree.getroot()

print(myroot[0][5].text)
print(myroot[0][0].text)
print(myroot[0][4].text)
print(myroot[1][3].text)
print(myroot[1][2].text)
print(myroot[1][1].text)

###################################################################################

import json
 
with open('starterClasses.json') as json_file:
    data = json.load(json_file)
    print(data)


open_json = open('starterClasses.json')
data = json.load(open_json)

for json_contents in data:
    print(json_contents)

open_json.close()
