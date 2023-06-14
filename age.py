while True:
    try:
        age = int(input("Quel est ton âge? "))
    except ValueError:
        print("Entrée invalide, veuillez saisir votre âge en chiffre.")
    else:
        break

if age < 18:
    print("Tu es mineur.")
else:
    print("Tu es majeur.")