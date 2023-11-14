#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:28:54 2023

@author: annkristin
"""

"""
Beregn veksten for den tenkte planten for hvert år i datasettet med bruk av funksjonen fra  del 1 oppgave h). 
Plott dette for hvert år i datasettet. Inkluder bare år hvor det er temperaturdata for mesteparten av året, 
det må være data for minst 300 dager for at et år  skal være gyldig. Dette vil kreve at dere lager separate lister 
for hvert år som kan brukes som  parameter til funksjonen fra del 1 oppgave h) 

Oppg. 1h)
def beregn_plante_vekst (temp_liste):
    total_vekst = 0 
    for temperatur in temp_liste:
        vekst = max(temperatur - 5, 0) #Veksten er 0 hvis temperaturen er < 5
        total_vekst += vekst 
        
    return total_vekst


temp_liste = [4,7,15]     
vekst_sum = beregn_plante_vekst(temp_liste)
print("Vekstsum: ",vekst_sum)


"""
#Venabu;SN13420;04.08.1980;0;1,9;13,3;7;4,6 
#Navn; Stasjon; Dato på formen DD.MM.ÅÅÅÅ; Snødybde i cm; Nedbør i mm;  Middeltemp; Gjns. skydekke; Høyeste middelvind i m/s
#0;1;2;3;4;5;6;7 --> lengde 8

import matplotlib.pyplot as plt

def beregn_plante_vekst(temp_liste):
    total_vekst = 0
    for temperatur in temp_liste:
        vekst = max(temperatur - 5, 0)  # Veksten er 0 hvis temperaturen er < 5
        total_vekst += vekst
    return total_vekst

with open("snoedybder_vaer_en_stasjon_dogn.csv", "r", encoding="UTF-8") as fila:
    next(fila)  #Hopper over den første linjen i fila
    total_grader_aar = {} #Tom dictionary for å lagre total vekst per år
    temperaturer = [] #Tom liste for å lagre temperaturer for hvert år
    aar = "" #Variabel for å holde styr på gjeldende år

    for linje in fila: #Starter en løkke som itererer gjennom hver linje i fila
        verdiliste = linje.split(";") #Deler opp linjen i en liste ved å bruke ";" som skilletegn. 
        #Resultatet er en liste kalt verdiliste som inneholder verdiene fra hver kolonne.
        if verdiliste[5] == "-" or verdiliste[5] == "":
            #Sjekker om verdien i den sjette kolonnen (indeks 5 i Python, siden indeksering starter med 0) 
            #er en streng "-" eller en tom streng. Hvis det er tilfellet, hopper koden til neste 
            #iterasjon av løkken ved å bruke continue.
            continue
        else:
            #Hvis betingelsen ikke er oppfylt, blir temperaturverdien i den sjette kolonnen konvertert til en flyttall. 
            #Eventuelle komma blir erstattet med punktum for å sikre riktig formatering.
            temperatur = float(str(verdiliste[5]).replace(",", "."))
            if verdiliste[2][-4:] == aar:
                temperaturer.append(temperatur)
            #Sjekker om året i den tredje kolonnen (indeks 2) er det samme som det gjeldende året (aar). 
            #Hvis det er tilfelle, legges temperaturverdien til temperaturer-listen.    
            elif aar == "":
                temperaturer.append(temperatur)
                aar = verdiliste[2][-4:]
                #Hvis aar er tomt, betyr det at dette er den første linjen. Legger temperaturverdien til temperaturer-listen 
                #og setter aar til å være de siste fire tegnene av datoen i den tredje kolonnen.
            else:
                if len(temperaturer) >= 300:
                    total_vekst = beregn_plante_vekst(temperaturer)
                    total_grader_aar.update({aar: total_vekst})
                    print(f"Vekst for {aar}: {total_vekst}")
                aar = verdiliste[2][-4:]
                temperaturer = []
                temperaturer.append(temperatur)
                #Hvis aar allerede er satt og ikke er det samme som året i den tredje kolonnen, 
                #sjekker koden om lengden på temperaturer-listen er større eller lik 300. Hvis det er tilfelle, 
                #beregner den total vekst ved hjelp av beregn_plante_vekst-funksjonen, oppdaterer total_grader_aar-dictionary 
                #med denne informasjonen, skriver ut veksten for det gjeldende året og starter på nytt for det nye året. 
                #Hvis lengden av temperaturer ikke er større eller lik 300, setter den gjeldende året til å være det nye året 
                #og starter en ny liste for temperaturer.

    x_verdier = total_grader_aar.keys()
    y_verdier = total_grader_aar.values()

    # Plotting
    plt.figure(figsize=(12.8, 4.8))
    plt.title("Vekstrate av planter gjennom årene")
    plt.xticks(rotation=45)
    plt.bar(x_verdier, y_verdier)
    plt.show()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    