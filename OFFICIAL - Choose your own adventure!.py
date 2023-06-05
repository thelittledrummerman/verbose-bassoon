from tkinter import *
 
#option text
option_A = 'Take the dark path'
option_A1 = 'Run through the middle'
option_A2 = 'Hug the wall and move slowly'
option_A2a = 'Continue straight'
option_1A2a = 'Try to tame them'
option_2A2a = 'Try to run away'
option_A2b = 'Descend the staircase'
option_B = 'Take the well-lit path'
option_B1 = 'Leave it alone'
option_B2 = 'Pull the lever'
option_B1a = 'Stride through the colorful flora'
option_B1b = 'Crawl through the hole'
option_1B1b = 'Wait it out'
option_2B1b = 'Crawl faster to get out'
###
#story text
starttext = 'On   your   adventure,   you    discover   a \ndeep   cave   reeking   of   treasure   and   fortune. \nYou   know   what   you   must   do.....'
story1 = 'Upon   entering,   you   see   that   the   cave \nsplits   in   two   paths.   One   pitch   black,   the   other \nbright   as   day.   Which   path   will   you   take?'
story2 = 'You   move   toward   the   dark...\nHow   would   you   like   to   proceed   down   the   path?'
story3 = 'As   you   continue   down   the   path,   you \nnotice   a   winding   staircase   to   your   left   that \ndescends   into   an   empty   abyss.   What   will   you   do?'
story4 = 'Continuing,   you   hear   a   strange   noise   from \nthe   ceiling   above.   Within   seconds,   you   are   surrounded \nby   hundreds   of   venemous   snakes.   What   will   you   do?'
story5 = 'After   walking   for   ages,   you   come \nacross   a   worn,   rusty   lever   on   the   wall. \nWhat   will   you   do?'
story6 = 'You   stumble   upon   a   large   chamber.   The   path   forward   is   laden \nwith   magnificent   flowers   and   plants.   You   also   see   a   very \nnarrow   opening   on   the   far   side   of   the   wall.   What   will   you   do?'
story7 = 'As   you   are   squeezing   through   the   hole, \nyou   hear   and   feel   a   low   rumbling   all   around   you. \nWhat   will   you   do?'
story8 = 'You   squeeze   out   just   in   time   as   the \nhole   collapses   behind   you.   You   turn   to   face   the   room \nand   find   treasure   beyond   your   wildest   dreams!'
story9 = 'A   pressure   plate   in   the \nmiddle   of   the   floor   sends   a   barrage \nof   arrows   that   impale   you.'
story10 = 'The  endless   descent   and   darkness \nmake   you   go   mad. \nTerrified,   you   sprint   back   the   way   you   came.'
story11 = 'The   floor   opens   up   beneath   you \nand   you   fall   on   a   deadly   bed \nof   jagged   spikes.'
story12 = 'You   left   your   flute   in   your   other   pants. \nThe   snakes   attack. \nYou   never   stood   a   chance.'
story13 = 'Thousands   of   locusts   emerge   from \nthe   brush,   swarming   and   biting \nuntil   there   is   nothing   left.'
story14 = 'You   took   too   long. \nThe   hole   caves   in   and   you   are   crushed \nby   the   rubbled.'
story15 = 'You   somehow   manage   to   shake   them   off \nand   run   towards   a   nearby   door. \nInside,   you   find   a   lifetime   of   treasure   and   valuables!'
###
#buttons/options
def optionA():
  button0.place_configure(x = 300, y = 500, width = 1000, height = 130)
  button0.configure(text = option_A, command = optionA1 )
  button1.place(x = 300, y = 660, width = 1000, height = 130)
  button1.configure(text = option_B, command = optionB)
  canvas.itemconfigure(storytext, text = story1)
def optionA1():
  button0.configure(text = option_A1, command = arrowtrap)
  button1.configure(text = option_A2, command = optionA2)
  canvas.itemconfigure(storytext, text = story2)
def optionA2():
  button0.configure(text = option_A2a, command = optionA2a)
  button1.configure(text = option_A2b, command = scaredlose)
  canvas.itemconfigure(storytext, text = story3)
def optionA2a():
  button0.configure(text = option_1A2a, command = snakebite)
  button1.configure(text = option_2A2a, command = win1)
  canvas.itemconfigure(storytext, text = story4)
def optionB():
  button0.configure(text = option_B1, command = optionB1)
  button1.configure(text = option_B2, command = spiketrap)
  canvas.itemconfigure(storytext, text = story5)
def optionB1():
  button0.configure(text = option_B1a, command = bugswarm)
  button1.configure(text = option_B1b, command = optionB1b)
  canvas.itemconfigure(storytext, text = story6)
def optionB1b():
  button0.configure(text = option_1B1b, command = collapse)
  button1.configure(text = option_2B1b, command = win2)
  canvas.itemconfigure(storytext, text = story7)
###
#death/lose text
def arrowtrap():
  startover()
  death.place_configure(x = 685, y = 375)
  canvas.itemconfigure(storytext, text = story9)
def scaredlose():
  startover()
  scared.place_configure(x = 390, y = 375)
  canvas.itemconfigure(storytext, text = story10)
def spiketrap():
  startover()
  death.place_configure(x = 685, y = 375)
  canvas.itemconfigure(storytext, text = story11)
def snakebite():
  startover()
  death.place_configure(x = 685, y = 375)
  canvas.itemconfigure(storytext, text = story12)
def bugswarm():
  startover()
  death.place_configure(x = 685, y = 375)
  canvas.itemconfigure(storytext, text = story13)
def collapse():
  startover()
  death.place_configure(x = 685, y = 375)
  canvas.itemconfigure(storytext, text = story14)
###
#win text
def win1():
  startover()
  win.place_configure(x = 685, y = 375)
  canvas.itemconfigure(storytext, text = story15)
def win2():
  startover()
  win.place_configure(x = 685, y = 375)
  canvas.itemconfigure(storytext, text = story8)
###
#places start over button // restarts game from beginning
def startover():
  button0.configure(text = 'Start over', command = restart)
  button0.place_configure(x = 450, y = 550, width = 700, height = 80)
  button1.place_forget()
def restart():
  button0.configure(text = 'START', command = optionA)
  button0.place_configure(x = 550, y = 480, width = 500, height = 180)
  win.place_forget()
  death.place_forget()
  scared.place_forget()
  canvas.itemconfigure(storytext, text = starttext)
###
#window
if __name__ == '__main__':
  root = Tk()
  root.geometry('1600x900+50+0')
  root.resizable(False, False)
  root.title( 'Can You Find the Treasure?' )
###  
#Canvas w/background image & story text
  canvas = Canvas(root, width = 1600, height = 900,)
  canvas.pack()
  background_image = PhotoImage(file = 'C:\\Users\\logan\\OneDrive\\Pictures\\cave picture1.png')
  canvas.create_image((800, 0), image = background_image, anchor = N)
  storytext = canvas.create_text((800, 215),
     text = 'On   your   adventure,   you   discover   a \ndeep   cave   reeking   of   treasure   and   fortune. \n\nYou   know   what   you   must   do.....', 
     font = ('Papyrus', 35), justify = CENTER, fill = 'cornsilk2')
###  
#sub-text of ending
  death = Label(root, text = 'You died!', font = ('Papyrus', 40), bg = 'black', fg = 'red')
  scared = Label(root, text = 'You live, but do not find the treasure. Try again!', font = ('Papyrus', 30), bg = 'black', fg = 'DarkGoldenrod3')
  win = Label(root, text = 'You Win!', font = ('Papyrus', 40), bg = 'black', fg = 'green')
  death.place
  scared.place
  win.place
###
#buttons
  button0 = Button(root, text = 'START', command = optionA)
  button0.configure(font = ('Papyrus', 28), bg = 'dark slate gray', fg = 'cornsilk2')
  button1 = Button(root, text = option_B, command = optionB)
  button1.configure(font = ('Papyrus', 28), bg = 'dark slate gray', fg = 'cornsilk2')
  button0.place(x = 550, y = 480, width = 500, height = 180)
###
  root.mainloop()