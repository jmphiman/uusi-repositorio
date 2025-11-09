from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_dict = tomli.loads(content)
        print(toml_dict)
        name = toml_dict["tool"]["poetry"]["name"]
        authors = toml_dict["tool"]["poetry"]["authors"]
        desc = toml_dict["tool"]["poetry"]["description"]
        dependencies = toml_dict["tool"]["poetry"]["dependencies"].keys()
        dev_dependencies = toml_dict["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()
        return Project(name, authors, desc, dependencies, dev_dependencies)
