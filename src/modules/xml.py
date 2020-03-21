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

    def insert_element_to_tree(self, element):
        self.tree.insert(1, element)
        return self.tree

    def remove_record(self, element):
        self.tree.remove(element)
        return

    def find_record(self, query):
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

    @staticmethod
    def create_element(element_name):
        element = ETREE.Element(element_name)
        return element

    @staticmethod
    def create_sub_element(element, child_element):
        sub_element = ETREE.SubElement(element, child_element)
        return sub_element

    @staticmethod
    def set_element_text(element, value):
        element.text = str(value)
        return element
    
    @staticmethod
    def set_element_attr(element, attribute, value):
        element.set(attribute, value)
        return element