import json
DATAPATH = "animals_data.json"


def main():
  display_animal_informations()

def get_data():
  with open(DATAPATH, "r") as objfile:
    data = json.load(objfile)
  return data


def save_data(data):
  with open(DATAPATH, "w") as objfile:
    json.dump(data, objfile, indent=4)


def get_all_animal_data():
  data = get_data()
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


def display_animal_informations():
  animal_informations = get_all_animal_data()

  for animal in animal_informations:

    name = animal[0]
    diet = animal[1]
    location = animal[2]

    if len(animal) == 4:
      type = animal[3]
      print(f"Name: {name}\nDiet: {diet}\nLocation: {location}\nType: {type}\n")
    else:
      print(f"Name: {name}\nDiet: {diet}\nLocation: {location}\n")


if __name__ == "__main__":
  main()