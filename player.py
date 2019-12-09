
class Player:
    VERSION = "0.2"

    def betRequest(self, game_state):
        players = game_state["players"]
        our_id = game_state["in_action"]
        our_player = players[our_id]
        first_card = our_player["hole_cards"][0]
        second_card = our_player["hole_cards"][1]
        if first_card["rank"] == second_card["rank"]:
            return game_state["current_buy_in"] - our_player["bet"]

        return 0

    def showdown(self, game_state):
        pass

