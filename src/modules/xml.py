import json
import xmltodict
import xml.etree.cElementTree as ET

class XML:

    def toXML(jsonString):
        xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)
        return xmlString


    def toJson(xmlString):
        jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
        return jsonString

        
