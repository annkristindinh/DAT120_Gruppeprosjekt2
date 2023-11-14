#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:24:51 2023

@author: ibenmostad
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt


def les_data(filbane):
    data=[]
    with open(filbane, newline="", encoding="UTF-8") as csvfile:
        leser=csv.DictReader(csvfile, delimiter=";")
        for rad in leser:
            data.append(rad)
    return data

def legg_til_år_kolonne(data):
    for oppføring in data:
        tidspunkt=oppføring["Tid(norsk normaltid)"]
        if tidspunkt:
            oppføring["År"]=datetime.strptime(tidspunkt, "%d.%m.%Y").year
        else:
            oppføring["År"]=None
            
        
def filtrer_gyldige_år(data):
    gyldige_år={}
    for oppføring in data:
        år=oppføring["År"]
        if år not in gyldige_år:
            gyldige_år[år]={"vindhastigheter":[]}
        vindhastighet_str= oppføring["Høyeste middelvind (døgn)"].replace(",",".")
        if vindhastighet_str and vindhastighet_str !="-":
            gyldige_år[år]["vindhastigheter"].append(float((vindhastighet_str)))
            
    return {år: data for år, data in gyldige_år.items() if len(data["vindhastigheter"])>=300}

def beregn_statistikk(gyldige_år):
    statistikk={"år":[], "maks_vindhastigheter":[], "median_vindhastigheter":[]}
    for år, data in gyldige_år.items():
        maks_vindhastighet=max(data["vindhastigheter"])
        median_vindhastighet=sorted(data["vindhastigheter"])[len(data["vindhastigheter"])//2]
        statistikk["år"].append(år)
        statistikk["maks_vindhastigheter"].append(maks_vindhastighet)
        statistikk["median_vindhastigheter"].append(median_vindhastighet)
    return statistikk

def plott_statistikk(statistikk):
    plt.figure(figsize=(10,6))
    plt.plot(statistikk["år"], statistikk["maks_vindhastigheter"], label="Høyeste middelvind")
    plt.plot(statistikk["år"], statistikk["median_vindhastigheter"], label="Median vindstyrke")
    plt.xlabel("År")
    plt.ylabel("Vindstyrke")
    plt.title("Høyeste middelvind og median vindstyrke for hvert år")
    plt.legend()
    plt.show()
    
filbane= "snodybde.csv"
data=les_data(filbane)
legg_til_år_kolonne(data)
gyldige_år=filtrer_gyldige_år(data)
statistikk=beregn_statistikk(gyldige_år)
plott_statistikk(statistikk)

                    
    


    