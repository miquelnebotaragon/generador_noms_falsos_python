#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
from faker import Faker
fake = Faker('es_ES')

# Variables:
num_elements = int(input("Introdueix la quantitat de noms i llinatges falsos a generar: "))
llista_noms = [fake.name() for _ in range(num_elements)]

# Execució:
for elements in llista_noms:
    print(elements)
