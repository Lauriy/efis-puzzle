# from collections import Counter
import random

# m6istatus = 'df 4c 2f d7 45 7d c1 40 31 df 48 39 2e 09 30 d7 5d 2e d3 45 7d d9 dc 2f c4 48 39'

# print(' '.join([str(int(tykk, 16)) for tykk in m6istatus.split(' ')]))
from collections import deque

from langdetect import detect

kymnendik = '223 76 47 215 69 125 193 64 49 223 72 57 46 9 48 215 93 46 211 69 125 217 220 47 196 72 57'

# XOR
# ascii = 'ßL/×E}Á@1ßH9.	0×].ÓE}ÙÜ/ÄH9'
# for i in range (0, 256):
#     print(' '.join(chr(ord(s) ^ i) for s in ascii))

# eesti_sagedus = 'A,E,I,S,T,L,U,N,K,D,O,M,R,V,G,H,J,P,Ä,Õ,B,Ü,Ö,F,Z,Q'.lower().split(',')

# m6istatuse_sagedused = Counter(kymnendik.split(' '))
# Counter({'223': 2, '47': 2, '215': 2, '69': 2, '125': 2, '72': 2, '57': 2, '46': 2, '76': 1, '193': 1, '64': 1,
# '49': 1, '9': 1, '48': 1, '93': 1, '211': 1, '217': 1, '220': 1, '196': 1})
# print(m6istatuse_sagedused)

ascii_komplekt = [chr(x) for x in range(256)]
kymnendik_arvudena = [int(x) for x in kymnendik.split(' ')]

ascii_deque = deque(ascii_komplekt)
for i in range(0, 256):
    asendatud = ''.join([ascii_deque[x] for x in kymnendik_arvudena])
    print(asendatud)
    ascii_deque.rotate(1)

#
# for i in range(0, 100000):
#     random.shuffle(ascii_komplekt)
#     asendatud = ''.join([ascii_komplekt[x] for x in kymnendik_arvudena])
#     arvatav_keel = detect(asendatud)
#     if arvatav_keel == 'et':
#         print(asendatud)