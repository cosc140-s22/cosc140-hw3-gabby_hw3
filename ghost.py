#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################

import random

def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist

def get_names(zero, one):
  while zero == one:
    print("\nYour names cannot be the same ")
    zero = input("Player 1, what would you like to be called? ")
    one = input("Player 2, what would you like to be called? ")
  return zero, one

def get_letter(name, word):
  letter = input(f"\nThe current fragment is: {word}\n{name} please input a single letter: ")
  while len(letter) > 1 or not letter.isalpha():
    letter = input("Please input only a single letter: ")

  letter = letter.upper()
  return letter

def check_for_start(fragment, words):
  for word in words:
    if word.startswith(fragment):
      return True
  return False

def check_game_over(fragment, words):
  if fragment in words and len(fragment) > 3:
    return True
  else:
    return False

def main():
  words = load_wordlist()
  print(f"{len(words)} words loaded.")

  # you can start your code here, inside main

  print("Welcome to Ghost!")
  
  game_over = False
  player0 = ""
  player1 = ""

  player0, player1 = get_names(player0, player1)
  
  player_turn = random.randint(0,1)

  current_word = ""
  
  while not game_over:
    player_turn = (player_turn + 1) % 2
    current_letter = ""
    
    if player_turn == 0:
      current_letter = get_letter(player0, current_word)
    else:
      current_letter = get_letter(player1, current_word)
      
    current_word = current_word + current_letter
    starts = check_for_start(current_word, words)
    contained = check_game_over(current_word, words)
    game_over = contained or not starts
    
    if contained:
      print(f"\nUnfortunately, {current_word} is in the dictionary")
    if not starts:
      print(f"\nUnfortunately, {current_word} does not start any words in my dictionary")

  won = ""
  lost = ""
  if player_turn == 0:
    won = player1
    lost = player0
  else:
    won = player0
    lost = player1
  
  print(f"\n\nCongrats {won}, you won!\n{lost} lost with the final word of {current_word}")

main()
