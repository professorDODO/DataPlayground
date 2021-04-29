# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 00:08:07 2021

@author: roman
"""

import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

schule = ET.parse('../data/Schulanfaenger-Abgaenger_21111-0001.xml').getroot()
uni = ET.parse('../data/Studienanfaenger_21311-0012.xml').getroot()

#xml-File musste nach der "Adresse" durchsucht werden. Diese wurde gefunden
vSchule = schule[1][0][0][2]

#Speicherung der Schulanfänger und -absolventen in Arrays (M=männl.;W=weibl.)
anzAnf = []
anzAbs = []
anzAnfM = []
anzAbsM = []
anzAnfW = []
anzAbsW = []
for v in vSchule.iter():
    #Content = 1 entspricht Schulanfänger
    #Content = 2 entspricht Schulabsolventen
    if v.get('CONTENT') == '1':
        if '[%TOTAL%]' in v.get('COORDINATE'):
            anzAnf.append(int(v.get('ORIG')))
        if '[GESM]' in v.get('COORDINATE'):
            anzAnfM.append(int(v.get('ORIG')))
        if '[GESW]' in v.get('COORDINATE'):
            anzAnfW.append(int(v.get('ORIG')))
    if v.get('CONTENT') == '2':
        if '[%TOTAL%]' in v.get('COORDINATE'):
            anzAbs.append(int(v.get('ORIG')))
        if '[GESM]' in v.get('COORDINATE'):
            anzAbsM.append(int(v.get('ORIG')))
        if '[GESW]' in v.get('COORDINATE'):
            anzAbsW.append(int(v.get('ORIG')))

#Jahr hätte sich auch aus dem Datensatz ziehen lassen können, ist so aber schneller
jahr = list(range(1997, 2019 + 1))

#Relationen
# anzAnfRel = [anzAnfW[x] / anzAnfM[x] for x in anzAnfM[2:-1]]


#plot der Daten
plt.plot(jahr[2:-1], anzAnfW[2:-1], '-r', label='Schulanfängerinnen')
plt.plot(jahr[2:-1], anzAnfM[2:-1], '-b', label='Schulanfänger')
plt.plot(jahr[2:-1], anzAbsW[2:-1], '--r', label='Schulabsolventinnen')

plt.plot(jahr[2:-1], anzAbsM[2:-1], '--b', label='Schulabsolventen')
plt.legend(fontsize = 'small')
plt.ylabel('Anzahl')
plt.xlabel('Jahr')
plt.title('Schulanfänger:innen und -absolvent:innen in Deutschland')
plt.xticks(range(jahr[2], jahr[-1], 2))
plt.autoscale(enable=True, axis='x', tight=True)
plt.show()
