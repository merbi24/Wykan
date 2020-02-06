from . import _WekanObject


class Swimlane(_WekanObject):
    def __init__(self, api, board_id, id: str):
        super().__init__(api, id)
        _data = api.get(f"/api/boards/{board_id}/swimlanes/{id}")

        self.title = _data.get('title')
        self.boardId = board_id
        self.archived = _data.get('archived')
        self.createdAt = _data.get('createdAt')
        self.updatedAt = _data.get('updatedAt')
        self.modifiedAt = _data.get('modifiedAt')
        self.type = _data.get('type')
        self.sort = _data.get('sort')
