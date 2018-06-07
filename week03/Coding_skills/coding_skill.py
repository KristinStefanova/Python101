import sys
import json


def read_json_file(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)

    return data


def get_languages(data):
    languages = {}
    for person in data["people"]:
        for skill in person["skills"]:
            languages[skill["name"]] = skill["level"]
    return languages


def get_hight_scored_languages(data):
    languages = get_languages(data)
    for name, level in languages.items():
        for person in data["people"]:
            for skill in person["skills"]:
                if skill["name"] == name:
                    if skill["level"] > languages[name]:
                        languages[name] = skill["level"]
    return languages


def coding_skills(data):
    languages = get_hight_scored_languages(data)
    for name, level in languages.items():
        for person in data["people"]:
            for skill in person["skills"]:
                if skill["name"] == name and skill["level"] == level:
                    languages[name] = f'{person["first_name"]} {person["last_name"]}'
    return languages


def people_by_languages(lang):
    result = []
    for lang, name in lang.items():
        result.append(f'{lang} - {name}\n')
    return "".join(result)


def main():
    print(people_by_languages(coding_skills(read_json_file(sys.argv[1]))))


if __name__ == '__main__':
    main()
