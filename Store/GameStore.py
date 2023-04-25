class GameStore:
    name: str
    playerNumber: int
    enemy_name: str = ""
    is_your_tour: bool = False
    game_phase: str = ""
    player_board = []
    player_hit = []
    enemy_hit = []

    @staticmethod
    def set_game_data(data):
        GameStore.name = data['name']
        GameStore.game_phase = data['game_phase']
        GameStore.player_board = data["player_board"]
        GameStore.player_hit = data['player_hit']
        GameStore.enemy_hit = data["enemy_hit"]
        GameStore.enemy_name = data["enemy_name"]
