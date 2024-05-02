

import pythonGraph as pg
import math
import random


#--------------------------------------------------------------------------------
SCREEN_SIZE = 600              
GRID_DIMENSION=5
pg.open_window(SCREEN_SIZE, SCREEN_SIZE)
pg.set_window_title('Taylor Swift Lyric Guesser')

#keyboard variables
keysize = 58
keymargin = 1
key = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
          ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
          ['Z', 'X', 'C', 'V', 'B', 'N', 'M']]
keys = []
#guess variables
guesses =  [[],[],[],[],[]]
colors =   [['WHITE','WHITE','WHITE','WHITE','WHITE'],
           ['WHITE','WHITE','WHITE','WHITE','WHITE'],
           ['WHITE','WHITE','WHITE','WHITE','WHITE'],
           ['WHITE','WHITE','WHITE','WHITE','WHITE'],
           ['WHITE','WHITE','WHITE','WHITE','WHITE']]
current_guess_row = 0
##end game variables
won = False
lost = False
invalid = False
##list of words from file
list_in_files = []
word = ''
guess_to_check = ''
guess_to_update = ''

#line1
def display_grid():
#a
   pg.draw_rectangle(5/20*SCREEN_SIZE,0,7/20*SCREEN_SIZE,1/10*SCREEN_SIZE,"BLACK",False,5 )
#b
   pg.draw_rectangle(7/20*SCREEN_SIZE,0,9/20*SCREEN_SIZE,1/10*SCREEN_SIZE,"BLACK",False,5 )
#c
   pg.draw_rectangle(9/20*SCREEN_SIZE,0,11/20*SCREEN_SIZE,1/10*SCREEN_SIZE,"BLACK",False,5 )
#d
   pg.draw_rectangle(11/20*SCREEN_SIZE,0,13/20*SCREEN_SIZE,1/10*SCREEN_SIZE,"BLACK",False,5 )
#e
   pg.draw_rectangle(13/20*SCREEN_SIZE,0,15/20*SCREEN_SIZE,1/10*SCREEN_SIZE,"BLACK",False,5 )
#line2
#a
   pg.draw_rectangle(5/20*SCREEN_SIZE,1/10*SCREEN_SIZE,7/20*SCREEN_SIZE,2/10*SCREEN_SIZE,"BLACK",False,5 )
#b
   pg.draw_rectangle(7/20*SCREEN_SIZE,1/10*SCREEN_SIZE,9/20*SCREEN_SIZE,2/10*SCREEN_SIZE,"BLACK",False,5 )
#c
   pg.draw_rectangle(9/20*SCREEN_SIZE,1/10*SCREEN_SIZE,11/20*SCREEN_SIZE,2/10*SCREEN_SIZE,"BLACK",False,5 )
#d
   pg.draw_rectangle(11/20*SCREEN_SIZE,1/10*SCREEN_SIZE,13/20*SCREEN_SIZE,2/10*SCREEN_SIZE,"BLACK",False,5 )
#e
   pg.draw_rectangle(13/20*SCREEN_SIZE,1/10*SCREEN_SIZE,15/20*SCREEN_SIZE,2/10*SCREEN_SIZE,"BLACK",False,5 )
#line3
#a
   pg.draw_rectangle(5/20*SCREEN_SIZE,2/10*SCREEN_SIZE,7/20*SCREEN_SIZE,3/10*SCREEN_SIZE,"BLACK",False,5 )
#b
   pg.draw_rectangle(7/20*SCREEN_SIZE,2/10*SCREEN_SIZE,9/20*SCREEN_SIZE,3/10*SCREEN_SIZE,"BLACK",False,5 )
#c
   pg.draw_rectangle(9/20*SCREEN_SIZE,2/10*SCREEN_SIZE,11/20*SCREEN_SIZE,3/10*SCREEN_SIZE,"BLACK",False,5 )
#d
   pg.draw_rectangle(11/20*SCREEN_SIZE,2/10*SCREEN_SIZE,13/20*SCREEN_SIZE,3/10*SCREEN_SIZE,"BLACK",False,5 )
#e
   pg.draw_rectangle(13/20*SCREEN_SIZE,2/10*SCREEN_SIZE,15/20*SCREEN_SIZE,3/10*SCREEN_SIZE,"BLACK",False,5 )
#line4
#a
   pg.draw_rectangle(5/20*SCREEN_SIZE,3/10*SCREEN_SIZE,7/20*SCREEN_SIZE,4/10*SCREEN_SIZE,"BLACK",False,5 )
#b
   pg.draw_rectangle(7/20*SCREEN_SIZE,3/10*SCREEN_SIZE,9/20*SCREEN_SIZE,4/10*SCREEN_SIZE,"BLACK",False,5 )
#c
   pg.draw_rectangle(9/20*SCREEN_SIZE,3/10*SCREEN_SIZE,11/20*SCREEN_SIZE,4/10*SCREEN_SIZE,"BLACK",False,5 )
#d
   pg.draw_rectangle(11/20*SCREEN_SIZE,3/10*SCREEN_SIZE,13/20*SCREEN_SIZE,4/10*SCREEN_SIZE,"BLACK",False,5 )
#e
   pg.draw_rectangle(13/20*SCREEN_SIZE,3/10*SCREEN_SIZE,15/20*SCREEN_SIZE,4/10*SCREEN_SIZE,"BLACK",False,5 )
#line5
#a
   pg.draw_rectangle(5/20*SCREEN_SIZE,4/10*SCREEN_SIZE,7/20*SCREEN_SIZE,5/10*SCREEN_SIZE,"BLACK",False,5 )
#b
   pg.draw_rectangle(7/20*SCREEN_SIZE,4/10*SCREEN_SIZE,9/20*SCREEN_SIZE,5/10*SCREEN_SIZE,"BLACK",False,5 )
#c
   pg.draw_rectangle(9/20*SCREEN_SIZE,4/10*SCREEN_SIZE,11/20*SCREEN_SIZE,5/10*SCREEN_SIZE,"BLACK",False,5 )
#d
   pg.draw_rectangle(11/20*SCREEN_SIZE,4/10*SCREEN_SIZE,13/20*SCREEN_SIZE,5/10*SCREEN_SIZE,"BLACK",False,5 )
#e
   pg.draw_rectangle(13/20*SCREEN_SIZE,4/10*SCREEN_SIZE,15/20*SCREEN_SIZE,5/10*SCREEN_SIZE,"BLACK",False,5 )
   
def display_guesses():
   num_of_guesses=5
   num_of_letters=5
   box = 50
   for i in range(num_of_guesses):
       for j in range(num_of_letters):
       # coordinate positions
           x = 155 + j * (box + 10)
           y = 5 + i * (box + 10)
           if i < len(guesses) and j < len(guesses[i]):
               guess = guesses[i][j]
               color = colors[i][j]
           else:
               guess = ''
               color = 'WHITE'

           # background box
           pg.draw_rectangle(x, y, x + box, y + box, colors[i][j] , True)
           # letter in the center of the box
           pg.draw_text(guess, x+box//4 , y+box//4 , 'BLACK', keysize)
def generate_word():
   global list_in_files
   with open('Taylor.txt','r') as file:
       list_in_files = file.read()
       word_choices =list_in_files.split()
   word= random.choice(word_choices)
   return word

def generate_keyboard():
   global keys
   global colors
   row_height = keysize + keymargin
   total_height = len(key) * row_height  # height of all rows
   startY = ((SCREEN_SIZE - total_height) //2) +150  # start y coordinate position
#loop for row
   for i in range(len(key)):
       row = key[i]
       row_keys = []
       startX = ((SCREEN_SIZE - (len(row) * (keysize + keymargin)))// 2) + 2.5
   #letter in row
       for l in range(len(row)):
           k = row[l]
           keyX1 = startX + l * (keysize + keymargin)
           keyY1 = startY + i *row_height
           keyX2 = keyX1 +keysize
           keyY2 = keyY1 +keysize
           color = 'light grey'
       # append key information
           row_keys.append([k, keyX1, keyY1, keyX2, keyY2, color])

   # append the row_keys list to the keys list
       keys.append(row_keys)
def update_keyboard(guess_to_update):
   global word
   global key
   global colors
   global current_guess_row
   #loop for updating colors on keys
   for i in range(len(guess_to_update)):
       for j in range(len(key)):
           if key[j][0] == guess_to_update[i]:
               key[j][5] = colors[current_guess_row][i]

def check_answer():
   global won
   global colors
   global word
   global keys
   correct_counter = 0
   #colors change due to position
   for i in range(len(guesses[current_guess_row])):
       if guesses[current_guess_row][i] == word[i]:
           correct_counter += 1
           colors[current_guess_row][i] = 'green'
           for line in keys:
               for keyss in line:
                   #forcing iteration through keyboard
                   #print(guesses[current_guess_row][i])
                   if keyss[0]==guesses[current_guess_row][i].upper():
                       keyss[5]= 'green'
                       print(keyss)
       elif guesses[current_guess_row][i] in word:
           colors[current_guess_row][i] = 'yellow'
           for line in keys:
               for keyss in line:
                   #forcing iteration through keyboard
                   #print(guesses[current_guess_row][i])
                   if keyss[0]==guesses[current_guess_row][i].upper()and keyss[5]!='green':
                       keyss[5]= 'yellow'
                       print(keyss)
       else:
           colors[current_guess_row][i] = 'dark grey'
           for line in keys:
               for keyss in line:
                   #forcing iteration through keyboard
                   #print(guesses[current_guess_row][i])
                   if keyss[0]==guesses[current_guess_row][i].upper()and keyss[5]!='green'and keyss[5]!='yellow':
                       keyss[5]= 'dark grey'
                       print(keyss)

           # If all letters are correct
   if correct_counter == 5:
       won = True
   update_keyboard(colors[current_guess_row])  

def display_keyboard():
   global keys
   for row in keys:
       for letter in row:
           #keybox
           pg.draw_rectangle(letter[1]+ 1, letter[2]+ 1, letter[3]-1, letter[4] -1, letter[5], True)
           # draw letter
           pg.draw_text(letter[0], (letter[1]+ keysize //2)-6, (letter[2] + keysize //2)-6, 'black', int(keysize//2))

def check_valid(word):
   if word in list_in_files:
       return True
   else:
       return False

def display_invalid():
   num_of_letters = 5
   global invalid
   global current_guess_row
   global guesses
   global colors
   if invalid == True:
       guesses[current_guess_row].clear()##erase frame if invalid to enter new guess
       colors[current_guess_row] = ['white'] * num_of_letters
       pg.draw_text('Invalid Word', 210, 320, 'BLUE', 40)

def listen_keyboard():
   num_of_guesses=5
   num_of_letters=5
   global current_guess_row
   global word
   global colors
   global guesses
   global guess_to_check
   global invalid
   pressed = pg.get_pressed_key()
   if pressed is not None:
       if pressed == "backspace":
           if guesses[current_guess_row]:
               guesses[current_guess_row].pop()
               colors[current_guess_row].pop()
       elif pressed == "return":
           if len(guesses[current_guess_row]) == num_of_letters:
               guess_to_check = (
               guesses[current_guess_row][0] +
               guesses[current_guess_row][1] +
               guesses[current_guess_row][2] +
               guesses[current_guess_row][3] +
               guesses[current_guess_row][4]
               )
               if check_valid(guess_to_check):
                   check_answer()
                   if current_guess_row < num_of_guesses:
                       current_guess_row += 1
               else:
                   invalid = True
           else:
               invalid = True #invalid for word not in file and if letters<5
       elif pressed.isalpha():
           if len(guesses[current_guess_row]) < num_of_letters:
               guesses[current_guess_row].append(pressed)  
               if current_guess_row >= len(colors):  
                   colors.append(['white'] * num_of_letters)  
               else:
                   colors[current_guess_row].append('white')
               invalid = False #user can enter guess after invalid word

           if len(guesses[current_guess_row]) == num_of_letters:
               if current_guess_row >= num_of_guesses - 1:
                   current_guess_row = num_of_guesses - 1

def game_over():
   global won
   global lost
   if won == True :
       pg.draw_text("YOU WIN!", 220, 320, 'GREEN', 40)
   elif current_guess_row == 5:
       lost = True
       pg.draw_text("YOU LOSE", 220, 320, 'RED', 40)

#main and function calls
#call generate keyboard once, not in a loop
generate_keyboard()  
word =generate_word()
print(word)
#set up your animation loop per Graohics 2 animate lesson
while pg.window_not_closed() and not won and not lost:
   pg.draw_rectangle(0, 0, SCREEN_SIZE,SCREEN_SIZE, 'white', True)#clear window/erase frame
   if invalid:
       display_invalid()#only displays invalid message when invalid

    
   ##only calls when game is not over
   if not won and not lost:
       listen_keyboard()
       display_grid()
       display_guesses()
       display_keyboard()


   game_over()
   pg.update_window()
#pg.wait_for_close()
