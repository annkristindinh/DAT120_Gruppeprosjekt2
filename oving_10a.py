#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:46:02 2023

@author: norunnhjartaker
"""

def les_vaerdata(filnavn):
   #opprettelse av dictionary
    vaerdata = {
        'navn':[],
        'stasjonstid':[],
        'dato':[],
        'sno_dybde_cm':[],
        'nedbor_mm':[],
        'middeltempereatur':[],
        'skydekke':[],
        'middelvind_mps':[],
    }


   
               
    try:
        with open(filnavn, 'r') as fil: #åpner fil for lesning 
            for linje in fil: #oppretter en for- løkke 
                data=linje.strip().split(';') #Linjen blir først strippet for ekstra mellomrom og deretter delt opp i lister. det gir en liste med vaerdata for den gjelende dagen
                if len(data)==8: # sjekker om elementer i linjen er 8
                #legger til data i dictionaryen
                    vaerdata['navn'].append(data[0])
                    vaerdata['stasjonstid'].append(data[1])
                    vaerdata['dato'].append(data[2])
                    try:
                       #Konverterer til riktig data
                       sno_dybde=float(data[3]) if data[3]!='-' else None
                       vaerdata['sno_dybde_cm'].append(sno_dybde)
                       
                       nedbor=float(data[4]) if data[4]!='-' else None 
                       vaerdata['nedbor_mm'].append(nedbor)
                       
                       middeltempereatur=float(data[5]) if data[5]!='-' else None
                       vaerdata['middeltempereatur'].append(middeltempereatur)
                       
                       skydekke=int(data[6]) if data[6]!='-' else None
                       vaerdata['skydekke'].append(skydekke)
                       
                       middelvind=float(data[7]) if data[7]!= '-' else None
                       vaerdata['middelvind_mps'].append(middelvind)
                    except ValueError as e:
                        #Feilmelding om det ikke er 8
                        print(f"feil konvertering:{e}")
               
    except ValueError as ex:
        print(f"Feil ved apning/lesning av fil: {ex}")
         
    return vaerdata #returnerer den ferdigstilte dictionarien 

                
