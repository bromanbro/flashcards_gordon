from random import shuffle

def process_line(line, reverse):
    return line.strip().split('###')[::-1] if reverse else line.strip().split('###')

def get_cards_at_level(cards, db, level):
    return list(filter(lambda card: (card[0] not in db.keys() and level == 0) or (card[0] in db.keys() and int(db[card[0]]) == level), cards))

def promote_card(db, card):
    if not card[0] in db.keys():
        db[card[0]] = "1";
    elif int(db[card[0]]) < 3:
        db[card[0]] = str(int(db[card[0]]) + 1)

def demote_card(db, card):
    if not card[0] in db.keys():
        db[card[0]] = "0";
    elif int(db[card[0]]) > 0:
        db[card[0]] = str(int(db[card[0]]) - 1)

def load_review_cards(db, card_file_name, spaced, reverse):
    with open(card_file_name) as f:
        card_list = [tuple(process_line(i, reverse)) for i in f]
        shuffle(card_list)

        if not spaced:
            return card_list

        if len(card_list) < 20:
            print('You must have at least 20 cards for spaced iteration.')
            exit(1)

        review_cards = []
        desired_cards = round(len(card_list) * .33);
        desired_at_level = [round(desired_cards * .48), round(desired_cards * .27), round(desired_cards * .17), round(desired_cards * .08)]
        for level in range(4):
            current_level = level
            while desired_at_level[level] > 0 and current_level <= 3:
                cards_at_level = get_cards_at_level(card_list, db, current_level)
                while len(cards_at_level) > 0 and desired_at_level[level] > 0:
                    card = cards_at_level.pop(0)
                    review_cards.append(card)
                    card_list.remove(card)
                    desired_at_level[level] -= 1
                current_level += 1

        while len(review_cards) < desired_cards and len(card_list) > 0:
            review_cards.append(card_list.pop(0))

        return review_cards
