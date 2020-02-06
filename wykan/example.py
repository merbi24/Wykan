import yaml

from wykan import Wykan

if __name__ == '__main__':
    with open("example_config.yml", "rb") as fd:
        config = yaml.load(fd)

    wekan_url = "http://localhost/"
    username = "admin"
    password = "Password1"
    Wykan.verify_tls = False
    wekan = Wykan(wekan_url, username, password)

    user = wekan.get_user_by_username('admin')
    wekan.create_board_from_configuration(config, user.id)

    board = wekan.get_board_by_title(user.id, config.title)
    wekan.duplicate_board(board, "dup test")
