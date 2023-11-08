#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 12:49:54 2023

@author: annkristin
"""

"""
Skriv en funksjon som leser inn ei fil på følgende format, som inneholder data fra en  
værstasjon for hvert døgn over mange år:  
    
Navn; Stasjonsid; Dato på formen DD.MM.ÅÅÅÅ; snødybde i centimeter; nedbør i millimeter;  
middeltemperatur; gjennomsnittlig skydekke i en skala fra 0 (skyfritt) til 8 (helt  overskyet);
høyeste middelvind i meter pr. sekund.  

Merk at ikke alle dataene eksisterer for alle dagene, det vil være et «-» tegn for slike  manglende
data.  Funksjonen skal lagre disse dataene i en eller flere lister eller dictionaries. 
Funksjonen skal  returnere disse listene eller dictionaryene. Det er en del av oppgaven at
dere finner ut hvilke  datastrukturer som er mest hensiktsmessige til dette. 


"""

def les_værdata(filnavn):
    data = []  # Liste for å lagre ordbøker med værdata

    with open(filnavn, 'r', encoding='utf-8') as fil:
        for linje in fil:
            deler = linje.strip().split(';')
            if len(deler) == 8:
                navn, stasjon, dato, snødybde, nedbør, temperatur, skydekke, vindhastighet = deler

                # Konverter numeriske verdier fra strenger til passende datatyper
                if snødybde != '-':
                    snødybde = int(snødybde) if snødybde else None
                if nedbør != '-':
                    nedbør = float(nedbør.replace(',', '.')) if nedbør else None
                if temperatur != '-':
                    temperatur = float(temperatur.replace(',', '.')) if temperatur else None
                if skydekke != '-':
                    skydekke = float(skydekke.replace(',', '.')) if skydekke else None
                if vindhastighet != '-':
                    vindhastighet = float(vindhastighet.replace(',', '.')) if vindhastighet else None

                # Opprett en ordbok for dagenes data og legg den til i listen
                dagsdata = {
                    "Navn": navn,
                    "Stasjon": stasjon,
                    "Dato": dato,
                    "Snødybde (cm)": snødybde,
                    "Nedbør (mm)": nedbør,
                    "Gjennomsnittstemperatur (°C)": temperatur,
                    "Skydekke": skydekke,
                    "Vindhastighet (m/s)": vindhastighet
                }
                data.append(dagsdata)

    return data

resultat = les_værdata("snoedybder_vaer_en_stasjon_dogn.csv") # Kall på funksjonen og lagre resultatet i en variabel

for dag in resultat[:5]: # Skriv ut de første fem radene av resultatet som et eksempel
    print("Dato:", dag['Dato'])
    print("Stasjon:", dag['Stasjon'])
    print("Snødybde (cm):", dag['Snødybde (cm)'])
    print("Nedbør (mm):", dag['Nedbør (mm)'])
    print("Gjennomsnittstemperatur (°C):", dag['Gjennomsnittstemperatur (°C)'])
    print("Skydekke:", dag['Skydekke'])
    print("Vindhastighet (m/s):", dag['Vindhastighet (m/s)'])
    print()


#Kan også skrive slik:
for dag in resultat[:5]:
    print(dag)

















