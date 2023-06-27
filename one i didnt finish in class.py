# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:44:08 2023

@author: kpenaalvarez


Pmt = r * PV/(1-(1+r)**-n)
Pmt is how much you pay back/mo
n is number of months
r is interest rate per month
n is number of months


"""
# putting """ after def and hitting enter gives you parameters
def Idunno(Pv, r, n):
    """


    Parameters
    ----------
    Pv : TYPE float
        DESCRIPTION. present value (amt you borrow)
    r : TYPE float
        DESCRIPTION. interest rate APR
    n : TYPE integer
        DESCRIPTION. number of months to pay back loan

    Returns
    -------
    Pmt : TYPE float
        DESCRIPTION. amt paid per month

    """
    Pmt =  r * PV/(1-(1+r)**-n)
    return Pmt
def computesPmt(Pmt, r, n):
    """

    Parameters
    ----------
    Pmt : TYPE float
        DESCRIPTION. how much i can afford monthly
    r : TYPE
        DESCRIPTION.
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    r = r/100 # convert apr to decimal
    r = r/12
    """
    Pv = (1-(1+r)**(-n)) * Pmt / r
    return Pv

#input the PV
import numpy as np

while(True):
    choice = int(input("enter choice 1 for PV, 2 for Pmt  ->  "))
    if (choice ==1 or choice == 2):
        break
else:
    print(f"enter a 1 or a 2, you entered {choice}")
    
if choice == 2:
    PV = input("enter PV: ")
    PV = float(PV)
    # equivalently PV = float(input("enter Pv: "))
    # \n creates a new line underneath
    print(f"PV = {PV} \n")
    
    r = input("interest (apr): ")
    r = float(r)/100
    r = r/12
    #  putting a : and 0.2 makes it round to two decimal places. ends in f
    print(f"interest rate = {r: 0.3f} \n")
    
    PV = computesPV(PV, r, n)
    PV = np.round(pmt, 2)
    print(f"payment is {Pv: } per month")
    
if choice == 1:
    Pmt = input('enter Pmt: ')
    Pmt = float(Pmt)
    print(f"Pmt = {Pmt} \n")
    
    r = input('interest APR: ')
    r = float(r/100)
    r = r/12 
    
    
    
    
