birth_year = int(input("Enter your birth year:  "))
if birth_year < 1900:
  print("Invalid Year, it should not be earlier than 1900")
if birth_year >= 1900:
    base = birth_year - 1900
    if base % 12 == 0:
        print("Your Chinese Zodiac Sign is: Rat (鼠 / Shǔ)") 
    elif base % 12 == 1:
        print("Your Chinese Zodiac Sign is: Ox (牛 / Niú)")        
    elif base % 12 == 2:
        print("Your Chinese Zodiac Sign is: Tiger (虎 / Hǔ)")   
    elif base % 12 == 3:
        print("Your Chinese Zodiac Sign is: Rabbit (兔 / Tù)")   
    elif base % 12 == 4:
        print("Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)")
    elif base % 12 == 5:
        print("Your Chinese Zodiac Sign is: Snake (蛇 / Shé)")
    elif base % 12 == 6:
        print("Your Chinese Zodiac Sign is: Horse (马 / Mǎ)")   
    elif base % 12 == 7:
        print("Your Chinese Zodiac Sign is: Goat (羊 / Yáng)")
    elif base % 12 == 8:
        print("Your Chinese Zodiac Sign is: Monkey (猴 / Hóu)")
    elif base % 12 == 9:
        print("Your Chinese Zodiac Sign is: Rooster (鸡 / Jī)")
    elif base % 12 == 10:
        print("Your Chinese Zodiac Sign is: Dog (狗 / Gǒu)")
    elif base % 12 == 11:
        print("Your Chinese Zodiac Sign is: Pig (猪 / Zhū)")  
