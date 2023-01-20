from tkinter import *
import random

def rock():
    user_choice.set("rock")
    play()

def paper():
    user_choice.set("paper")
    play()

def scissors():
    user_choice.set("scissors")
    play()

def play():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    computer_choice_label.config(text=computer_choice)
    outcome.config(text=compare(user_choice.get(),computer_choice))

def compare(user, computer):
    if user == computer:
        return "Tie!"
    elif user == "rock" and computer == "scissors":
        return "You win!"
    elif user == "rock" and computer == "paper":
        return "You lose!"
    elif user == "paper" and computer == "rock":
        return "You win!"
    elif user == "paper" and computer == "scissors":
        return "You lose!"
    elif user == "scissors" and computer == "paper":
        return "You win!"
    elif user == "scissors" and computer == "rock":
        return "You lose!"
    else:
        return "Invalid input"

root = Tk()
root.title("Rock-Paper-Scissors")

user_choice = StringVar()

rock_button = Button(root, text="Rock", command=rock)
rock_button.pack()

paper_button = Button(root, text="Paper", command=paper)
paper_button.pack()

scissors_button = Button(root, text="Scissors", command=scissors)
scissors_button.pack()

computer_choice_label = Label(root, text="")
computer_choice_label.pack()

outcome = Label(root, text="")
outcome.pack()

root.mainloop()
