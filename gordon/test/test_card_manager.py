import pytest
from gordon.card_manager import *

@pytest.fixture
def simple_db():
    db = {
        "question1": "0",
        "question2": "1",
        "question3": "1",
        "answer1": "0",
        "answer2": "0",
        "answer3": "0"
    }
    return db

@pytest.fixture
def complex_db():
    db = {
        "question1": "0",
        "question2": "0",
        "question3": "0",
        "question4": "0",
        "question5": "0",
        "question6": "0",
        "question7": "1",
        "question8": "1",
        "question9": "1",
        "question10": "1",
        "question11": "1",
        "question12": "2",
        "question13": "2",
        "question14": "2",
        "question15": "2",
        "question16": "3",
        "question17": "3",
        "question18": "3",
        "question19": "3",
        "question20": "3",
        "answer1": "0",
        "answer2": "0",
        "answer3": "0",
        "answer4": "0",
        "answer5": "0",
        "answer6": "0",
        "answer7": "1",
        "answer8": "1",
        "answer9": "1",
        "answer10": "1",
        "answer11": "1",
        "answer12": "2",
        "answer13": "2",
        "answer14": "2",
        "answer15": "2",
        "answer16": "3",
        "answer17": "3",
        "answer18": "3",
        "answer19": "3",
        "answer20": "3"
    }
    return db

@pytest.fixture
def deficient_db():
    db = {
        "question4": "0",
        "question5": "0",
        "question6": "0",
        "question7": "0",
        "question8": "0",
        "question9": "0",
        "question10": "0",
        "question11": "0",
        "question12": "2",
        "question13": "2",
        "question14": "2",
        "question15": "2",
        "question16": "3",
        "question17": "3",
        "question18": "3",
        "question19": "3",
        "question20": "3"
    }
    return db

@pytest.fixture
def all_trained_db():
    db = {
        "question4": "4",
        "question5": "4",
        "question6": "4",
        "question7": "4",
        "question8": "4",
        "question9": "4",
        "question10": "4",
        "question11": "4",
        "question12": "4",
        "question13": "4",
        "question14": "4",
        "question15": "4",
        "question16": "4",
        "question17": "4",
        "question18": "4",
        "question19": "4",
        "question20": "4"
    }
    return db

def fake_shuffle(list):
    return list

def test_load_review_cards(simple_db, mocker):
    mocker.patch("gordon.card_manager.shuffle", fake_shuffle)
    cards = load_review_cards(simple_db, "gordon/test/test_files/small.dek", False, False)
    assert len(cards) == 3
    assert cards[0][0] == "question1"
    assert cards[1][0] == "question2"
    assert cards[2][0] == "question3"
    assert cards[0][1] == "answer1"
    assert cards[1][1] == "answer2"
    assert cards[2][1] == "answer3"

def test_load_review_cards_reversed(simple_db, mocker):
    mocker.patch("gordon.card_manager.shuffle", fake_shuffle)
    cards = load_review_cards(simple_db, "gordon/test/test_files/small.dek", False, True)
    assert len(cards) == 3
    assert cards[0][0] == "answer1"
    assert cards[1][0] == "answer2"
    assert cards[2][0] == "answer3"
    assert cards[0][1] == "question1"
    assert cards[1][1] == "question2"
    assert cards[2][1] == "question3"

def test_get_cards_at_level(simple_db):
    cards = [
        ("question1", "answer1"),
        ("question2", "answer2"),
        ("question3", "answer3")
    ]
    result = get_cards_at_level(cards, simple_db, 1)
    assert len(result) == 2
    assert result[0] == cards[1]
    assert result[1] == cards[2]

def test_get_cards_at_level_handles_empty_db():
    cards = [
        ("question1", "answer1"),
        ("question2", "answer2"),
        ("question3", "answer3")
    ]
    result = get_cards_at_level(cards, {}, 1)
    assert len(result) == 0

def test_get_cards_at_level_treats_missing_as_level_zero():
    cards = [
        ("question1", "answer1"),
        ("question2", "answer2"),
        ("question3", "answer3")
    ]
    result = get_cards_at_level(cards, {}, 0)
    assert len(result) == 3

def test_load_review_cards_spaced(complex_db, mocker):
    mocker.patch("gordon.card_manager.shuffle", fake_shuffle)
    cards = load_review_cards(complex_db, "gordon/test/test_files/big.dek", True, False)
    assert len(cards) == 7 #Roughly 1/3 of the total deck
    #3 cards at level 0
    assert cards[0][0] == "question1"
    assert cards[1][0] == "question2"
    assert cards[2][0] == "question3"
    #2 cards at level 1
    assert cards[3][0] == "question7"
    assert cards[4][0] == "question8"
    #1 card at level 2
    assert cards[5][0] == "question12"
    #1 card at level 3
    assert cards[6][0] == "question16"

def test_load_review_cards_spaced_reversed(complex_db, mocker):
    mocker.patch("gordon.card_manager.shuffle", fake_shuffle)
    cards = load_review_cards(complex_db, "gordon/test/test_files/big.dek", True, True)
    assert len(cards) == 7 #Roughly 1/3 of the total deck
    #3 cards at level 0
    assert cards[0][0] == "answer1"
    assert cards[1][0] == "answer2"
    assert cards[2][0] == "answer3"
    #2 cards at level 1
    assert cards[3][0] == "answer7"
    assert cards[4][0] == "answer8"
    #1 card at level 2
    assert cards[5][0] == "answer12"
    #1 card at level 3
    assert cards[6][0] == "answer16"

def test_load_review_cards_spaced_treats_missing_in_db_as_level_zero(deficient_db, mocker):
    mocker.patch("gordon.card_manager.shuffle", fake_shuffle)
    cards = load_review_cards(deficient_db, "gordon/test/test_files/big.dek", True, False)
    #3 cards at level 0
    assert cards[0][0] == "question1"
    assert cards[1][0] == "question2"
    assert cards[2][0] == "question3"

def test_load_review_cards_spaced_loads_from_next_tier(deficient_db, mocker):
    mocker.patch("gordon.card_manager.shuffle", fake_shuffle)
    cards = load_review_cards(deficient_db, "gordon/test/test_files/big.dek", True, False)
    #2 cards at level 1 taken from level 2 because there are none left at 1
    assert cards[3][0] == "question12"
    assert cards[4][0] == "question13"
    #1 card at level 2
    assert cards[5][0] == "question14"
    #1 card at level 3
    assert cards[6][0] == "question16"

def test_load_review_cards_spaced_handles_empty_db(mocker):
    mocker.patch("gordon.card_manager.shuffle", fake_shuffle)
    cards = load_review_cards({}, "gordon/test/test_files/big.dek", True, False)
    assert cards[0][0] == "question1"
    assert cards[1][0] == "question2"
    assert cards[2][0] == "question3"
    assert cards[3][0] == "question4"
    assert cards[4][0] == "question5"
    assert cards[5][0] == "question6"
    assert cards[6][0] == "question7"

def test_load_review_cards_spaced_handles_all_trained(all_trained_db, mocker):
    mocker.patch("gordon.card_manager.shuffle", fake_shuffle)
    cards = load_review_cards(all_trained_db, "gordon/test/test_files/big.dek", True, False)
    assert cards[0][0] == "question1"
    assert cards[1][0] == "question2"
    assert cards[2][0] == "question3"
    assert cards[3][0] == "question4"
    assert cards[4][0] == "question5"
    assert cards[5][0] == "question6"
    assert cards[6][0] == "question7"

def test_promote_card(simple_db):
    cards = [
        ("question1", "answer1"),
        ("question2", "answer2"),
        ("question3", "answer3")
    ]
    promote_card(simple_db, cards[0])
    promote_card(simple_db, cards[1])
    assert simple_db[cards[0][0]] == "1"
    assert simple_db[cards[1][0]] == "2"

def test_promote_card_handles_higest_level():
    db = {
        "question1": "3"
    }
    card = ("question1", "answer1")
    promote_card(db, card)
    assert db[card[0]] == "3"

def test_promote_card_handles_missing():
    db = {}
    card = ("question1", "answer1")
    promote_card(db, card)
    assert db[card[0]] == "1"

def test_demote_card(simple_db):
    cards = [
        ("question1", "answer1"),
        ("question2", "answer2"),
        ("question3", "answer3")
    ]
    demote_card(simple_db, cards[0])
    demote_card(simple_db, cards[1])
    assert simple_db[cards[0][0]] == "0"
    assert simple_db[cards[1][0]] == "0"

def test_demote_card_handles_lowest_level():
    db = {
        "question1": "0"
    }
    card = ("question1", "answer1")
    demote_card(db, card)
    assert db[card[0]] == "0"

def test_demote_card_handles_missing():
    db = {}
    card = ("question1", "answer1")
    demote_card(db, card)
    assert db[card[0]] == "0"
