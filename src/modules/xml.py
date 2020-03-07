import json

import xmltodict


class XML:
    @staticmethod
    def toXML(jsonObj):
        xmlString = xmltodict.unparse(jsonObj, pretty=True)
        return xmlString

    @staticmethod
    def toJson(xmlString):
        jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
        return jsonString
