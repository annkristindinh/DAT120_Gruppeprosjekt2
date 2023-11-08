#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:15:08 2023

@author: annkristin
"""

"""
c) 
Beregn trenden for antall dager med skiføre med å bruke funksjonen fra del 1 oppgave g). 
x_akse: Året skisesongen starter skal være x-akse og 
y_akse: Antall dager med skiføre den skisesongen skal være y-akse. 


Del 1, oppg. g)

import statistics

def trender(liste_x, liste_y): 
    lengde = len(liste_x)
    gjennomsnitt_x = statistics.mean(liste_x)
    gjennomsnitt_y = statistics.mean(liste_y)
    teller = 0 
    nevner = 0 
    for i in range(lengde):
        teller += (liste_x[i] - gjennomsnitt_x)*(liste_y[i] - gjennomsnitt_y)
        nevner += ((liste_x[i] - gjennomsnitt_x)**2)
    a = teller/nevner
    b = gjennomsnitt_y - (a*gjennomsnitt_x)
    print("a = ", round(a,2))
    print("b = ",round(b,2))
    return a,b 


liste_x = [1, 2, 3, 4, 5]
liste_y = [3, 5, 7, 9, 11]

a, b = trender(liste_x, liste_y)
print("Linær formel: verdi = {:.1f}x + {:.1f}".format(a, b))

"""

import statistics

def trender(liste_x, liste_y):
    lengde = len(liste_x)
    gjennomsnitt_x = statistics.mean(liste_x)
    gjennomsnitt_y = statistics.mean(liste_y)
    teller = 0
    nevner = 0
    for i in range(lengde):
        teller += (liste_x[i] - gjennomsnitt_x) * (liste_y[i] - gjennomsnitt_y)
        nevner += (liste_x[i] - gjennomsnitt_x) ** 2
    a = teller / nevner
    b = gjennomsnitt_y - (a * gjennomsnitt_x)
    return a, b


def les_data(filnavn):
    år = []
    antall_dager_med_skiføre = []
    with open(filnavn, "r") as file:
        for line in file:
            parts = line.strip().split(";")
            if len(parts) == 8:  # Sjekk om raden har riktig antall kolonner
                dato = parts[2]
                skiføre = parts[3].replace(",", ".")  # Bytt ut komma med punkt
                if skiføre.isdigit():  # Sjekk om skiføre er et tall
                    år.append(int(dato[-4:]))  # Hent ut året fra datoen
                    antall_dager_med_skiføre.append(float(skiføre))
    return år, antall_dager_med_skiføre


filnavn = "snoedybder_vaer_en_stasjon_dogn.csv"
år, antall_dager_med_skiføre = les_data(filnavn)

a, b = trender(år, antall_dager_med_skiføre)
print("Trenden for antall dager med skiføre:")
print(f"a = {round(a, 4)}")
print(f"b = {round(b, 4)}")
print("Linær formel: verdi = {:.5f}x + {:.5f}".format(a, b))


#Oving 10 oppgave d)
import matplotlib.pyplot as plt

def plot_snødybde_og_trend(år, antall_dager_med_skiføre, a, b): #Tar inn 4 parametre
    år_start = min(år)
    år_slutt = max(år)
    x = [år_start, år_slutt]
    y = [a * år_start + b, a * år_slutt + b] #Lager en liste y med to punkter som representerer trendlinjen. Bruker parameterne a og b for å beregne verdiene.

    år_med_data = [] #Lager en tom liste som skal inneholde år med tilstrekkelig data
    antall_dager_med_skiføre_med_data = [] #Lager liste som skal inneholde tilsvarende antall dager med skiføre for år med tilstrekkelig data.

    for i in range(len(år)): #Løkke som går gjennom hvert år i listen "år"
        if antall_dager_med_skiføre[i] >= 200: #Sjekker om antall dager med skiføre for det gjeldende året er større eller lik 200.
            år_med_data.append(år[i]) #Hvis betingelsen er oppfylt, legges året til i år_med_data.
            antall_dager_med_skiføre_med_data.append(antall_dager_med_skiføre[i]) #Tilsvarende legges antall dager med skiføre til i antall_dager_med_skiføre_med_data.

    plt.figure(figsize=(10, 6)) #Lager en figur for plottet med en størrelse på 10x6 tommer.
    plt.scatter(år_med_data, antall_dager_med_skiføre_med_data, label="Antall dager med skiføre") # Dette lager et spredningsplott av dataene med årene på x-aksen og antall dager med skiføre på y-aksen. "label" gir en etikett til plottet.
    #Lager trendlinjen med de to punktene og gir den en rød farge med en stiplet linjestil. Det inkluderer også en etikett som viser den matematiske formelen for trenden.
    plt.plot(x, y, color='red', linestyle='--', label=f"Trend: y = {round(a, 2)}x + {round(b, 2)}")
    plt.xlabel("År")
    plt.ylabel("Antall dager med skiføre")
    plt.title("Snødybde og Trend")
    plt.legend() #Legger til en plottlegende som viser etikettene for data og trendlinjen.
    plt.grid(True) #Legger til et rutenett i plottet.
    plt.show()

filnavn = "snoedybder_vaer_en_stasjon_dogn.csv"
år, antall_dager_med_skiføre = les_data(filnavn)
a, b = trender(år, antall_dager_med_skiføre)
plot_snødybde_og_trend(år, antall_dager_med_skiføre, a, b)

































