#asking for the users name
name = input("Yar! Ahoy there! Nice to meet you...er...what's your name fellow sailor? ==> ")

print("Well it sure is nice to make your acquaintance, cap'n "+str(name)+"!")

#asking the user if they would like to build a ship.
buildaship = input("So, what do you say sailor, do you want to build a ship? Aye or nay? ==> ")

if buildaship == "Aye":
    print("Well then cap'n "+str(name)+", what're we waiting for?! Let's get to building!")

if buildaship== "Nay":
    print("What are you doing wasting my time for then?! I've got treasure to find!")

#asking the user what material they would like to build their ship with
shipmaterial = input("First things first, what would ya like to build your ship with? We've got planks or driftwood! ==> ")

if shipmaterial == "Planks":
    print("Ah, a man of quality you be! Only the best for you and yer crew, much like me own ship!")

if shipmaterial == "Driftwood":
    print("Saving yer dubloons for more important things I see, good on you cap'n! Hopefully there be smooth waters where you be sailing!")

#asking the user what length they'd like their ship
shiplength = input("Well, now that you've got your wood, what length of ship would you like to make your mark on these seas? Short or long? ==> ")

if shiplength == "Long":
    print("Well that sure will leave rival sailors shivering in their boots!")

if shiplength == "Short":
    print("That is certainly one way to not spend your booty all in one place! I be respectin' a sailor who conserves his bounty rather than squanders it!")

#asking the user what colour they'd like their ships flag to be
flagcolor = input("Now that that's settled, what colour be your flag matey? I've checked me cabin and I've got some brown, green, red, or purple cloth. ==> ")

if flagcolor == "Brown":
    print("Ahoy! Now there be a colour that'll strike fear into the hearts of even the most mangy of seadogs!")

if flagcolor == "Green":
    print("Ahoy! Now there be a colour that'll strike fear into the hearts of even the most mangy of seadogs!")

if flagcolor == "Red":
    print("Ahoy! Now there be a colour that'll strike fear into the hearts of even the most mangy of seadogs!")

if flagcolor == "Purple":
    print("Ahoy! Now there be a colour that'll strike fear into the hearts of even the most mangy of seadogs!")

#asking the user what emblem should be on their flag
emblem = input("Cap'n "+str(name)+" it's time to choose the symbol which will represent you and your crew on your journey, what will it be? ==> ")

print("What a strong choice that be, sailor. A "+str(emblem)+" is sure to strike fear into the hearts of even the most scurvy of pirates! Here ye!")
               

#asking what the name of their boat should be
boatname = input("Now that you've decided on the symbol which be representin' your ship, it's time to decide on your ships name! What do ya say matey? ==> ")

print("Yar! "+str(boatname)+" you say? Yar! Well that be the most perfect name I've heard for a ship as beautiful as yours, cap'n "+str(name)+"!")

#bot discussing the boat that was created

finalconversation = input("Well, it seems we've reached the end of our journey, cap'n "+str(name)+" and it's time for you to take "+str(boatname)+" to the seas! Best of luck to you, sailor! Ahoy!")
