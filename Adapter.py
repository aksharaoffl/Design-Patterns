import xml.etree.ElementTree as ET
import json

class DataProvider:
    def get_data(self):
        raise NotImplementedError


# Adaptee (incompatible: produces XML)
class XMLDataProvider:
    def get_xml_data(self):
        return """<person>
                    <name>Divu</name>
                    <age>7</age>
                  </person>"""


# Adapter (wraps XMLDataProvider and converts to JSON/dict)
class XMLtoJSONAdapter(DataProvider):
    def __init__(self, xml_provider: XMLDataProvider):
        self.xml_provider = xml_provider

    def get_data(self):
        xml_string = self.xml_provider.get_xml_data()
        root = ET.fromstring(xml_string)

        data = {child.tag: child.text for child in root}

        return data

def client_code(provider: DataProvider):
    data = provider.get_data()
    print("converted json data :", json.dumps(data))



if __name__ == "__main__":
    xml_provider = XMLDataProvider()
    adapter = XMLtoJSONAdapter(xml_provider)

    client_code(adapter)



