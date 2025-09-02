#Rock, Paper, Scissors Game Version 0.0.0
#Copyright (c) 2025 Z_yx2
#This software is licensed under the MIT License (https://opensource.org/license/mit/)

import tkinter as tk
import random

# Scoreboard
player_score = 0
computer_score = 0

# Mapping for choices
choices_map = {'r': '🪨', 'p': '📜', 's': '✂️'}

# Function to play the game
def play(player_choice):
    global player_score, computer_score

    # Convert player's choice to emoji
    player_emoji = choices_map.get(player_choice, player_choice)
    computer_choice = random.choice(list(choices_map.values()))
    
    # Determine winner
    if player_emoji == computer_choice:
        result = "It's a tie!"
    elif (player_emoji == '🪨' and computer_choice == '✂️') or \
         (player_emoji == '📜' and computer_choice == '🪨') or \
         (player_emoji == '✂️' and computer_choice == '📜'):
        result = "You win!"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update labels
    player_label.config(text=f"Player: {player_score}")
    computer_label.config(text=f"Computer: {computer_score}")
    result_label.config(text=f"You chose {player_emoji}, Computer chose {computer_choice}. {result}")

# Game interface
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

title_label = tk.Label(root, text=" Rock, Paper, Scissors Game ", font=("Arial", 28, "bold"))
title_label.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.pack(pady=10)

# Score Labels
player_label = tk.Label(root, text="Player: 0", font=("Arial", 20))
player_label.pack(pady=10)
computer_label = tk.Label(root, text="Computer: 0", font=("Arial", 20))
computer_label.pack(pady=10)

# Buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=20)

for choice in ['r','p','s']:
    btn = tk.Button(buttons_frame, text=choices_map[choice], font=("Arial", 30), width=5, 
                    command=lambda c=choice: play(c))
    btn.pack(side='left', padx=10)

# Keyboard bindings
root.bind('r', lambda e: play('r'))
root.bind('p', lambda e: play('p'))
root.bind('s', lambda e: play('s'))

root.mainloop()
