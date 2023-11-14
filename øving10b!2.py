#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:41:27 2023

@author: ibenmostad
"""

import csv

def tell_storre_enn_verdi(liste, verdi):
    antall_storre_enn_verdi=0
    for element in liste:
        if element>=verdi:
            antall_storre_enn_verdi+=1
    return antall_storre_enn_verdi

def beregn_snødager(filbane):
    snø_data={}
    
    
    with open(filbane, "r", encoding="UTF8") as fil:
        leser= csv.reader(fil, delimiter=";")
        next(leser)
    
        for rad in leser:
            if len(rad)<4:
                print(f"Ugyldig rad: {rad}")
                continue
                
          
            snødybde=rad[3].replace(",",".")
            try:
                 snødybde=float(snødybde)
            except ValueError:
                 #print(f"Ugyldig snødybdeverdi: {snødybde}")
                 continue
             
            dato=rad[2].split(".")
            måned=int(dato[1])
            år=dato[2]
        
            if måned>=10:
                if år not in snø_data:
                     snø_data[år]=[]
                snø_data[år].append(snødybde)
            
            elif måned<=6:
                 forrige_år=str(int(år)-1)
                 if forrige_år not in snø_data:
                     snø_data[forrige_år]=[]
                 snø_data[forrige_år].append(snødybde)
    return snø_data
 
    #eksempelbruk
snø_data=beregn_snødager("snodybde.csv")

for år, verdi in snø_data.items():
    snø_data[år]=tell_storre_enn_verdi(verdi, 20)
    print(f"i {år} var det {snø_data[år]} dager med minst 20cm snø.")
             
                
    