#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:34:58 2019

@author: alejo
"""
# First we use the euclidean algorithm 
# to compute lowest common multiply

def gcd(a,b):
    if a==b:
        return a
    if a < b:
        aux=a
        a=b
        b=aux
    mod = b
    rest= a%b
    while rest !=0:
        aux= rest
        rest=mod % rest
        mod= aux
    return mod

def lcm(a,b):
    lcm=abs(a*b)/gcd(a,b)
    return lcm

def ChocolatesByNumbers(N,M):
    lcm_choc=lcm(N,M)
    chocos= lcm_choc/M
    return chocos

print(ChocolatesByNumbers(10,4))
    