<h1 align="center"><b>Generador de noms falsos amb Python</b></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GPL--3+" src="https://img.shields.io/badge/License-GPL--3+-yellow.svg" />
  </a>
  <a href="https://twitter.com/miquelnebot" target="_blank">
    <img alt="Twitter: Miquel Nebot" src="https://img.shields.io/twitter/follow/miquelnebot.svg?style=social" />
  </a>
</p>
<div align="center"><img src="https://user-images.githubusercontent.com/57944755/222732835-8c04b9fa-c89c-42fb-a12b-372d3d1638d0.png"></div>


# 👁️‍🗨️ Introducció

Generador de noms i llinatges falsos amb Python.

# 💻 Escenari
Kubuntu 22.04

# 0️⃣ Abans de començar
1. Haurem de tenir instal·lat Python en el nostre ordinador. Verificarem si disposam d'ell i la seva versió mitjançant la comanda següent a dins el Terminal (Ctrl+Alt+T): 

```console
user@kubuntu-mnebot:~$ python3 -V
```
Si no el tenim instal·lat, el podem aconseguir fàcilment amb la instrucció:
```console
user@kubuntu-mnebot:~$ sudo apt install python3
```
2. Per a la importació dels mòduls necessaris (**faker**) és imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per això, i si no ho hem fet amb anterioritat, l'instal·larem a través de la terminal de la següent manera:
```console
user@kubuntu-mnebot:~$ sudo apt install python3-pip
```
3. Instal·larem finalment els mòduls necessaris responsables de generar el codi QR sol·licitat:
```console
user@kubuntu-mnebot:~$ sudo pip install faker
```

# 👇 Descàrrega i execució
Copiarem el codi següent 👇 a un arxiu amb extensió **.py** al nostre ordinador (per exemple **generar_noms_python.py**) per a la seva posterior execució: 
<p></p>📝 Descàrrega de l'arxiu .py des d'<a href="https://github.com/miquelnebotaragon/generador_noms_falsos_python/blob/main/generar_noms_python.py" target="_blank">aquí</a>.

# 🏆 Vull saber-ne més
Desglossant el codi:
## Part 1:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import faker

```
Aquesta és la part inicial i més senzilla:
<p>· Enumeram els mòduls a importar, en aquest cas només un, faker.</p>


```python

# Variables:
num_elements = int(input("Introdueix la quantitat de noms i llinatges falsos a generar: "))
llista_noms = [fake.name() for _ in range(num_elements)]

```

<p>· Mostram en pantalla un text on sol·licitam a l'usuari que indiqui la quantitat de noms i llinatges falsos que vol generar.</p>
<p>· La segona variable s'emmagatzemarà de manera automàtica generant-se un llistat amb la quantitat indicada de noms falsos.</p>


```python

# Execució:
for elements in llista_noms:
    print(elements)

```

<p>· Finalment procedim a l'execució del programa imprimint en pantalla el llistat emmagatzemat a la segona variable.</p>


# ➕ Informació
1️⃣ L'arxiu **.py** ha estat comentat al detall 👆 per tal de possibilitar l'anàlisi del seu funcionament.<p></p>
2️⃣ Aquesta aplicació ha estat creada únicament amb finalitat d'estudi i divulgació. No em faig responsable dels possibles problemes ni perjudicis que pugui provocar el seu ús.<p></p>
