import json
JSON_DATAPATH = "animals_data.json"
HTML_DATAPATH = "animals_template.html"

def main():
  update_HTML_data()


def get_json_data():
  with open(JSON_DATAPATH, "r") as objfile:
    data = json.load(objfile)
  return data


def get_HTML_data():
  with open(HTML_DATAPATH, "r") as htmlfile:
    data = htmlfile.read()

    return data


def save_HTML_data(data):
  with open(HTML_DATAPATH, "w") as objfile:
    objfile.write(data)


def get_all_animal_data():
  data = get_json_data()
  all_animal_informations = []
  for animal in data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]

    try:
      animal_type = animal["characteristics"]["type"]
      animal_informations = [name, diet, location, animal_type]
      all_animal_informations.append(animal_informations)

    except KeyError:
      animal_informations = [name, diet, location]
      all_animal_informations.append(animal_informations)

  return all_animal_informations


def generate_animal_informations():
  animal_informations = get_all_animal_data()
  output = ""

  for animal in animal_informations:
    output += '<li class="cards__item">'
    name = animal[0]
    diet = animal[1]
    location = animal[2]

    if len(animal) == 4:
      type = animal[3]
      output += f"Name: {name}<br/>\nDiet: {diet}<br/>\nLocation: {location}<br/>\nType: {type}\n</li>\n\n"
    else:
      output += f"Name: {name}<br/>\nDiet: {diet}<br/>\nLocation: {location}\n</li>\n\n"

  return output


def update_HTML_data(old_data="__REPLACE_ANIMALS_INFO__"):
  html = get_HTML_data()
  animal_info = generate_animal_informations()

  html = html.replace(old_data, animal_info)

  save_HTML_data(html)



if __name__ == "__main__":
  main()