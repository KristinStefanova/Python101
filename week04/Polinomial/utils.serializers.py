import json
import xml.etree.ElementTree


class JsonableMixin:
    def to_json(indent=4):
        print(locals())

    @classmethod
    def from_json(json_string):
        pass


class XmlableMixin:
    def to_xml():
        pass

    @classmethod
    def from_xml(json_string):
        pass


class Panda(JsonableMixin, XmlableMixin):
    def __init__(self, name):
        self.name = name


def main():
    p = Panda("Krisi")
    p.to_json


if __name__ == '__main__':
    main()
