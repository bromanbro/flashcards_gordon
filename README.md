[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/DorianYeager/5)

# Flashcards Gordon
Flashcards at the command line with advanced features including reversal and spaced repetition

## About The Project
Flashcards Gordon was developed because the world deserves a simple flashcard application with powerful features available at the command line.  The decks you create are plain text files with each line representing a card and the text for the front and back separated by three pound signs.  Flashcards Gordon gives you all of the powerful features that you expect from a flashcard application.  
* The reversal feature will quiz you by showing the backs of the cards and asking you to answer what the front is.  Very useful when learning a new language.
* The spaced feature puts Flashcards Gordon in spaced repition mode where one third of the deck is pulled placing emphasis on the cards you are learning while giving lower priority to those already mastered.  This is an excellent feature to use two or three times throughout the day when you have five minutes to spare.

## Getting Started
Flashcards Gordon was developed for use at the Linux command line.  It may be compatible with Windows and Mac environments but this is untested at this time.

You will need to make a deck of flashcards containing the information you wish to memorize.  This is very easy to do.  Your deck file is simply a plain text file.  Each line in the text file is a card where you put the text for the front of the card then three pound signs and the text for the back of the card.  Be careful not to leave any trailing spaces after each line.  When you you are quized the app will expect an answer that matches the line exactly, spaces and all.   

In the example below I am learning esperanto.  I put the english phrase on one side and esperanto on the other.

**Example Contents of a Card File**   
Who is that man over there?###Kiu estas tiu tie?   
What kind of apple is this?###Kia pomo estas ĉi tio?   
Whose pencil is this?###Kies krajono estas ĉi tiu?   
## Installation
1. You need to have python 3.10 and pip installed.
2. Install from the repo with pip
```sh
pip install git+https://github.com/bromanbro/flashcards_gordon.git
```
## Usage
usage: gordon [-h] [-r] [-s] card_file

positional arguments:
  card_file      The text file of the deck.

options:
  -h, --help     show this help message and exit
  -r, --reverse  Reverse question.
  -s, --spaced   Run Leitner algorithm.

## For Your Consideration
Flashcards Gordon has to persist some information to your machine so that it can keep track of your performance and weight cards for the spaced repetition algorithm.  Therefore the application will create data files for each of your decks located here:   
~/.config/gordon/

You may delete these at any time to reset the state of a deck or to simply clean out files for decks that you are no longer using.

## Roadmap
- [ ] Release usage videos demoing Flashcards Gordon
- [ ] ?
- [ ] Profit
