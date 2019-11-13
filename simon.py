import random
from playsound import playsound
from tkinter import ttk
import tkinter as tk

class Simon:
    """Simon Game Object"""

    def __init__(self, root):
        self.root = root

        self.high_score = 0
        
        self.canvas = tk.Canvas(self.root, height=400, width=400)
        self.canvas.pack()
        
        self.light = {'R': "red", 'G': "green", 'B': "blue", 'Y': "goldenrod"}
        self.dark  = {'R': "darkred", 'G': "darkgreen", 'B': "darkblue", 'Y': "darkgoldenrod"}

        self.squares = {
            'R': self.canvas.create_rectangle(0, 0, 200, 200, fill= "darkred", outline="darkred"),
            'G': self.canvas.create_rectangle(200, 0, 400, 200, fill= "darkgreen", outline="darkgreen"),
            'B': self.canvas.create_rectangle(0, 200, 200, 400, fill= "darkblue", outline="darkblue"),
            'Y': self.canvas.create_rectangle(200, 200, 400, 400, fill= "darkgoldenrod", outline="darkgoldenrod")
        }

        self.sounds = {
            'R': 'sounds/red.wav',
            'G': 'sounds/green.wav',
            'B': 'sounds/blue.wav',
            'Y': 'sounds/yellow.wav'
        }

        self.ids = {v:k for k,v in self.squares.items()}
        self.button = ttk.Button(self.root, text="Start Game", command=self.draw_board)
        self.button.pack()

        #self.draw_board()
    
    def draw_board(self):
        """Starts the round"""

        self.pattern = random.choice('RGBY')
        self.selections = ''
        self.root.after(1000, self.animate_board)
        self.button.state(['disabled'])


    def animate_board(self, index=0):
        """Shows the user the next pattern sequence"""

        c = self.pattern[index]
        playsound(self.sounds[c], False)
        self.canvas.itemconfig(self.squares[c], fill=self.light[c],  outline=self.light[c])
        self.root.after(500, lambda: self.canvas.itemconfig(self.squares[c], fill=self.dark[c], outline=self.dark[c]))

        index += 1
        if index < len(self.pattern):
            self.root.after(1000, lambda: self.animate_board(index))
        else:
            self.bind_buttons()

    def bind_buttons(self):
        """Binds buttons"""
        self.canvas.bind('<1>', self.select)

    def select(self, event=None):
        """Checks the user input against the next item in the pattern"""

        id = self.canvas.find_withtag("current")[0]
        color = self.ids[id]

        self.selections += color
        #print('%s v %s' %(self.pattern, self.selections))

        playsound(self.sounds[color], False)
        self.canvas.itemconfig(id, fill=self.light[color],  outline=self.light[color])
        self.root.after(200, lambda: self.canvas.itemconfig(id, fill=self.dark[color], outline=self.dark[color]))

        if self.pattern == self.selections:
            self.canvas.unbind('<1>')
            self.pattern += random.choice("RGBY")
            self.selections = ''
            self.root.after(1500, self.animate_board)
            self.button.config(text="Score %d" % (len(self.pattern)-1))
        elif self.pattern[len(self.selections)-1] != color:
            self.high_score = max(len(self.pattern)-1, self.high_score)
            self.canvas.unbind('<1>')
            self.button.config(text="Try Again!")
            self.button.state(['!disabled'])
            
    
    def print_pattern(self):
        """Prints the current pattern to the terminal"""

        print(self.pattern)