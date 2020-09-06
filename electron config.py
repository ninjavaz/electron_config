#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author: Dominik Nuszkiewicz
Electron config v1.0
Console application return configuration of electrons of given element.
Please, write int type number and press Enter.
Algorithm will return electron configuration of element, which has got given atomic number.
"""




import math


def e_config(atom_number): ##max 38 at.
    numb=1;
    s1=2;
    s2=2;
    p2=6;
    s3=2;
    p3=6;
    s4=2
    d3=10
    p4=6
    s5=2
    d4=10
    p5=6
    s6=2
    f4=14
    d5=10
    p6=6
    s7=2
    f5=14
    d6=10
    p7=6

    finish_list=[]
    list_of_e=[]
    for i in range(atom_number):
        if i+1>=0 and i+1<=s1:
            list_of_e.append('1s')
        if i+1>s1 and i+1<=(s1+s2):
            list_of_e.append('2s')
        if i+1>(s1+s2) and i+1<=(s1+s2+p2):
            list_of_e.append('2p')

        if i+1>(s1+s2+p2) and i+1<=(s1+s2+p2+s3):
            list_of_e.append('3s')

        if i+1>(s1+s2+p2+s3) and i+1<=(s1+s2+p2+s3+p3):
            list_of_e.append('3p')

        if i+1>(s1+s2+p2+s3+p3) and i+1<=(s1+s2+p2+s3+p3+s4):
            list_of_e.append('4s')

        if i+1>(s1+s2+p2+s3+p3+s4) and i+1<=(s1+s2+p2+s3+p3+s4+d3):#######26
            list_of_e.append('3d')
		
        if i+1>(s1+s2+p2+s3+p3+s4+d3) and i+1<=(s1+s2+p2+s3+p3+s4+d3+p4): #########36
            list_of_e.append('4p')
        
        if i+1>(s1+s2+p2+s3+p3+s4+d3+p4) and i+1<=(s1+s2+p2+s3+p3+s4+d3+p4+s5): #####34
            list_of_e.append('5s')
        
  

    finish_list.append("1s" + "^" +str(list_of_e.count('1s')))
    if list_of_e.count('2s')>0:
        finish_list.append("2s" + "^" +str(list_of_e.count('2s')))
    if list_of_e.count('2p')>0:
        finish_list.append("2p" + "^" +str(list_of_e.count('2p')))
    if list_of_e.count('3s')>0:
        finish_list.append("3s" + "^" +str(list_of_e.count('3s')))
    if list_of_e.count('3p')>0:
        finish_list.append("3p" + "^" +str(list_of_e.count('3p')))
    if list_of_e.count('4s')>0:
        finish_list.append("4s" + "^" +str(list_of_e.count('4s')))
    if list_of_e.count('3d')>0:
        finish_list.append("3d" + "^" +str(list_of_e.count('3d')))
    if list_of_e.count('4p')>0:
        finish_list.append("4p" + "^" +str(list_of_e.count('4p')))
    if list_of_e.count('5s')>0:
        finish_list.append("5s" + "^" +str(list_of_e.count('5s')))

    
    for a in finish_list:
        print(a, end=" ")
    print('\n')

while True:
    x=input('Podaj liczbę atomową pierwiastka: ')
    print("Oto jego konfiguracja elektronowa:")
    e_config(int(x))
 
