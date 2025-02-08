# Culture Seas 2025
Creators: David Shi, Insiah Kizilbash, Jessica Hsin, Adelle Melnikov
## Goal:
- To promote real and meaningful human connection through a virtual game

## Game Outline:
- Culture Seas is an interactive game that allows users to explore new cultures by making human connections
- The user starts the game with the first screen, prompting to enter a name
- After hitting enter/return, the user switches to the cruise ship view, where they are greeted with Charlie, an elderley man acting as a guide
- Charlie holds a brief conversation with the user, while the ships sails to nearby islands.
- When approaching an island, the user has the option to get of the ship ans explore
- When selecting exploration, the user enters a new island, where he/she can move to the island's resident (each resident represents a real person, who has bought his/her culture to share")
- The island resident sparks a conversation with the user and the user participates in a few lines of dialogue, given the oopportunity to visit landmarks and other interesting sites on the island

## Contains:
- assets folder: both imported and personally designed images for the game visuals
- ship-scene folder: image components designed for the ship view
- Scene_CruiseShip.py
- Scene_Start.py
- Scene_Island.py
- Scene_AnchoredShip.py
- game_manager.py
- dialogue.py
- main.py
- config.py

## Functions:
- game_manager: creates and changes new scenes for the game display
- Scene files:
  - handle_events: update the screen based on what action the user completes 
  - draw: draw the new screen after all updates have been made 
- dialogue:
  - start_dialogue: island resident begins dialogue with the user
  - advance_dialogue: user chooses dialogue options to respond to the island resident
- main:
  - runs the game loop, updating and drawing each frame after the user makes changes

## How to Use:
- User moves using w(up), a(left), s(down), d(right) keys
- After typing the desired name into the start screen, hit enter to change to the cruise ship view
- To talk to a character, move using the keys specified and click on the screen
- When a dialogue is started, click on the choice desired when it pops up after the island resident's speech


