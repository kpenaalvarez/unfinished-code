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
def computesPmt(PV, r, n):
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
    r = r/100 # convert apr to decimal
    r = r/12
    
    Pmt =  r * PV/(1-(1+r)**-n)
    return Pmt

def computesPV(Pmt, r, n):
    """
compute how much money you can borrow
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
    """
    r = r/100 # convert apr to decimal
    r = r/12

    Pv = (1-(1+r)**(-n)) * Pmt / r
    return Pv

#input the PV
import numpy as np

while(True):
    choice = int(input("enter choice 2 for PV, 1 for Pmt  ->  "))
    if (choice ==1 or choice == 2):
        break
    else:
        print(f"enter a 1 or a 2, you entered {choice}")
        
    
if choice == 1:
    PV = input("enter PV: ")
    PV = float(PV)
    # equivalently PV = float(input("enter Pv: "))
    # \n creates a new line underneath
    print(f"PV = {PV} \n")
    
    r = float(input("interest (apr): "))
    #  putting a : and 0.2 makes it round to two decimal places. ends in f
    print(f"interest rate = {r: 0.3f} \n")
    
    n = int(input('how many months:  '))
    print(f"\nn = {n} months\n")
    
    pmt = computesPmt(PV, r, n)
    pmt = np.round(pmt, 2)
    print(f"payment is {pmt: } per month")
    
if choice == 2:
    
    Pmt = input('enter Pmt: ')
    Pmt = float(Pmt)
    print(f"Pmt = {Pmt} \n")
    
    r = float(input("interest (apr): "))
    #  putting a : and 0.2 makes it round to two decimal places. ends in f
    print(f"interest rate = {r: 0.3f} \n")
    
    n = int(input('how many months:  '))
    print(f"\nn = {n} months\n")
   
    PV = computesPV(Pmt, r, n)
    PV = np.round(PV, 2)
    print(f"amt I can borrow {PV: } per month")
    
    
    
    

