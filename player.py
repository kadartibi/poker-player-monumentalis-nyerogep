class Player:
    VERSION = "0.3"

    def betRequest(self, game_state):
        cards_values_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 12, "10": 13, "J": 14,
                             "Q": 18, "K": 19, "A": 20}

        cards_values = ({"2": 2},
                        {"3": 3},
                        {"4": 4},
                        {"5": 5},
                        {"6": 6},
                        {"7": 7},
                        {"8": 8},
                        {"9": 12},
                        {"10": 13},
                        {"J": 14},
                        {"Q": 18},
                        {"K": 19},
                        {"A": 20},)

        our_player = game_state["players"][game_state["in_action"]]

        first_card = our_player["hole_cards"][0]
        second_card = our_player["hole_cards"][1]
        total_card_value = cards_values_dict[first_card["rank"]] + cards_values_dict[second_card["rank"]]

        if first_card["rank"] == second_card["rank"]:
            return game_state["current_buy_in"] - our_player["bet"]

        if total_card_value >= 30:
            return game_state["current_buy_in"] - our_player["bet"]

        return 0

    def showdown(self, game_state):
        pass
