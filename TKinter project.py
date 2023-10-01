import tkinter
import random

colors = ['yellow', 'magenta', 'teal', 'grey', 'red', 'brown', 'Orange' ]

score = 0
timeleft = 45

def startGame(event):

    #game time left, 45 seconds
    if timeleft == 45:

        countdown()
    #choosing the next color
    nextColor()

def nextColor():
    #use globally declared 'score
    #and 'play variables
    global score
    global timeleft

    #if the game is currently in play
    if timeleft > 0:

        #make the text entry box active
        e.focus_set()


        #if the color type is equal
        #to the color of the text
        if e.get().lower() == colors[1].lower():

            score += 1

            #clear the text entry
            e.delete(0, tkinter.END)

            random.shuffle(colors)

            #change the color to type, by changing the taext and the color to a random color
            label.config(fg = str(colors[1]), text = str(colors[0]))

            #update score
            scoreLabel.config(text = 'Score: ' + str(score))

def countdown():

    global timeleft

    #if the game is in paly
    if timeleft > 0:

        #decrease the timer
        timeleft -= 1

        #update the time left label
        timeLabel.config(text = "Time left: " + str(timeleft))

        #run the function again after 1 sec
        timeLabel.after(1000, countdown)
       

#Driver Code

#creat a GUI window
root = tkinter.Tk()

#set the title
root.title("COLORGAME")

#set the size
root.geometry("375x200")

#add the instructions label
instructions = tkinter.Label(root, text = "Type in the color" "of the words, and not the word Text!", font = ('Poppins, 13'))
instructions.pack()

#add the score label
scoreLabel = tkinter.Label(root, text = 'Press enter to start', font = ('Poppins', 13))

scoreLabel.pack()

#add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), font = ('Poppins', 13))

#add a label for displaying the colors
label = tkinter.Label(root, font = ('Poppins', 55))
label.pack()

#add a text entry box for typing the colors
e = tkinter.Entry(root)

#run tje 'startGame' function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

#set focus on the entry box
e.focus_set()

#start
root.mainloop()