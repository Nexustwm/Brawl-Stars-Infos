import os
import colorama

def clear():
    os.system("cls")

clear()

# only for pins
def common(nc, text):
    print(nc, colorama.Fore.CYAN + text + colorama.Style.RESET_ALL)

# for both skins and pins
def rare(nc, text):
    print(nc, colorama.Fore.GREEN + text + colorama.Style.RESET_ALL)

def superrare(nc, text):
    print(nc, colorama.Fore.BLUE + text + colorama.Style.RESET_ALL)

def epic(nc, text):
    print(nc, colorama.Fore.MAGENTA + text + colorama.Style.RESET_ALL)

def mythic(nc, text):
    print(nc, colorama.Fore.RED + text + colorama.Style.RESET_ALL)

def legendary(nc, text):
    print(nc, colorama.Fore.YELLOW + text + colorama.Style.RESET_ALL)

def skins():
    print("Select an number below to see info about its associated skin type")
    rare("1.", "Rare skins")
    superrare("2.", "Super Rare skins")
    epic("3.", "Epic skins")
    mythic("4.", "Mythic skins")
    legendary("5.", "Legendary skins")
    x = input("\n>>> ")
    if x == "1":
        top_text = "Rare Skins"
        gems = "29"
        bling = "1000"
        discount = "19"
        texture = True
        animation = False
        effects = False
        voice = False
        icon = False
        pin = False
        spray = False
        pinpack = False
        nobling = False
    elif x == "2":
        top_text = "Super Rare Skins"
        gems = "79"
        bling = "2750"
        discount = "39"
        texture = True
        animation = True
        effects = True
        voice = False
        icon = False
        pin = True
        spray = False
        pinpack = False
        nobling = False
    elif x == "3":
        top_text = "Epic Skins"
        gems = "149"
        bling = "5000"
        discount = "79"
        texture = True
        animation = True
        effects = True
        voice = False
        icon = True
        pin = True
        spray = False
        pinpack = False
        nobling = False
    elif x == "4":
        top_text = "Mythic Skins"
        gems = "199"
        bling = "na"
        discount = "149"
        texture = True
        animation = True
        effects = True
        voice = False
        icon = True
        pin = True
        spray = True
        pinpack = False
        nobling = True
    elif x == "5":
        top_text = "Legendary Skins"
        gems = "299"
        bling = "na"
        discount = "269"
        texture = True
        animation = True
        effects = True
        voice = True
        icon = True
        pin = False
        spray = True
        pinpack = True
        nobling = True
    else:
        clear()
        skins()
    print(top_text + "\n")
    if nobling == True:
        print("Price: " + gems + colorama.Fore.GREEN + " Gems" + colorama.Style.RESET_ALL)
    if nobling == False:
        print("Price: " + gems + colorama.Fore.GREEN + " Gems" + colorama.Style.RESET_ALL + " | " + bling + colorama.Fore.CYAN + " Bling" + colorama.Style.RESET_ALL)
    print("Special offers & Discount price: " + discount + colorama.Fore.GREEN + " Gems" + colorama.Style.RESET_ALL)
    print(f"\n{top_text} include:")
    if texture == True:
        print("- Custom texture")
    if animation == True:
        print("- Custom animations")
    if effects == True:
        print("- Custom effects")
    if voice == True:
        print("- Custom voice effects")
    if icon == True:
        print("- Profile Icon")
    if pin == True:
        print("- Pin")
    if spray == True:
        print("- Spray")
    if pinpack == True:
        print("- Pin Set")
    input("\nPress Enter to continue")
    clear()
    main()

def pins():
    print("Select an number below to see info about its associated pin type")
    print("Brawler specific Pins:")
    common("1.", "Common pins")
    rare("2.", "Rare pins")
    epic("3.", "Epic pins")
    print("\nSlot 2 Pins:")
    legendary("4.", "Legendary pins")
    x = input("\n>>> ")
    if x == "1":
        source = "Catalog"
        top_text = "Common Pins"
        gems = "9"
        bling = "375"
        default = True
        happy = True
        sad = True
        angry = True
        gg = False
        clap = False
        thanks = False
        phew = False
        special = False
    elif x == "2":
        source = "Catalog"
        top_text = "Rare Pins"
        gems = "19"
        bling = "750"
        default = False
        happy = False
        sad = False
        angry = False
        gg = True
        clap = True
        thanks = False
        phew = False
        special = False
    elif x == "3":
        source = "Catalog"
        top_text = "Epic Pins"
        gems = "39"
        bling = "1500"
        default = False
        happy = False
        sad = False
        angry = False
        gg = False
        clap = False
        thanks = True
        phew =  True
        special = True
    elif x == "4":
        source = "Catalog, Shop, Brawl Talk YouTube description link and BSC website"
        top_text = "Legendary Pins"
        gems = "39"
        bling = "1500"
        default = True
        happy = True
        sad = True
        angry = True
        gg = True
        clap = True
        thanks = True
        phew = True
        special = True
    else:
        clear()
        pins()
    print(top_text + "\n")
    print("You can get these type of pins from " + source)
    print("Price: " + gems + colorama.Fore.GREEN + " Gems" + colorama.Style.RESET_ALL + " | " + bling + colorama.Fore.CYAN + " Bling" + colorama.Style.RESET_ALL)
    print("Special offers & Discount price: " + colorama.Fore.RED + "Pins are not discounted" + colorama.Style.RESET_ALL)
    print(f"\n{top_text} can have one of the following type of animations:")
    if default == True:
        print("- Default")
    if happy == True:
        print("- Happy")
    if sad == True:
        print("- Sad")
    if angry == True:
        print("- Angry")
    if gg == True:
        print("- Good game!")
    if clap == True:
        print("- Clap")
    if thanks == True:
        print("- Thanks!")
    if phew == True:
        print("- Phew!")
    if special == True:
        print("- Special Pin")
    input("\nPress Enter to continue")
    clear()
    main()

r_date = "Jun. 10, 2024 9:00 UTC"

def trophyS():
    print(f"Input your trophies number for a specific brawler (Next trophy reset: {r_date})")
    try:
        x = int(input("\n>>> "))
        if x < 500:
            reset = "0"
            bling = "0"
        elif x > 500 and x < 525:
            reset = "500"
            bling = "4"
        elif x > 524 and x < 550:
            reset = "524"
            bling = "6"
        elif x > 549 and x < 575:
            reset = "549"
            bling = "8"
        elif x > 574 and x < 600:
            reset = "574"
            bling = "10"
        elif x > 599 and x < 625:
            reset = "599"
            bling = "12"
        elif x > 624 and x < 650:
            reset = "624"
            bling = "14"
        elif x > 649 and x < 675:
            reset = "649"
            bling = "16"
        elif x > 674 and x < 700:
            reset = "674"
            bling = "18"
        elif x > 699 and x < 725:
            reset = "699"
            bling = "20"
        elif x > 724 and x < 750:
            reset = "724"
            bling = "22"
        elif x > 749 and x < 775:
            reset = "749"
            bling = "24"
        elif x > 774 and x < 800:
            reset = "774"
            bling = "26"
        elif x > 799 and x < 825:
            reset = "799"
            bling = "28"
        elif x > 824 and x < 850:
            reset = "824"
            bling = "30"
        elif x > 849 and x < 875:
            reset = "849"
            bling = "32"
        elif x > 874 and x < 900:
            reset = "874"
            bling = "34"
        elif x > 899 and x < 925:
            reset = "899"
            bling = "36"
        elif x > 924 and x < 950:
            reset = "924"
            bling = "38"
        elif x > 949 and x < 975:
            reset = "949"
            bling = "40"
        elif x > 974 and x < 1000:
            reset = "974"
            bling = "42"
        elif x > 999 and x < 1050:
            reset = "999"
            bling = "44"
        elif x > 1049 and x < 1100:
            reset = "1049"
            bling = "46"
        elif x > 1099 and x < 1150:
            reset = "1099"
            bling = "48"
        elif x > 1149 and x < 1200:
            reset = "1149"
            bling = "50"
        elif x > 1199 and x < 1250:
            reset = "1199"
            bling = "52"
        elif x > 1249 and x < 1300:
            reset = "1249"
            bling = "54"
        elif x > 1299 and x < 1350:
            reset = "1299"
            bling = "56"
        elif x > 1349 and x < 1400:
            reset = "1349"
            bling = "58"
        elif x > 1399 and x < 1450:
            reset = "1399"
            bling = "60"
        elif x > 1449 and x < 1500:
            reset = "1449"
            bling = "62"
        elif x > 1499:
            reset = "1499"
            bling = "64"
        if reset == "0" and bling == "0":
            print("You have less than 500 trophies on this brawler, so after the trophy reset the amount of trophies won't change and you won't get any Bling!")
        else:
            print("\nAfter the next season reset, your brawler will have " + reset + colorama.Fore.YELLOW + " trophies" + colorama.Style.RESET_ALL + " and you will get " + colorama.Fore.CYAN + bling + colorama.Style.RESET_ALL + " Bling")
        input("\nPress Enter to continue")
        clear()
        main()
    except:
        print("Make sure you typed a number")
        input("Press Enter to return to main menu")
        clear()
        main()

def bp():
    print("Select your Brawl Pass type:\n")
    legendary("1.", "Brawl Pass")
    common("2.", "Brawl Pass Plus")
    x = input("\n>>> ")
    if x == "1":
        price = "$7.53"
        top_text = "Brawl Pass"
        brawler_unlock = True
        coins = 8000
        pp = 2000
        credit = 1000
        bling = 2200
        gems = 50
        skin = True
        pinset = True
        icon = True
        spray = True
        skin_chromas = False
        title = False
        progress = False
    elif x == "2":
        price = "$10.77"
        top_text = "Brawl Pass Plus"
        brawler_unlock = True
        coins = 11000
        pp = 3500
        credit = 1000
        bling = 3700
        gems = 100
        skin = True
        pinset = True
        icon = True
        spray = True
        skin_chromas = True
        title = True
        progress = True # instant 20%
    else:
        clear()
        bp()
    print(top_text + f" is at {price}(depends on region) price and it gives:\n")
    if brawler_unlock == True:
        print("- Unlock any Brawler up to Epic rarity")
    print(f"- {coins} Coins")
    print(f"- {pp} Power Points")
    print(f"- {credit} Credits")
    print(f"- {bling} Bling")
    print(f"- {gems} Gems")
    if skin == True:
        print("- Exclusive Skin")
    if pinset == True:
        print("- Pin Set")
    if icon == True:
        print("- Player Icon")
    if spray == True:
        print("- Spray")
    if skin_chromas == True:
        print("- Skin color variations")
    if title == True:
        print("- Title")
    if progress == True:
        print("- Instant 20% progress")
    print("\nAlso both Brawl Pass types include chromatic name, extra daily shop gift, double daily XP and extra Quests.")
    input("\nPress Enter to continue")
    clear()
    main()

def mastery():
    print("Select a rarity and you will see the rewards of respective Brawlers")
    rare("1.", "Rare brawlers")
    superrare("2.", "Super Rare brawlers")
    epic("3.", "Epic brawlers")
    mythic("4.", "Mythic brawlers")
    legendary("5.", "Legendary brawlers")
    x = input("\n>>> ")
    if x == "1":
        top_text = "Rare brawler"
        tier1 = "750" #coins
        tier2 = "100" #pp
        tier3 = "75" #credits
        tier4 = "200" #pp
        tier5 = "1250" #coins
        tier6 = "150" #credits
        tier7 = "Facepalm Pin"
        tier8 = "Player Icon"
        tier9 = "Title"
    if x == "2":
        top_text = "Super Rare brawler"
        tier1 = "750" #coins
        tier2 = "100" #pp
        tier3 = "75" #credits
        tier4 = "200" #pp
        tier5 = "1250" #coins
        tier6 = "150" #credits
        tier7 = "Facepalm Pin"
        tier8 = "Player Icon"
        tier9 = "Title"
    if x == "3":
        top_text = "Epic brawler"
        tier1 = "750" #coins
        tier2 = "100" #pp
        tier3 = "75" #credits
        tier4 = "200" #pp
        tier5 = "1250" #coins
        tier6 = "150" #credits
        tier7 = "Facepalm Pin"
        tier8 = "Player Icon"
        tier9 = "Title"
    if x == "4":
        top_text = "Mythic brawler"
        tier1 = "1000" #coins
        tier2 = "150" #pp
        tier3 = "100" #credits
        tier4 = "300" #pp
        tier5 = "2000" #coins
        tier6 = "200" #credits
        tier7 = "Facepalm Pin"
        tier8 = "Player Icon"
        tier9 = "Title"
    if x == "5":
        top_text = "Legendary brawler"
        tier1 = "1000" #coins
        tier2 = "150" #pp
        tier3 = "100" #credits
        tier4 = "300" #pp
        tier5 = "2000" #coins
        tier6 = "200" #credits
        tier7 = "Facepalm Pin"
        tier8 = "Player Icon"
        tier9 = "Title"
    print("\nIf you are going to push a " + top_text + ", you will get these rewards:")
    print("Bronze I: ", tier1, " Coins")
    print("Bronze II: ", tier2, " Power Points")
    print("Bronze III: ", tier3, " Credits")
    print("Silver I: ", tier4, " Power Points")
    print("Silver II: ", tier5, " Coins")
    print("Silver III: ", tier6, " Credits")
    print("Gold I: ", tier7)
    print("Gold II: ", tier8)
    print("Gold III: ", tier9)
    input("\nPress Enter to continue")
    clear()
    main()

def std():
    print("Select a type of Starr Drop and you will see what type of rewards you can get\n")
    rare("1.", "Rare Starr Drop")
    superrare("2.", "Super Rare Starr Drop")
    epic("3.", "Epic Starr Drop")
    mythic("4.", "Mythic Starr Drop")
    legendary("5.", "Legendary Starr Drop")
    x = input("\n>>> ")
    if x == "1":
        top_text = "Rare Starr Drop"
        coins = True
        pp = True
        credit = True
        bling = False
        xp = True
        rare_brawler = False
        superrare_brawler = False
        epic_brawler = False
        mythic_brawler = False
        legendary_brawler = False
        rare_pin = False
        common_pin = False
        epic_pin = False
        special_pin = False
        spray = False
        icon = False
        sp = False
        gadget = False
        rare_skin = False
        superrare_skin = False
        epic_skin = False
    elif x == "2":
        top_text = "Super Rare Starr Drop"
        coins = True
        pp = True
        credit = True
        bling = True
        xp = True
        rare_brawler = False
        superrare_brawler = False
        epic_brawler = False
        mythic_brawler = False
        legendary_brawler = False
        rare_pin = False
        common_pin = True
        epic_pin = False
        special_pin = False
        spray = True
        icon = True
        sp = False
        gadget = False
        rare_skin = True
        superrare_skin = False
        epic_skin = False
    elif x == "3":
        top_text = "Epic Starr Drop"
        coins = True
        pp = True
        credit = True
        bling = True
        xp = True
        rare_brawler = True
        superrare_brawler = True
        epic_brawler = True
        mythic_brawler = False
        legendary_brawler = False
        rare_pin = True
        common_pin = True
        epic_pin = True
        special_pin = True
        spray = True
        icon = True
        sp = True
        gadget = True
        rare_skin = True
        superrare_skin = False
        epic_skin = False
    elif x == "4":
        top_text = "Mythic Starr Drop"
        coins = True
        pp = True
        credit = True
        bling = True
        xp = True
        rare_brawler = True
        superrare_brawler = True
        epic_brawler = True
        mythic_brawler = True
        legendary_brawler = False
        rare_pin = True
        common_pin = True
        epic_pin = True
        special_pin = True
        spray = True
        icon = True
        sp = True
        gadget = True
        rare_skin = True
        superrare_skin = True
        epic_skin = False
    elif x == "5":
        top_text = "Legendary Starr Drop"
        coins = True
        pp = True
        credit = True
        bling = True
        xp = True
        rare_brawler = True
        superrare_brawler = True
        epic_brawler = True
        mythic_brawler = True
        legendary_brawler = True
        rare_pin = True
        common_pin = True
        epic_pin = True
        special_pin = True
        spray = True
        icon = True
        sp = True
        gadget = True
        rare_skin = True
        superrare_skin = True
        epic_skin = True
    print(f"\nA {top_text} can give you one of the following rewards:")
    if coins:
        print("- Coins")
    if pp:
        print("- Power Points")
    if credit:
        print("- Credits")
    if bling:
        print("- Bling")
    if xp:
        print("- XP Doublers")
    if rare_brawler:
        print("- Rare brawler")
    if superrare_brawler:
        print("- Super Rare brawler")
    if epic_brawler:
        print("- Epic brawler")
    if mythic_brawler:
        print("- Mythic brawler")
    if legendary_brawler:
        print("- Legendary brawler")
    if rare_pin:
        print("- Rare Pin")
    if common_pin:
        print("- Common Pin")
    if epic_pin:
        print("- Epic Pin")
    if special_pin:
        print("- Special Starr Drop Pin")
    if spray:
        print("- Spray")
    if icon:
        print("- Player Icon")
    if sp:
        print("- Star Power")
    if gadget:
        print("- Gadget")
    if rare_skin:
        print("- Rare skin")
    if superrare_skin:
        print("- Super Rare skin")
    if epic_skin:
        print("- Epic skin")
    input("\nPress Enter to continue")
    clear()
    main()

def center_2strings(conwidth, str1, str2):
	return print(str1 + (' ' * (conwidth // 2 - len(str1)) + '| ' + str2))

def colored_str(text, color = None):
	if not color:
		color = colorama.Fore.GREEN
	return print(color + text + ' ' * (10 - len(text)) + colorama.Style.RESET_ALL)

import shutil

conwidth = shutil.get_terminal_size().columns

def line():
    print(conwidth*" ")

# VERSION
v = "5.1"
clickbait = "I am back"

def listn(tab, char, text):
    print(tab*"\t" + colorama.Fore.GREEN + char + " " + colorama.Style.RESET_ALL + text)

def news():
    clear()
    colored_str("News")
    print("\nI am back! - May 14, 2024 | 5.0 -> 5.1")
    print("")
    print("For start, i changed some details")
    listn(1, ">", "Fixed some wrong texts")
    listn(1, ">", "Updated trophy reset date")
    listn(1, ">", "Bling is not displayed for Mythic and Legendary skins anymore")
    listn(1, ">", "Mastery leaderboard removed")
    listn(2, "-", "Its useless")
    listn(2, "-", "Takes space on your device")
    #listn(0, "", "")
    print("\nIt's all for this update, but i will add more cool features soon!")
    input("\nPress Enter to continue")
    clear()
    main()

def main():
    print((colorama.Back.BLACK + colorama.Fore.GREEN + f"Brawl Stars Infos | Version {v}" + colorama.Style.RESET_ALL).center(conwidth + 14))
    print('Check for updates!'.center(conwidth))
    line()
    colored_str("Brawl")
    center_2strings(conwidth, ' 1   ' + "Skins", "Price, discounts & more")
    center_2strings(conwidth, ' 2   ' + "Pins", "Price & more")
    center_2strings(conwidth, ' 3   ' + "Trophy Reset", "How much trophies will you have after season ends?")
    center_2strings(conwidth, ' 4   ' + "Brawl Pass", "Select a Brawl Pass type")
    center_2strings(conwidth, ' 5   ' + "Mastery Rewards", "Select a brawler rarity")
    center_2strings(conwidth, ' 6   ' + "Starr Drops", "Rewards for each Starr Drop type")
    line()
    colored_str("Other")
    center_2strings(conwidth, ' 7 ' + "News", f"{clickbait}...")
    line()
    colored_str("Power")
    print(' 8 ' + "Restart")
    print(' 9 ' + "Exit")
    line()
    x = input("\n>>> ")
    if x == "1":
        clear()
        skins()
    elif x == "2":
        clear()
        pins()
    elif x == "3":
        clear()
        trophyS()
    elif x == "4":
        clear()
        bp()
    elif x == "5":
        clear()
        mastery()
    elif x == "6":
        clear()
        std()
    elif x == "7":
        clear()
        news()
    elif x == "8":
        clear()
        main()
    elif x == "9":
        exit()
    else:
        clear()
        main()

main()
