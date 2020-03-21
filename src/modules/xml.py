import json
import xml.etree.ElementTree as ETREE

from src.modules.file import File


class XML:
    path = "credentials.xml"
    tree = None

    def __init__(self):
        fp = File(self.path)
        tree = ETREE.parse(fp.getPath())
        self.tree = tree.getroot()
        return None

    def get_tree(self):
        return self.tree

    def insert_record(self, alias_val, website_val, username_val, password_val):
        record_element = ETREE.Element("Record")
        record_element.set("name", alias_val)
        record_element.set("website", website_val)

        aliasElement = ETREE.SubElement(record_element, "Alias").text = str(
            alias_val)

        websiteElement = ETREE.SubElement(record_element, "Website").text = str(
            website_val)

        usernameElement = ETREE.SubElement(record_element, "Username").text = str(
            username_val)

        passwordElement = ETREE.SubElement(record_element, "Password").text = str(
            password_val)

        self.tree.insert(1, record_element)
        return

    def remove_record(self, alias_val, website_val):
        element = self.find_record(alias_val, website_val)
        self.tree.remove(element)
        return

    def find_record(self, alias_val, website_val):
        if alias_val is not None:
            query = f".//Record[@name='{str(alias_val)}']"
        if website_val is not None:
            query = f".//Record[@website='{str(website_val)}']"

        element = self.tree.find(query)
        return element

    def dump_tree(self):
        tree = ETREE.dump(self.tree)
        print(tree)
        return

    def write_xml(self):
        tree = ETREE.ElementTree(self.tree)
        tree.write(self.path, xml_declaration=True, encoding="utf-8", method="xml")
        return
