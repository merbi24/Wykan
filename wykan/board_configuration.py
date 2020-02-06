import yaml


class CardConfiguration(yaml.YAMLObject):
    yaml_tag = "!CardConfiguration"

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description


class ListConfiguration(yaml.YAMLObject):
    yaml_tag = "!ListConfiguration"

    def __init__(self, title: str, cards: [CardConfiguration]):
        self.title = title
        self.cards = cards


class BoardConfiguration(yaml.YAMLObject):
    yaml_tag = "!BoardConfiguration"

    def __init__(self, title: str, lists: [ListConfiguration]):
        self.title = title
        self.lists = lists
