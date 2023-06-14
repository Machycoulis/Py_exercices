from datetime import date

year = int(input("Année AAAA: "))
month = int(input("Mois MM: "))
day = int(input("Jour JJ: "))

def get_age(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

print(get_age(date(year, month, day)), "years")