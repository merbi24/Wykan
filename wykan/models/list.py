from wykan.models.card import Card
from . import _WekanObject
from .colors import Colors


class List(_WekanObject):
    """
    Wekan List
    """

    def __init__(self, api, board_id, list_id: str):
        super().__init__(api, list_id)
        _list = self._api.get(f"/api/boards/{board_id}/lists/{list_id}")

        self.title = _list.get("title")
        self.starred = _list.get("starred")
        self.archived = _list.get("archived")
        self.boardId = board_id
        self.swimlaneId = _list.get("swimlaneId")
        self.createdAt = _list.get("createdAt")
        self.sort = _list.get("sort")
        self.updatedAt = _list.get("updatedAt")
        self.modifiedAt = _list.get("modifiedAt")
        self.wipLimit = _list.get("wipLimit")
        self.color = Colors[_list.get("color")] if _list.get("color") else None
        self.type = _list.get("type")

    def create_card(self, title: str, description: str) -> Card:
        """
        Add a card to the list
        :param title: Title of the card to add.
        :return:
        """

        board = self._api.get_board(self.boardId)

        card_data = {
            "title": title,
            "description": description,
            "authorId": board.get_admin_users()[0].id,
            "swimlaneId": board.get_swimlanes()[0].id,
        }

        new_card = self._api.post(f"/api/boards/{self.boardId}/lists/{self.id}/cards", card_data)

        return Card(self._api, self.boardId, self.id, new_card["_id"])

    def get_cards(self) -> [Card]:
        """
        Get the list of all cards in this list
        :return:
        """

        cards_data = self._api.get(f"/api/boards/{self.boardId}/lists/{self.id}/cards")
        if len(cards_data) <= 0:
            raise LookupError(f"Could not find cards in list {self.title}")

        return [Card(self._api, self.boardId, self.id, card['_id']) for card in cards_data]
