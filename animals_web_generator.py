import json
JSON_DATAPATH = "./animals_data.json"
HTML_DATAPATH = "./animals_output.html"


def main():
  create_new_html_file()


def get_json_data():
  with open(JSON_DATAPATH, "r") as objfile:
    data = json.load(objfile)
  return data


def save_HTML_data(data):
  with open(HTML_DATAPATH, "w") as objfile:
    objfile.write(data)


def get_all_animal_data():
  """Gets needed information from JSON file and puts it - for each animal - in a list of lists"""
  data = get_json_data()
  all_animal_informations = []
  for animal in data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]

    try:
      animal_type = animal["characteristics"]["type"]
      animal_informations = [name, diet, location, animal_type]
    except KeyError:
      animal_informations = [name, diet, location]

    all_animal_informations.append(animal_informations)

  return all_animal_informations


def generate_animal_informations():
  """Generates HTML code for each animal"""
  animal_informations = get_all_animal_data()
  output = ""

  for animal in animal_informations:
    output += "<li class='cards__item'>"
    name = animal[0]
    diet = animal[1]
    location = animal[2]

    output += f"<div class='card__title'>{name}</div>\n"
    output += f"<p class='card__text'>\n<strong>Diet:</strong> {diet}<br/>\n"
    output += f"<strong>Location:</strong> {location}<br/>\n"

    if len(animal) == 4:
      animal_type = animal[3]
      output += f"<strong>Type:</strong> {animal_type}<br/>\n"

    output += "</p>\n</li>\n"

  return output


def create_new_html_file():
  """Creates a new HTML file with the animal information"""
  html_template = """
    <html>
    <head>
        <style>
        html {
          background-color: #ffe9e9;
        }

        h1 {
            text-align: center;
            font-size: 40pt;
            font-weight: normal;
        }

        body {
          font-family: 'Roboto','Helvetica Neue', Helvetica, Arial, sans-serif;
          font-style: normal;
          font-weight: 400;
          letter-spacing: 0;
          padding: 1rem;
          text-rendering: optimizeLegibility;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
          -moz-font-feature-settings: "liga" on;
          width: 900px;
          margin: auto;
        }

        .cards {
          list-style: none;
          margin: 0;
          padding: 0;
        }

        .cards__item {
          background-color: white;
          border-radius: 0.25rem;
          box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
          overflow: hidden;
          padding: 1rem;
          margin: 50px;
        }

        .card__title {
          color: #696969;
          font-size: 1.25rem;
          font-weight: 300;
          letter-spacing: 2px;
          text-transform: uppercase;
        }

        .card__text {
          flex: 1 1 auto;
          font-size: 0.95rem;
          line-height: 2;
          margin-bottom: 1.25rem;
        }
        </style>
    </head>
    <body>
        <h1>My Animal Repository</h1>
        <ul class="cards">
            __REPLACE_ANIMALS_INFO__
        </ul>
    </body>
    </html>
    """

  animal_info = generate_animal_informations()
  html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info)
  save_HTML_data(html_content)


if __name__ == "__main__":
  main()
