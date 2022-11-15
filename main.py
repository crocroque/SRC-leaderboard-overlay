from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import tkinter as tk

def cookies():
    while True:
        try:
            cookie = driver.find_element(By.XPATH, value="/html/body/div[19]/div[2]/div[1]/div[2]/div[2]/button[1]")
        except:
            pass
        else:
            cookie.click()
            break

leaderboard_link = open("txt file/leaderboard_link.txt").readline()

options = webdriver.ChromeOptions()
options.add_argument('--lang=fr')
options.add_argument('--headless')

driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=options)
driver.get(leaderboard_link)

cookies()

player = driver.find_element(By.CSS_SELECTOR, value="#game-leaderboard > div.relative.max-w-full.overflow-x-auto.overflow-y-hidden.scroll-smooth > table > tbody")
info_run = driver.find_element(By.XPATH, value="/html/body/div[7]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div")
info_run = len(info_run.text.split("\n"))

place_run = 1
index_list = 0
info_runner = ""
player_list = []
first_list = []

with open("txt file/leaderboard.txt", "w+") as file:
    file.write(player.text)

with open("txt file/leaderboard.txt", "r+") as file:
    for i in range(3):
        for m in range(info_run-1):
            info_runner = info_runner + file.readline().split("\n")[0].split("il y a ")[0].split("today")[0] + " | "
        first_list.append("#" + str(place_run) + " " + info_runner)
        place_run += 1
        info_runner = ""

    while file.readline().split("\n")[0] != "":
        for i in range(info_run):
            info_runner = info_runner + file.readline().split("\n")[0].split("il y a ")[0].split("today")[0] + " | "

        player_list.append("#" + str(place_run) + " | " + info_runner)
        info_runner = ""
        place_run += 1


def update():
    global index_list

    try:
        lfour.config(text=player_list[index_list])
    except:
        lfour.config(text="")

    try:
        lfive.config(text=player_list[index_list+1])
    except:
        lfive.config(text="")

    try:
        lsix.config(text=player_list[index_list+2])

    except:
        lsix.config(text="")

    try:
        lseven.config(text=player_list[index_list+3])
    except:
        lseven.config(text="")

    try:
        leight.config(text=player_list[index_list+4])
    except:
        leight.config(text="")
        index_list = -5

    index_list += 5
    root.after(time_wait, update)


root = tk.Tk()

param = False
bg_color = "white"
fg_color = "white"

while True:
    bg_color = input("background color :\n1 : green \n2 : white \n3 : blue \n4 : black \n5 : other\n6 : color_param \n>>>")

    if bg_color == "1":
        bg_color = "#00ff00"
        break

    elif bg_color == "2":
        bg_color = "#ffffff"
        break

    elif bg_color == "3":
        bg_color = "#0000ff"
        break

    elif bg_color == "4":
        bg_color = "#000000"
        break

    elif bg_color == "5":
        bg_color = input("type your color (Hex) : #")
        try:
            bg_color = "#" + bg_color
            test_isHex = tk.Label(bg=bg_color)
        except:
            print(bg_color, "is not a Hex color")
        else:
            break

    elif bg_color == "6":
        with open("txt file/color_param.txt") as file:
            try:
                bg_color = file.readline().split("background_color : ")[1].split("\n")[0]
                fg_color = file.readline().split("text_color : ")[1].split("\n")[0]
                time_wait = file.readline().split("time between each change (sec) : ")[1].split("\n")[0]
                time_wait = int(time_wait)
                test_isHex = tk.Label(bg=bg_color)
                test_isHex2 = tk.Label(fg=fg_color)
            except:
                print("color_param.txt does not have the expected parameters")
            else:
                param = True
                time_wait *= 1000
                break


while param == False:
    fg_color = input("text color :\n1 : black \n2 : white \n3 : other\n>>>")

    if fg_color == "1":
        fg_color = "#000000"
        break

    elif fg_color == "2":
        fg_color = "#ffffff"
        break

    elif fg_color == "3":
        try:
            fg_color = input("type your color (Hex) : #")
            fg_color = "#" + fg_color
            test_isHex = tk.Label(fg=bg_color)
        except:
            print(fg_color, "is not a Hex color")
        else:
            break

while param == False:
    time_wait = input("enter the time between each change (second)\n>>>")
    try:
        time_wait = int(time_wait)
    except:
        pass
    else:
        time_wait *= 1000

root.geometry("250x170")
root.title("SRC leaderboard")
root.configure(background=bg_color)


first = tk.Label(text=first_list[0], bg=bg_color, fg=fg_color)
second = tk.Label(text=first_list[1], bg=bg_color, fg=fg_color)
third = tk.Label(text=first_list[2], bg=bg_color, fg=fg_color)
lfour = tk.Label(text="", bg=bg_color, fg=fg_color)
lfive = tk.Label(text="", bg=bg_color, fg=fg_color)
lsix = tk.Label(text="", bg=bg_color, fg=fg_color)
lseven = tk.Label(text="", bg=bg_color, fg=fg_color)
leight = tk.Label(text="", bg=bg_color, fg=fg_color)


first.pack()
second.pack()
third.pack()
lfour.pack()
lfive.pack()
lsix.pack()
lseven.pack()
leight.pack()
root.after(1000, update)
root.mainloop()
