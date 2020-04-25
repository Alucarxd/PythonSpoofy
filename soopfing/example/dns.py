#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:49:56 2020

@author: colored
"""
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def main():
    if parser.target:
        try:
            objetivo = requests.get(url=parser.target)
            header = dict(objetivo.headers)
            for x in header:
                print(x+ ":"+header[x])
        except:
            print("No me pude conectar")
    else:
        print("Escribe bien el objetivo")
if __name__ == '__main__':
    main()
                