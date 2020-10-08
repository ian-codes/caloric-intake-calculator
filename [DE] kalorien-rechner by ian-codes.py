input("Drücke die Enter-Taste, um zu beginnen.")
print("\n")

# Personal  Input Values
num1 = input("Gib dein Körpergewicht in kg ein: ")
num2 = input("Gib deine Körpergrösse in cm ein: ")
num3 = input("Gib dein alter in Jaren ein: ")
result = round(66.5 + (13.75 * float(num1)) + (5 * float(num2)) - (6.76 * float(num3)))
print("\n")

# BMR
print("Dein Grundumsatz ist:", result ,
      "Kalorien pro Tag.")
print("\n")
input("Drücke die Enter-Taste, um fortzufahren.")
print("\n")

# Activity Level Selection
print("Wähle deine sportliche Aktivität: \n")
print("1) Sitzend (wenig bis keine Bewegung)")
print("2) Leichte Bewegung (leichtes Training, 1-3 Tage/Woche)")
print("3) Mittelgradige Bewegung (mittelgradiges Training, 3-5 Tage/Woche)")
print("4) Hohe Bewegung (strenges Training, 6-7 Tage/Woche)\n")

num4 = input("Wähle eine Zahl zwischen 1 - 4: \n")
if num4 == "1":
    print("Dein TDEE (Total Daily Energy Expenditure) ist ungefähr ",
           round(result * 1.2),"Kalorien pro Tag.")
    res1 = round(result * 1.2)
elif num4 == "2":
    print("Dein TDEE (Total Daily Energy Expenditure) ist ungefähr ",
          round(result * 1.38), "Kalorien pro Tag.")
    res1 = round(result * 1.38)
elif num4 == "3":
    print("Dein TDEE (Total Daily Energy Expenditure) ist ungefähr ",
          round(result * 1.55), "Kalorien pro Tag.")
    res1 = round(result * 1.55)
elif num4 == "4":
    print("Dein TDEE (Total Daily Energy Expenditure) ist ungefähr ",
          round(result * 1.73), "Kalorien pro Tag.")
else :
    print("Error! Gib einen Wert zwischen 1 - 4 ein.")
print("\n")
input("Drücke die Enter-Taste um fortzufahren.")
print("\n")

# Weight goal
print("Wähle dein Ziel: \n")
print("1) Ich möchte gern zunehmen.")
print("2) Ich möchte gern abnehmen.")
print("3) Ich möchte mein aktuelles Körpergewicht beibehalten. \n")

num5 = input("Wähle eine Option zwischen 1 - 3 \n")
if num5 == "1":
    print("Deine tägliche Kalorieneinnahme sollte ungefähr ",
          res1 + 500, "Kalorien sein." )
elif num5 == "2":
    print("Deine tägliche Kalorieneinnahme sollte ungefähr. ",
          res1 - 500, "Kalorien sein.")
elif num5 == "3":
    print("Deine tägliche Kalorieneinnahme sollte ungefähr. ",
           res1, "Kalorein sein."
                 " Dies ist der gleiche Wert, wie oben schon berechnet wurde (TDEE).")
else :
    print("Error! Gib einen Wert zwischen 1 - 3. ein")
print("\n")

input("Drücke die Enter-Taste, um das Programm zu beenden.")
