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
company_telephone_list = []
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
            print("hola")
            #print(hola)
            #print("pepe " + str(hola[0]))
            
            if not hola:
                continue
            else:
                # print("pepe " + str(hola[0]))
                # print("La quota mensual del telèfon és " + hola[2] + " " + hola[3])
                # Identifiquem les línies que contenen els números dels telèfons corporatius
                if hola[0] == "Telèfon":
                    if hola[1].isdigit():
                        if len(hola[1]) == 9:
                            company_telephone_list.append(int(hola[1]))
                print(hola)
                # Identifiquem les línies que contenen la tarifa associada al telèfon

                # Identifiquem les línies que contenen la despesa de dades associada al telèfon
            
            print("\n")
    print("########################################")

all_pdf_phone_numbers_sorted_list = sorted(str(list(dict.fromkeys(telephone_list))).strip("[").strip("]").replace(" ", "").split(","), reverse=True)
# print(phone_sorted_list)
'''
for phone_number in company_telephone_list:
    print("Número de telèfon: " + "\t" + str(phone_number))
    print("El telèfon " + str(phone_number) + " té la tarifa...\t" + "TARIFA_X " + "que té un cost de " + "X" + "€")
    print("El mes de " + "X_MES" + " el telèfon " + str(phone_number) + " ha gastat " + "x " + "dades" + "\n\n")
'''
