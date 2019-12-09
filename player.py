class Player:
    VERSION = "0.3"

    def betRequest(self, game_state):
        cards_values_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 10, "10": 13, "J": 14,
                             "Q": 18, "K": 19, "A": 20}

        our_player = game_state["players"][game_state["in_action"]]

        first_card = our_player["hole_cards"][0]
        second_card = our_player["hole_cards"][1]
        card_difference = card_distance(first_card, second_card)
        total_card_value = cards_values_dict[first_card["rank"]] + cards_values_dict[second_card["rank"]]
                           #+ card_difference + check_card_color(first_card, second_card)

        if first_card["rank"] == second_card["rank"] or total_card_value >= 30:
            return game_state["current_buy_in"] - our_player["bet"]

        return 0

    def showdown(self, game_state):
        pass


def card_distance(card_one, card_two):
    cards_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    difference = abs(cards_values.index(card_one["rank"]) - cards_values.index(card_two["rank"]))
    difference_modifiers = {1: 5, 2: 3, 3: 0, 4: -1, 5: -3, 6: -5}
    return difference_modifiers[difference] if difference < 7 else -10


def check_card_color(card_one, card_two):
    return 3 if card_one["suit"] == card_two["suit"] else 0
