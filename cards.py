import os
import pytest
import requests

def handle_request_error(error_type, function_name, error):
    print(f"Error in {function_name}: {error_type} - {error}")

def make_api_request(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as err:
        handle_request_error(type(err).__name__, "make_api_request", err)
        return None

@pytest.fixture
def shuffled_deck_id():
    # Make the API request to get a shuffled deck
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = make_api_request(url)

    if response:
        # Join the letters to form a single string
        deck_id = ''.join(response.json()['deck_id'])

        # Print the shuffled deck ID
        print("")
        print(f"Shuffled Deck ID: {deck_id}")

        return deck_id
    else:
        return None

def test_draw_cards(shuffled_deck_id):
    # Example of using shuffled_deck_id in a test
    if shuffled_deck_id is not None:
        url = f"https://deckofcardsapi.com/api/deck/{shuffled_deck_id}/draw/?count=5"
        response = make_api_request(url)

        if response:
            # Print the draw cards response
            print(f"Draw Cards Response for Deck ID {shuffled_deck_id}:")
            print(response.json())

            # Check the content of the response
            data = response.json()

            # Assert the presence of keys and their data types
            assert "success" in data and isinstance(data["success"], bool)
            assert "deck_id" in data and data["deck_id"] == shuffled_deck_id

            assert "cards" in data and isinstance(data["cards"], list)
            assert len(data["cards"]) == 5

            for card in data["cards"]:
                assert "code" in card and isinstance(card["code"], str)
                assert "image" in card and isinstance(card["image"], str)
                assert "images" in card and isinstance(card["images"], dict)
                assert "value" in card and isinstance(card["value"], str)
                assert "suit" in card and isinstance(card["suit"], str)

                images = card["images"]
                assert "svg" in images and isinstance(images["svg"], str)
                assert "png" in images and isinstance(images["png"], str)

            assert "remaining" in data and isinstance(data["remaining"], int)

def test_pile_cards(shuffled_deck_id, data):
    # Example of using shuffled_deck_id in a test
    if shuffled_deck_id is not None:
        drawn_cards = ",".join([card["code"] for card in data["cards"] if "code" in card and isinstance(card["code"], str)])

        url = f"https://deckofcardsapi.com/api/deck/{shuffled_deck_id}/pile/emma/add/?cards=AS,2S"
        # url = f"https://deckofcardsapi.com/api/deck/{shuffled_deck_id}/pile/MYPILE/add/?cards=${drawncards}"
        response = make_api_request(url)

        # if response:
        #     # Print the draw cards response
        #     print(f"Draw Cards Response for Deck ID {shuffled_deck_id}:")
        #     print(response.json())

        #     # Check the content of the response
        #     data = response.json()

        #     # Assert the presence of keys and their data types
        #     assert "success" in data and isinstance(data["success"], bool)
        #     assert "deck_id" in data and data["deck_id"] == shuffled_deck_id

        #     assert "cards" in data and isinstance(data["cards"], list)
        #     assert len(data["cards"]) == 2



            # assert "remaining" in data and isinstance(data["remaining"], int)
            ####shuffle deck 5 cards out
# Shuffled a new deck.x
#Draw 5 cards x
#Add these cards to a pile
#Draw 5 more cards from the same deck
#Add to a different pile
#print out all the cards from both piles.