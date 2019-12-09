
class Player:
    VERSION = "0.2"

    def betRequest(self, game_state):
        for element in game_state:
            if element == "players":
                for player in element:
                    if player["id"] == game_state["in_action"]:
                        if player["hole_cards"][0]["rank"] == player["hole_cards"][1]["rank"]:
                            return game_state["current_buy_in"] - player["bet"] + game_state["minimum_raise"]
        return 0

    def showdown(self, game_state):
        pass

