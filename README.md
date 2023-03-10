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


# 馃憗锔忊?嶐煑笍 Introducci贸

Generador de noms i llinatges falsos amb Python.

# 馃捇 Escenari
Kubuntu 22.04

# 0锔忊儯 Abans de comen莽ar
1. Haurem de tenir instal路lat Python en el nostre ordinador. Verificarem si disposam d'ell i la seva versi贸 mitjan莽ant la comanda seg眉ent a dins el Terminal (Ctrl+Alt+T): 

```console
user@kubuntu-mnebot:~$ python3 -V
```
Si no el tenim instal路lat, el podem aconseguir f脿cilment amb la instrucci贸:
```console
user@kubuntu-mnebot:~$ sudo apt install python3
```
2. Per a la importaci贸 dels m貌duls necessaris (**faker**) 茅s imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per aix貌, i si no ho hem fet amb anterioritat, l'instal路larem a trav茅s de la terminal de la seg眉ent manera:
```console
user@kubuntu-mnebot:~$ sudo apt install python3-pip
```
3. Instal路larem finalment els m貌duls necessaris pel funcionament d'aquest programa de Python:
```console
user@kubuntu-mnebot:~$ sudo pip install faker
```

# 馃憞 Desc脿rrega i execuci贸
Copiarem el codi seg眉ent 馃憞 a un arxiu amb extensi贸 **.py** al nostre ordinador (per exemple **generar_noms_python.py**) per a la seva posterior execuci贸: 
<p></p>馃摑 Desc脿rrega de l'arxiu .py des d'<a href="https://github.com/miquelnebotaragon/generador_noms_falsos_python/blob/main/generar_noms_python.py" target="_blank">aqu铆</a>.

# 馃弳 Vull saber-ne m茅s
Desglossant el codi:
## Part 1:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# M貌duls a importar:
import faker

```
Aquesta 茅s la part inicial i m茅s senzilla:
<p>路 Enumeram els m貌duls a importar, en aquest cas nom茅s un, faker.</p>


```python

# Variables:
num_elements = int(input("Introdueix la quantitat de noms i llinatges falsos a generar: "))
llista_noms = [fake.name() for _ in range(num_elements)]

```

<p>路 Mostram en pantalla un text on sol路licitam a l'usuari que indiqui la quantitat de noms i llinatges falsos que vol generar.</p>
<p>路 La segona variable s'emmagatzemar脿 de manera autom脿tica generant-se un llistat amb la quantitat indicada de noms falsos.</p>

## Part 2:
```python

# Execuci贸:
for elements in llista_noms:
    print(elements)

```

<p>路 Finalment procedim a l'execuci贸 del programa imprimint en pantalla el llistat emmagatzemat a la segona variable.</p>


# 鉃? Informaci贸
1锔忊儯 L'arxiu **.py** ha estat comentat al detall 馃憜 per tal de possibilitar l'an脿lisi del seu funcionament.<p></p>
2锔忊儯 Aquesta aplicaci贸 ha estat creada 煤nicament amb finalitat d'estudi i divulgaci贸. No em faig responsable dels possibles problemes ni perjudicis que pugui provocar el seu 煤s.<p></p>
