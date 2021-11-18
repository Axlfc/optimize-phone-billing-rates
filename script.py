#!/usr/bin/env python3
import pdftotext

# Load your PDF
with open("/home/axl/Escriptori/git/optimize-phone-billing-rates/factures/Octubre/28-J1U1-004553.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Read all the text into one string
pdf_content="\n\n".join(pdf)

# Separate page content in a list
pagines = pdf_content.split("Página")

# Create telephone list containing sorted phone list
telephone_list = []

for pagina in pagines:
    contingut = pagina.splitlines()
    print("####################################")
    for i in contingut:
        test = i.split("\n")
        for j in test: 
            hola = str(j).replace("\t", "").split(" ")

            hola[:] = [x for x in hola if x]
            for k in hola:
                if k.isdigit():
                    if len(k) == 9:
                        telephone_list.append(int(k))
            print(hola)
    print("########################################")

phone_sorted_list = sorted(str(list(dict.fromkeys(telephone_list))).strip("[").strip("]").replace(" ", "").split(","), reverse=True)
print(phone_sorted_list)
for phone_number in phone_sorted_list:
    print("Número de telèfon: " + "\t" + str(phone_number))
    print("El telèfon " + str(phone_number) + " té la tarifa...\t" + "TARIFA_X " + "que té un cost de " + "X" + "€")
    print("El mes de " + "X_MES" + " el telèfon " + str(phone_number) + " ha gastat " + "x " + "dades" + "\n\n")
