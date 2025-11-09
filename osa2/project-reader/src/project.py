class Project:
    def __init__(self, name, authors, description, dependencies, dev_dependencies):
        self.name = name
        self.authors = authors
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        if len(dependencies) < 1:
            return "-"
        parsed = ""
        for dep in dependencies:
            parsed = parsed + "\n" + "- " +dep
        return parsed

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nAuthors: {self._stringify_dependencies(self.authors)}"
            f"\nDescription: {self.description or '-'}"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
