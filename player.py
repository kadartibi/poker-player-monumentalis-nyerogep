class Player:
    VERSION = "0.4"

    def betRequest(self, game_state):
        cards_values_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 10, "10": 13, "J": 14,
                             "Q": 18, "K": 19, "A": 20}

        our_player = game_state["players"][game_state["in_action"]]

        first_card = our_player["hole_cards"][0]
        second_card = our_player["hole_cards"][1]
        community_cards = game_state["community_cards"]
        pair_in_hand = False

        color_counter = {"spades": 0, "hearts": 0, "clubs": 0, "diamonds": 0}

        # Check card distance before flop
        cards_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        difference = abs(cards_values.index(first_card["rank"]) - cards_values.index(second_card["rank"]))
        difference_modifiers = {1: 5, 2: 3, 3: 0, 4: -1, 5: -3, 6: -5}
        card_difference = difference_modifiers[difference] if 0 < difference < 7 else -10

        # Check card color
        color_value_modifier = 3 if first_card["suit"] == second_card["suit"] else 0

        total_card_value = cards_values_dict[first_card["rank"]] + cards_values_dict[
            second_card["rank"]] + card_difference + color_value_modifier

        # if len(community_cards) == 0 or len(community_cards) == 4 or len(community_cards) == 5:
        if first_card["rank"] == second_card["rank"]:
            pair_in_hand = True
            if first_card["rank"] in ["Q", "K", "A"]:
                return game_state["current_buy_in"] - our_player["bet"] + game_state["minimum_raise"]
            return game_state["current_buy_in"] - our_player["bet"]

        if total_card_value >= 30:
            return game_state["current_buy_in"] - our_player["bet"]

        # Check after flop
        # if len(community_cards) == 3:
        #     highest_card_value_on_table = 0
        #     color_counter[first_card["rank"]] += 1
        #     color_counter[second_card["rank"]] += 1
        #     for card in community_cards:
        #         if cards_values_dict[card["rank"]] > highest_card_value_on_table:
        #             highest_card_value_on_table = cards_values_dict[card["rank"]]
        #         color_counter[card["rank"]] += 1
        #         if first_card["rank"] == card["rank"] or second_card["rank"] == card["rank"] or pair_in_hand:
        #             return game_state["current_buy_in"] - our_player["bet"]
        #
        #     if cards_values_dict[first_card["rank"]] > highest_card_value_on_table or \
        #             cards_values_dict[second_card["rank"]] > highest_card_value_on_table:
        #         return game_state["current_buy_in"] - our_player["bet"]
        #
        #     for color_number in color_counter.values():
        #         if color_number >= 4:
        #             return game_state["current_buy_in"] - our_player["bet"]

        return 0

    def showdown(self, game_state):
        pass
