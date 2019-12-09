
class Player:
    VERSION = "0.2"

    def betRequest(self, game_state):
        our_id = game_state["in_action"]
        our_player = game_state["players"]["our_id"]
        bet = game_state["current_buy_in"]
        if our_player["hole_cards"][0]["rank"] == our_player["hole_cards"][1]["rank"]:
            return game_state["minimum_raise"]
        return 0

    def showdown(self, game_state):
        pass

