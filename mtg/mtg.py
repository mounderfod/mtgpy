import sys
import json
import requests

def main():
    try:
        sys.argv.pop(0)
        string = "+".join(sys.argv)
        final_string = string.lower()
        if not sys.argv:
            raise IndexError
    except IndexError:
        print("A card name was not passed. Try again.")
        exit()

    url = "https://api.scryfall.com/cards/named?fuzzy=" + final_string
    data = json.loads(requests.get(url).text)
    if data["object"] == "error":
        print("An error occurred! " + data["details"])

    else:
        print("")
        print("Name: " + data["name"])
        print("Type: " + data["type_line"])
        print("Mana Cost: " + data["mana_cost"])
        print("Text: " + data["oracle_text"])
        print("")
        print("Rarity: " + data["rarity"].title())
        print("Card Prices: (there may be none of these)")
        try:
            print("USD: $" + data["prices"]["usd"])
        except:
            pass
        try:
            print("USD (Foil): $" + data["prices"]["usd_foil"])
        except:
            pass
        try:
            print("EUR: €" + data["prices"]["eur"])
        except:
            pass
        try:
            print("EUR (Foil): €" + data["prices"]["eur_foil"])
        except:
            pass
        try:
            print("Tix: " + data["prices"]["tix"])
        except:
            pass
        print("")
        if not "Token" in data["type_line"]:
            print("Legality:")
            print("Standard: " + data["legalities"]["standard"].title().replace("_", " "))
            print("Future: " + data["legalities"]["future"].title().replace("_", " "))
            print("Historic: " + data["legalities"]["historic"].title().replace("_", " "))
            print("Gladiator: " + data["legalities"]["gladiator"].title().replace("_", " "))
            print("Pioneer: " + data["legalities"]["pioneer"].title().replace("_", " "))
            print("Modern: " + data["legalities"]["modern"].title().replace("_", " "))
            print("Legacy: " + data["legalities"]["legacy"].title().replace("_", " "))
            print("Pauper: " + data["legalities"]["pauper"].title().replace("_", " "))
            print("Vintage: " + data["legalities"]["vintage"].title().replace("_", " "))
            print("Penny: " + data["legalities"]["penny"].title().replace("_", " "))
            print("Commander: " + data["legalities"]["commander"].title().replace("_", " "))
            print("Brawl: " + data["legalities"]["brawl"].title().replace("_", " "))
            print("Duel: " + data["legalities"]["duel"].title().replace("_", " "))
            print("Old School: " + data["legalities"]["oldschool"].title().replace("_", " "))
            print("Pre-Modern: " + data["legalities"]["premodern"].title().replace("_", " "))
        

