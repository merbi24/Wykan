from . import _WekanObject


class Card(_WekanObject):
    """
    Wekan Card
    """

    def __init__(self, api, board_id, list_id, id: str):
        super().__init__(api, id)
        self.boardId = board_id
        self.listId = list_id
        _data = self._api.get(f"/api/boards/{self.boardId}/lists/{self.listId}/cards/{self.id}")

        self.title = _data.get("title")
        self.description = _data.get("description")
