import argparse
import os
import dbm
from os.path import expanduser
from gordon.card_manager import load_review_cards, promote_card, demote_card

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("card_file", help="The text file of the deck.")
    parser.add_argument("-r", "--reverse", help="Reverse question.", action="store_true")
    parser.add_argument("-s", "--spaced", help="Run Leitner algorithm.", action="store_true")
    args = parser.parse_args()

    if not os.path.isfile(args.card_file):
        print("Unable to find that card file.")
        exit(1)

    filename = os.path.basename(args.card_file);

    home = expanduser("~")
    if not os.path.isdir(home + "/.config/gordon"):
        os.makedirs(home + "/.config/gordon")

    with dbm.open(home + "/.config/gordon/" + filename + ".data", "c") as db:
        reviewCards = load_review_cards(db, args.card_file, args.spaced, args.reverse)

        for card in reviewCards:
            os.system('clear')
            print(card[0])
            if input("answer: ") == card[1]:
                promote_card(db, card)
                print("That is correct.")
            else:
                demote_card(db, card)
                print("The correct answer is: ", card[1])
            input("Press Enter to continue...")

        print("That concludes this deck.  Have a big one.")
