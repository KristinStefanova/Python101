import json
import xml.etree.ElementTree as ET
import ast


serializable_types = (
    int,
    float,
    str,
    list,
    dict,
    bool,
    type(None))


class Jsonable:
    def to_json_dict(self):
        class_name = self.__class__.__name__
        dict_ = {}

        for key, value in self.__dict__.items():
            if type(value) in serializable_types:
                dict_[key] = value
            elif isinstance(value, Jsonable):
                dict_[key] = value.to_json_dict()
            else:
                raise ValueError(f'{value} is not serializable!')

        return {"class_name": class_name, "dict": dict_}

    def to_json(self):
        return json.dumps(self.to_json_dict(), indent=4)

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        if json_dict['class_name'] != cls.__name__:
            raise ValueError
        obj = cls()
        for key, value in json_dict["dict"].items():
            if type(value) is not dict:
                setattr(obj, key, value)
            else:
                if "class_name" in value.keys():
                    class_name = value["class_name"]
                    sub = globals()[class_name].from_json(json.dumps(value))
                    setattr(obj, key, sub)
                else:
                    setattr(obj, key, value)
        return obj


class Xmlable:
    def to_xml_element(self):
        class_name = self.__class__.__name__
        root = ET.Element(class_name)

        for key, value in self.__dict__.items():
            if isinstance(value, Xmlable):
                sub = ET.Element(key)
                sub.append(value.to_xml_element())
                root.append(sub)
            elif type(value) in serializable_types:
                sub = ET.Element(key)
                sub.text = str(value)
                root.append(sub)
            else:
                raise ValueError(f'{value} is not serializable!')
        return root

    def to_xml(self):
        return ET.tostring(
            self.to_xml_element(), encoding='unicode')

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)
        if root.tag != cls.__name__:
            raise ValueError
        obj = cls()
        for child in root:
            if len(child.getchildren()) == 0:
                if child.text.isalpha():
                    if child.text == 'True':
                        setattr(obj, child.tag, True)
                    elif child.text == 'False':
                        setattr(obj, child.tag, False)
                    elif child.text == 'None':
                        setattr(obj, child.tag, None)
                    else:
                        setattr(obj, child.tag, child.text)
                else:
                    setattr(obj, child.tag, ast.literal_eval(child.text))
            else:
                for ch in child.getchildren():
                    sub = globals()[ch.tag].from_xml(
                        ET.tostring(ch, encoding='unicode'))
                    setattr(obj, child.tag, sub)
        return obj


class Tree(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Panda(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Person(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def main():
    tree = Tree(name="lavendar")
    pet = Panda(name="Timi", tree=tree)
    person = Person(name="Krisi", pet=pet, age={})

    json_str_person = person.to_json()
    xml_str_person = person.to_xml()

    print("XML string object:\n", xml_str_person)
    print("JSON string object:\n", json_str_person)

    from_json_person = Person.from_json(json_str_person)
    from_xml_person = Person.from_xml(xml_str_person)

    print(person == from_json_person)
    print(person == from_xml_person)

    print(from_json_person)
    print(from_xml_person)
    print(person)


if __name__ == '__main__':
    main()
