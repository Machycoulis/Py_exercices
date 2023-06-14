papa = "Bob"
maman = "Isabelle"
enfant_1 = "Alexandre"
enfant_2 = "Sam"

famille = [papa, maman, enfant_1, enfant_2]

dict_fam = {
    papa: ["21-12-1970", "garçon"],
    maman: ["10-07-1980", " fille"],
    enfant_1: ["19-05-199", " garçon"],
    enfant_2: ["02-03-2002", " garçon"],
}

for membre in famille:
    print("Nombre de lettres dans le prénom", membre, ":", len(membre))