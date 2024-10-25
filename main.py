
import turtle as trtl
import random

# Global variables
score = 0
time_left = 10  # You can adjust the total time here


def start_game():
    global score, time_left

    # Create the turtle that will be clicked
    turt = trtl.Turtle()

    # Turtles for displaying score and time
    scoreKeeper = trtl.Turtle()
    timeKeeper = trtl.Turtle()
    scoreKeeper.hideturtle()
    timeKeeper.hideturtle()

    # Move score/time turtles to positions
    teleportation(scoreKeeper, [0, 370])
    teleportation(timeKeeper, [0, 340])

    # Initial display of score and time
    font_setup = ("Arial", 20, "normal")
    text_update(scoreKeeper, score, "Your score: ", font_setup)
    text_update(timeKeeper, time_left, "Time left: ", font_setup)

    # Set up the game window
    wind = trtl.Screen()
    wind.screensize(800, 800)
    wind.title("Catch-A-Turtle Game")
    wind.bgcolor("lightblue")
