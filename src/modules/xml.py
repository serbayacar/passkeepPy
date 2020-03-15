import json

from src.modules.file import File
import xmltodict
import xml.etree.ElementTree as ETREE


class XML:
    path = "credentials.xml"
    tree = None

    def __init__(self):
        filePointer = File(self.path)
        tree = ETREE.parse(filePointer.getPath())
        self.tree = tree.getroot()
        return None

    def getTree(self):
        return self.tree

    def insertRecord(self, aliasVal, websiteVal, usernameVal, passwordVal):
        recordElement = ETREE.Element("Record")
        recordElement.set('name', aliasVal)
        recordElement.set('website', websiteVal)

        aliasElement = ETREE.SubElement(
            recordElement,  "Alias").text = str(aliasVal)

        websiteElement = ETREE.SubElement(
            recordElement,  "Website").text = str(websiteVal)

        usernameElement = ETREE.SubElement(
            recordElement,  "Username").text = str(usernameVal)

        passwordElement = ETREE.SubElement(
            recordElement,  "Password").text = str(passwordVal)

        self.tree.insert(1, recordElement)
        return

    def removeRecord(self, aliasVal, websiteVal):
        if aliasVal is not None:
            query = ".//Record[@name='{}']".format(str(aliasVal))
        if websiteVal is not None:
            query = ".//Record[@website='{}']".format(str(websiteVal))

        searchElement = self.tree.find(query)
        self.tree.remove(searchElement)
        return

    def dumpTree(self):
        tree = ETREE.dump(self.tree)
        print(tree)
        return

    def writeXML(self):
        tree = ETREE.ElementTree(self.tree)
        tree.write(self.path, xml_declaration=True,
                   encoding='utf-8', method="xml")
        return

    @staticmethod
    def toXML(jsonObj):
        xmlString = xmltodict.unparse(jsonObj, pretty=True)
        return xmlString

    @staticmethod
    def toJson(xmlString):
        jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
        return jsonString
