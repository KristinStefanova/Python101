import sys
import json


def read_json_file(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)

    return data


def generate_head(person):
    return f"""<head>
    <title>{person["first_name"]} {person["last_name"]}</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    </head>"""


def generete_base_info(person):
    return f"""<div class="base-info">
    <p>Age: {person["age"]}</p>
    <p>Birth date: {person["birth_date"]}</p>
    <p>Birth place: {person["birth_place"]}</p>
    <p>Gender: {person["gender"]}</p>
    </div>"""


def generate_interests(person_interests):
    return """<div class="interests">
    <h2>Interests:</h2>
    <ul> {0} </ul>
    </div>""".format(
        "".join([f'<li>{interest}</li>\n' for interest in person_interests]))


def generate_skills(person_skills):
    return """<div class="skills">
    <h2>Skills:</h2>
    <ul>{0}</ul>
    </div>""".format(
        "".join([f'<li>{skill["name"]} - {skill["level"]}</li>\n'
                 for skill in person_skills]))


def generate_body(person):
    return f"""<body>
    <div class="business-card male">
    <h1 class="full-name">{person["first_name"]} {person["last_name"]}</h1>
    <img class="avatar" src="avatars/{person["avatar"]}">
    {generete_base_info(person)}
    {generate_interests(person["interests"])}
    {generate_skills(person["skills"])}
    </div>
    </body>"""


def generate_html(person):
    return f"""<!DOCTYPE html>
    <html>
    {generate_head(person)}
    {generate_body(person)}
    </html>"""


def all_person_htmls(file_name):
    people = read_json_file(file_name)
    html_list = []
    for person in people["people"]:
        htmlname = f'{person["first_name"].lower()}_{person["last_name"].lower()}.html'
        with open(htmlname, "w") as f:
            f.write(generate_html(person))
        html_list.append(htmlname)
    return html_list


def main(file_name):
    return all_person_htmls(file_name)


if __name__ == '__main__':
    file_name = sys.argv[1]
    main(file_name)
