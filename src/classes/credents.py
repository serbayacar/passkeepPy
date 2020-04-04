from src.modules.xml import XML
from src.modules.table import Table

class Credentials():
    alias : None
    website : None
    xmlTree : None

    def __init__(self, alias_value, website_value):
        self.alias = alias_value
        self.website = website_value
        self.xmlTree = XML()

    def isDuplicate(self, alias_value, website_value):
        element = self.find_record(alias_value, website_value)
        return True if element is not None else False

    def find_record(self, alias_val, website_val):
        if alias_val is not None:
            query = f".//Record[@name='{str(alias_val)}']"
        if website_val is not None:
            query = f".//Record[@website='{str(website_val)}']"
        element = self.xmlTree.find_record(query)
        return element

    def insert_record(self, alias_val, website_val, username_val, password_val):
        if self.isDuplicate(alias_val, website_val) is True :
            raise Warning('Credentials you want to keep are duplicate')
            
        record_element = XML.create_element('Record')
        XML.set_element_attr(record_element, 'name', alias_val)
        XML.set_element_attr(record_element, 'website', website_val)

        alias_element = XML.create_sub_element(record_element, 'Alias')
        XML.set_element_text(alias_element, alias_val)

        website_element = XML.create_sub_element(record_element, 'Website')
        XML.set_element_text(website_element, website_val)

        username_element = XML.create_sub_element(record_element, 'Username')
        XML.set_element_text(username_element, username_val)

        password_element = XML.create_sub_element(record_element, 'Password')
        XML.set_element_text(password_element, password_val)

        self.xmlTree.insert_element_to_tree(record_element)
        self.xmlTree.write_xml()
        return True

    def remove_record(self, alias_val, website_val):
        if self.isDuplicate(alias_val, website_val) is False :
            raise Warning('Credentials you want to remove are not exist')

        element = self.find_record(alias_val, website_val)
        tree = self.xmlTree.remove_record(element)
        self.xmlTree.write_xml()
        return True

    def show(self, element):
        if element is not None:
            alias_text = element.find("Alias").text
            website_text = element.find("Website").text
            username_text = element.find("Username").text
            password_text = element.find("Password").text

            headers = ['Alias', 'Website', 'Username', 'Password']
            texts = [ alias_text, website_text, username_text, password_text ]
            Table.createTable(texts, headers)
        else:
            raise Warning("Credentials you want to show is not found!")


