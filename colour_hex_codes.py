HEX_COLOUR = {"AliceBlue": "#f0f8ff", "BlueViolet": "#8a2be2", "CadetBlue1": "#98f5ff", "chartreuse3": "#66cd00", "chocolate3": "#cd661d", "DarkGreen": "#006400", "DarkOliveGreen": "#556b2f", "DarkOrchid4": "#68228b", "HotPink1": "	#ff6eb4", "OrangeRed1": "#ff4500"}

colour = input("Please enter a colours name.")
while colour == "":
    if colour in HEX_COLOUR:
        print(colour, "is", HEX_COLOUR.values(colour))
    else:
        print("That colour is not in my dictionary. Please try again")
        colour = input("Please enter a colours name.")

#for k,v in HEX_COLOUR.items():
#    print("{:} is {:}".format(k,v))

