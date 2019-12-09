
class Player:
    VERSION = "0.2"

    def betRequest(self, game_state):
        our_id = game_state["in_action"]
        bet = game_state["current_buy_in"]
        for player in game_state["players"]:
            if player["id"] == our_id:
                our_player = player["id"]
                if our_player["hole_cards"][0]["rank"] == our_player["hole_cards"][1]["rank"]:
                    return bet - our_player["bet"] + game_state["minimum_raise"]
        return 0

    def showdown(self, game_state):
        pass

