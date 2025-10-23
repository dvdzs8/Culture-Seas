# Culture Seas 
Created in 24 hours for TartanHacks 2025!

Creators: David Shi, Insiah Kizilbash, Jessica Hsin, Adelle Melnikov

## Check Out Our Video Demo!
Video Demo: https://www.youtube.com/watch?v=Ha9Wmbtq5EE

Hackathon Presentation: https://docs.google.com/presentation/d/1ncjYsTzNHGWsVEASKVvvvBabJLUvanFI-_UMcfBBwe0/edit?usp=sharing

## Goal
Highlight the beauty of genuine and meaningful human connection

## Spiel
The Against the Current track encourages us to submit a project that is not related to AI. We drew inspiration from this and took it further. What would happen if we went "against the current" of tech influx over the past decades instead? Culture Seas highlights the beauty of human connection with cozy, cultural, and meaningful vibes. 

How unlikely yet incredible is it that four people came together on the same college journey despite having such wonderfully unique backgrounds? This is the question that underscores this game; it is a love letter to our shared experiences and unique histories. The characters you meet in the game are representations of us through each other's eyes, and the islands are modeled after important landmarks from our own memories and cultures. The lonely player slowly recruits us to accompany them on their cruise ship, an action that symbolizes the ephemeral journey of college. Culture Seas is an anthology of our lives told in a personal story format that draws from Stardew Valley and Episode. We hope you enjoy it, and thank you!

## Game Outline (WIP)
- Culture Seas is an interactive game that allows users to explore new cultures by making human connections
- The user starts on a screen asking them to enter a name
- After hitting enter/return, the user switches to the cruise ship view, where they are greeted by Charlie, an elderly man acting as a guide
- Charlie holds a brief conversation with the user, while the ship sails to nearby islands
- When approaching an island, the user has the option to get off the ship and explore
- When selecting exploration, the user enters a new island, where he/she can move to the island's resident (each resident represents one of us, who has implemented their culture to share)
- The island resident sparks a conversation with the user and the user participates in a few lines of dialogue, given the opportunity to visit landmarks and other interesting sites on the island

## Contains
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

## File Explanations
- game_manager: creates and changes new scenes for the game display
- Scene files:
  - handle_events: update the screen based on what action the user completes 
  - draw: draw the new screen after all updates have been made 
- dialogue:
  - start_dialogue: island resident begins dialogue with the user
  - advance_dialogue: user chooses dialogue options to respond to the island resident
- main:
  - runs the game loop

## Challenges
Dialogue boxes were the main focus of our game which we would funnel the enjoyable nature of conversation through. However, after getting the file to work, we had trouble integrating everything together between functions and GitHub conflicts. Down to the wire, we quickly switched gears and implemented a basic console functionality instead so that we could retain some feel of the whole game. We also committed much of our time to figuring out Tiled and tilemaps, but we eventually got there albeit without knowing that .tmx files contain absolute paths on your personal computer for its tiles!

## How to Use
- Clone or download the repository
- With Python 3.13, Pygame, and PyTMX installed on your device, run the following command in the terminal after changing directories to the repository: py main.py
- User moves using w(up), a(left), s(down), d(right) keys
- After typing the desired name into the start screen, hit enter to change to the cruise ship view
- To talk to a character, move using the keys specified and click on the character
- When a dialogue is started, click on the choice desired when it pops up after the island resident's speech


