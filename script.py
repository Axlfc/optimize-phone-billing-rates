#!/usr/bin/env python3
import pdftotext

# Load your PDF
with open("/media/sf_Compartir/factures/28-J1U1-004553.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Read all the text into one string
pdf_content="\n\n".join(pdf)

# Separate page content in a list
pagines = pdf_content.split("Página")

# Create telephone list containing sorted phone list
telephone_list = []
company_telephone_list = []
phone_billing_data = {}

for pagina in pagines:
    contingut = pagina.splitlines()
    phone_associated_data = []
    for i in contingut:
        test = i.split("\n")

        for j in test:
            hola = str(j).replace("\t", "").split(" ")

            hola[:] = [x for x in hola if x]
            for k in hola:
                if k.isdigit():
                    if len(k) == 9:
                        telephone_list.append(int(k))

            if not hola:
                continue
            else:
                # Identifiquem les línies que contenen els números dels telèfons corporatius
                if hola[0] == "Telèfon":
                    if hola[1].isdigit():
                        if len(hola[1]) == 9:
                            company_telephone_list.append(int(hola[1]))
                # Identifiquem les pàgines que contentn la informació dels telèfon
                if hola[0] == "Madrid,":
                    page_num = int(str(hola[-1].split("/")[0]))
                if page_num > 2:
                    if hola[0] == "Total":
                        if not hola[1][-1] == "€":
                            phone_associated_data.append(hola[3])
                        else:
                            phone_associated_data.append(hola[1])

                    if hola[0] == "Tipus" and hola[2] == "contracte:":
                        phone_associated_data.append(str(hola[3:]).replace(",", "").replace("'", "").replace("[", "").replace("]", ""))
                    if hola[0] == "Quota":
                        phone_associated_data.append(hola[4])
                    if hola[0] == "TOTAL":
                        print("S'ha trobat un total de " + hola[4] + " amb IVA inclòs")
                    # Identifiquem les línies que contenen la despesa de dades associada al telèfon
                    if hola[0] == "Dades":
                        if hola[1][0] == "(":
                            phone_associated_data.append(hola[7])
                    if hola[0][-1:][0] == "€":
                        phone_associated_data.append(hola[0])
                    if hola[0] == "Telèfon" and hola[1].isdigit():
                        phone_billing_data[hola[1]] = phone_associated_data
                        # Afegim els números de telèfon com a claus de diccionari i afegim els camps de tarifa i despesa de dades com a valors de cada clau del diccionari
                        phone_associated_data = []

all_pdf_phone_numbers_sorted_list = sorted(str(list(dict.fromkeys(telephone_list))).strip("[").strip("]").replace(" ", "").split(","), reverse=True)
# print(phone_sorted_list)

# S'ha d'iterar sobre les claus del diccionari per mostrar la informació desitjada
# Actualment està preparat en concepte de prova iterant només sobre la llista de telèfons corporatius.
'''
for phone_number in company_telephone_list:
    print("Número de telèfon: " + "\t" + str(phone_number))
    print("El telèfon " + str(phone_number) + " té la tarifa...\t" + "TARIFA_X " + "que té un cost de " + "X" + "€")
    print("El mes de " + "X_MES" + " el telèfon " + str(phone_number) + " ha gastat " + "x " + "dades" + "\n\n")
'''
print(phone_billing_data)
