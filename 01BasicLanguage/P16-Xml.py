import xml.etree.ElementTree as Et

tree = Et.parse('./test.xml')
root = tree.getroot()
person = root.find("person")
name = person.find("name")
print(name.text)