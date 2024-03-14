#!/usr/bin/env python3

import ipdb
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
  
    def __init__(self, name='Bill', breed="Mastiff"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_param):
        if(type(name_param) is str) and 1 <= len(name_param) <= 25:
            self._name = name_param
        else: 
           print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, breed_param):
        if(breed_param in APPROVED_BREEDS):
            self._breed = breed_param
        else:
            print("Breed must be in list of approved breeds.")
        
    
