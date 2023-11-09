# RGB Finder

import websocket
import datetime
import json
import os
from colr import color
import datetime
import time
import rich
import random
import threading
import subprocess
from rich.console import Console
from rich import print as rprint
from rich.text import Text
from rich.panel import Panel

console = Console()
version = "v2.1"
no_buddies = False
rgb_condition = {'connection_time': None}
clearonce = True

rgbfinder1 = r"""
____/\\\\\\\\\_________/\\\\\\\\\\\\__/\\\\\\\\\\\\\______________/\\\\\\\\\\\\\\\__/\\\\\\\\\\\__/\\\\\_____/\\\__/\\\\\\\\\\\\_____/\\\\\\\\\\\\\\\____/\\\\\\\\\_____        
__/\\\///////\\\_____/\\\//////////__\/\\\/////////\\\___________\/\\\///////////__\/////\\\///__\/\\\\\\___\/\\\_\/\\\////////\\\__\/\\\///////////___/\\\///////\\\___       
_\/\\\_____\/\\\____/\\\_____________\/\\\_______\/\\\___________\/\\\_________________\/\\\_____\/\\\/\\\__\/\\\_\/\\\______\//\\\_\/\\\_____________\/\\\_____\/\\\___      
    _\/\\\\\\\\\\\/____\/\\\____/\\\\\\\_\/\\\\\\\\\\\\\\____________\/\\\\\\\\\\\_________\/\\\_____\/\\\//\\\_\/\\\_\/\\\_______\/\\\_\/\\\\\\\\\\\_____\/\\\\\\\\\\\/____     
    _\/\\\//////\\\____\/\\\___\/////\\\_\/\\\/////////\\\___________\/\\\///////__________\/\\\_____\/\\\\//\\\\/\\\_\/\\\_______\/\\\_\/\\\///////______\/\\\//////\\\____    
    _\/\\\____\//\\\___\/\\\_______\/\\\_\/\\\_______\/\\\___________\/\\\_________________\/\\\_____\/\\\_\//\\\/\\\_\/\\\_______\/\\\_\/\\\_____________\/\\\____\//\\\___   
    _\/\\\_____\//\\\__\/\\\_______\/\\\_\/\\\_______\/\\\___________\/\\\_________________\/\\\_____\/\\\__\//\\\\\\_\/\\\_______/\\\__\/\\\_____________\/\\\_____\//\\\__  
        _\/\\\______\//\\\_\//\\\\\\\\\\\\/__\/\\\\\\\\\\\\\/____________\/\\\______________/\\\\\\\\\\\_\/\\\___\//\\\\\_\/\\\\\\\\\\\\/___\/\\\\\\\\\\\\\\\_\/\\\______\//\\\_ 
        _\///________\///___\////////////____\/////////////______________\///______________\///////////__\///_____\/////__\////////////_____\///////////////__\///________\///__
"""

rgbfinder2 = r"""
 ██████╗  ██████╗ ██████╗     ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
 ██╔══██╗██╔════╝ ██╔══██╗    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
 ██████╔╝██║  ███╗██████╔╝    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
 ██╔══██╗██║   ██║██╔══██╗    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
 ██║  ██║╚██████╔╝██████╔╝    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
 ╚═╝  ╚═╝ ╚═════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

def main():
    
    os.system('cls')

    # You can also change the rgbfinder1 to rgbfinder2 to have bigger picture
    print(color(f"\n{rgbfinder2}", fore=(229, 65, 49)))
    
    # 𝕄𝕒𝕕𝕖 𝕓𝕪 𝕄𝕦𝕕𝕩𝕚𝕖𝕛 𝕚𝕟 𝕔𝕠𝕝𝕝𝕒𝕓𝕠𝕣𝕒𝕥𝕚𝕠𝕟 𝕨𝕚𝕥𝕙 𝕠𝕧𝕠𝕤𝕚𝕞𝕡𝕒𝕥𝕚𝕔𝕠 𝕗𝕣𝕠𝕞 𝕥𝕙𝕖 𝕍ℝ𝕐 𝕕𝕖𝕧𝕖𝕝𝕠𝕡𝕞𝕖𝕟𝕥 𝕥𝕖𝕒𝕞 

    print(color(" 𝕄𝕒𝕕𝕖 𝕓𝕪 ", fore=(0, 97, 103)) +
        color("𝕄𝕦𝕕𝕩𝕚𝕖𝕛_ ", fore=(165, 22, 17)) +
        color("𝕚𝕟 𝕔𝕠𝕝𝕝𝕒𝕓𝕠𝕣𝕒𝕥𝕚𝕠𝕟 𝕎𝕚𝕥𝕙 ", fore=(172, 135, 0)) +
        color("𝕠𝕧𝕠𝕤𝕚𝕄𝕡𝕒𝕥𝕚𝕔𝕠 ", fore=(255, 255, 0)) +
        color("𝕗𝕣𝕠𝕄 𝕥𝕙𝕖 𝕍ℝ𝕐 𝕕𝕖𝕧𝕖𝕝𝕠𝕡𝕄𝕖𝕟𝕥 𝕥𝕖𝕒𝕄.", fore=(172, 135, 0)) +
        color(f"\n\n Version:", fore=(20, 20, 159)) +
        color(f" {version}", fore=(50, 50, 189)))
    
    time.sleep(2)

    print(color("\n\n Connecting with a ", fore=(48, 48, 48)) +
        color("WebSocket", fore=(71, 71, 71)) +
        color("...", fore=(48, 48, 48)))

    no_buddies = False

    websocket_url = "ws://localhost:1100"
    ws = websocket.WebSocketApp(websocket_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.on_open = on_open
    ws.run_forever()

def on_message(ws, message):
    
    global no_buddies, clearonce

    # Load the buddy ID
    data = json.loads(message)
    SKIN_BUDDY_ID_RGB = "ad508aeb-44b7-46bf-f923-959267483e78"
    SKIN_BUDDY_ID_OCTO = "934164fc-49dd-1e67-0896-6c8e645fd081"
    buddy_found = False
    rgb_condition['connection_time'] = datetime.datetime.now()

    for player_id, player in data['Players'].items():
        for weapon_id, weapon in player['Weapons'].items():

            # Check for similar pattern with a buddy
            if 'skin_buddy' in weapon and weapon['skin_buddy'] == SKIN_BUDDY_ID_RGB:
                            
                buddy_found = True
                no_buddies = False
                weapon_name = weapon['weapon']
                skin_display_name = weapon['skinDisplayName']

                agent_name_with_artwork = player['AgentArtworkName']
                agent_name = agent_name_with_artwork.replace('Artwork', '')

                # Add the game data to the folder
                timestamp = datetime.datetime.now().strftime("%d/%m/%Y  %H:%M")

                save_file_lines = (
                    f"Time: {timestamp}\n"
                    f"Agent played: {agent_name}\n"
                    f"Weapon: {weapon_name}\n"
                    f"Skin: {skin_display_name}\n\n\n"
                )

                with open("List_RiotGunBuddy.txt", "a") as buddy_file:
                    buddy_file.write(save_file_lines)

                time.sleep(1.5)

                if clearonce:
                    os.system('cls')
                    clearonce = False

                team_color = 'red' if player['Team'] == "Red" else 'blue'
                print(color(f"\n\n Found RGB on player: {agent_name}", fore=team_color))
                print(f" Weapon: {weapon_name}")
                print(f" Skin: {skin_display_name}")

    clearonce = True

    # If buddy is not found
    if not buddy_found:
        
        os.system('cls')
        no_buddies = True
        rgb_condition['connection_time'] = datetime.datetime.now()

        print(color("\n\n There are", fore=(255, 255, 0)) +
            color(" no Riot Gun Buddies\n", fore=(255, 0, 0), style=1 | 4) +
            color(" in this lobby. ", fore=(255, 255, 0)) +
            color("Hidden names decrypted", fore=(74, 127, 51), style=4) +
            color(".\n", fore=(74, 127, 51)))

    # If the buddy is found
    if buddy_found:
        directory = "GameData"
        if not os.path.exists(directory):
            os.makedirs(directory)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{directory}/websocket_{timestamp}.dict"
        with open(filename, "w") as file:
            file.write(message)

        print(color("\n\n\n Data written to file", fore=(50, 178, 50)) +
            color(f" {filename}\n\n", fore=(0, 128, 128)))

        buddy_found = False
        
def on_open(ws):

    print(color("\n Connetion with VRY WebSocket was set ", fore=(48, 48, 48)) +
        color("succesfully", fore=(71, 71, 71), style=4) +
        color(".\n\n", fore=(48, 48, 48)))

    time.sleep(3)

    timer_thread = threading.Thread(target=update_timer, args=(rgb_condition,))
    timer_thread.daemon = True
    timer_thread.start()
    
def on_error(ws, error):
    return

    #if error == ".":
        #error = "CTRL + C has stopped the code (probably)"

    #if error != 'Players':
        #print(
            #color("\n\n\n There is an ", fore=(128, 128, 128)) +
            #color("error", fore=(255, 0, 0), style=4) +
            #color(" in the app ", fore=(128, 128, 128)) +
            #color("Error code name", fore=(162, 162, 162), style=4) +
            #color(":", fore=(192, 192, 192)) +
            #color(f" {error}.", fore=(192, 192, 192)) +
            #color("\n\n Please contact the developer about an error", fore=(64, 64, 64)))

def on_close(ws, close_status_code, close_msg):

    print(color("\n\n Connection closed\n", fore=(255, 255, 0)))
    time.sleep(2)

def update_timer(rgb_condition):

        while True:

            while no_buddies:

                time.sleep(1.4)
                
                current_time = datetime.datetime.now()
                time_difference = current_time - rgb_condition['connection_time']
                total_seconds = time_difference.total_seconds()

                if total_seconds >= 3600:
                    # If the difference is an hour or more, format it as HH:MM:SS
                    hours = int(total_seconds // 3600)
                    minutes = int((total_seconds % 3600) // 60)
                    seconds = int(total_seconds % 60)
                    time_difference_formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                else:
                    # Otherwise, format it as MM:SS
                    minutes = int(total_seconds // 60)
                    seconds = int(total_seconds % 60)
                    time_difference_formatted = f"{minutes:02d}:{seconds:02d}"

                print(color("\033[A" + " Last data received", fore=(91, 192, 222)) +
                        f" {color(time_difference_formatted, fore=(60, 60, 60))} " +
                        color("ago", fore=(91, 192, 222)))

if __name__ == "__main__":
    main()