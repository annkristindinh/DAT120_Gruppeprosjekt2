#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 08:58:16 2023

@author: ibenmostad
"""

import csv
import matplotlib.pyplot as plt

def lengste_nullsekvens(liste):
    maks_lengde=0  #starter fra 0
    gjeldende_lengde=0   #hvor mange 0er det faktisk er
    
    for nummer in liste:
        if nummer==0:
            gjeldende_lengde+=1
            
            if gjeldende_lengde>maks_lengde:
                maks_lengde=gjeldende_lengde
        else:
           gjeldende_lengde=0
        
    return maks_lengde

def finn_lengste_tørkeperioder(filbane):
    nedbørsdata= {}
    
    with open(filbane, "r", encoding="UTF8") as fil:
        leser=csv.reader(fil, delimiter=";")
        next(leser)
        
        for rad in leser:
            if len(rad)<6 or rad[5]=="-" or not rad[4].replace(",","").replace(".","").isdigit():
                continue
            
            try:
                nedbør=float(rad[4].replace(",","."))
            except ValueError:
                print(f"Ugyldig nedbørsverdi: {rad[4]}")
                continue
            
            år=rad[2].split(".")[-1]
            
            if år not in nedbørsdata:
                nedbørsdata[år]=[]
                
            nedbørsdata[år].append(nedbør)
            
    gyldige_år=[]
    lengste_tørkeperioder=[]
    
    for år, nedbørsliste in nedbørsdata.items():
        if len(nedbørsliste)>=300:
            gyldige_år.append(år)
            lengste_tørke=lengste_nullsekvens([1 if nedbør>0 else 0 for nedbør in nedbørsliste])
            lengste_tørkeperioder.append(lengste_tørke)
    
    return gyldige_år, lengste_tørkeperioder

#eksempelbruk
filbane="snodybde.csv"
gyldige_år, lengste_tørkeperioder=finn_lengste_tørkeperioder(filbane)

#plot resultatet
plt.plot(gyldige_år, lengste_tørkeperioder, marker="o")
plt.xlabel("År")
plt.ylabel("Lengste tørkeperioder (dager)")
plt.title("Lengste tørkeperiode for hvert år")
plt.show()





        