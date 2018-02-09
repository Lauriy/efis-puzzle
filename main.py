# Encrypted with the same key
import random

from langdetect import detect

str_1 = 'SDZROZDBITGNUMYNSF'
str_2 = 'YHDRCRLBUTIPUCMFGF'

#        ***R***B*T**U****F
# These are characters that repeat on both occasions

# DEC 10 12 30 0 12 8 8 0 28 0 14 30 0 14 20 8 20 0
# HEX 0A 0C 1E 00 0C 08 08 00 1C 00 0E 1E 00 0E 14 08 14 00
# BIN 00001010 00001100 00011110 00000000 00001100 00001000 00001000 00000000 00011100 00000000 00001110 00011110 00000000 00001110 00010100 00001000 00010100 00000000
# BASE64 CgweAAwICAAcAA4eAA4UCBQA
# ASCII indecipherable
# xor = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str_1, str_2))

# Try numerical keys in case it's XORing with 42 again...
# Nonsense
# for i in range (0, 100):
#     print(' '.join(chr(ord(s) ^ i) for s in str_1))

# Nonsense
# for i in range (0, 100):
#     print(' '.join(chr(ord(s) ^ i) for s in str_2))

# Nonsense
# for i in range (0, 100):
#     print(' '.join(chr(ord(s) ^ i) for s in xor))

# en_symbol_frequency = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'g', 'p', 'y',
#                        'w', '\\r', 'b', '', '', '.', 'v', 'k', '-', '"', '_', "'", 'x', ')', '(', ';', '0', 'j', '1',
#                        'q', '=', '2', ':', 'z', '/', '*', '!', '?', '$', '3', '5', '>', '{', '}', '4', '9', '[', ']',
#                        '8', '6', '7', '\\', '+', '|', '&', '<', '%', '@', '#', '^', '`', '~']
#
# en_letter_frequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'g', 'p', 'y', 'w',
#                        'b', 'v', 'k', 'x', 'j', 'q', 'z']
#
# et_letter_frequency = 'A,E,I,S,T,L,U,N,K,D,O,M,R,V,G,H,J,P,Ä,Õ,B,Ü,Ö,F,Z,Q'.lower().split(',')

# str_1 [('S', 2), ('D', 2), ('Z', 2), ('N', 2), ('R', 1), ('O', 1), ('B', 1), ('I', 1), ('T', 1), ('G', 1), ('U', 1), ('M', 1), ('Y', 1), ('F', 1)]
# str_2 [('R', 2), ('C', 2), ('U', 2), ('F', 2), ('Y', 1), ('H', 1), ('D', 1), ('L', 1), ('B', 1), ('T', 1), ('I', 1), ('P', 1), ('M', 1), ('G', 1)]
# msg_frequency_dict = {}
# for symbol in str_2:
#     if symbol not in msg_frequency_dict:
#         msg_frequency_dict[symbol] = 1
#     else:
#         msg_frequency_dict[symbol] += 1
# msg_frequency_dict = sorted(msg_frequency_dict.items(), key=operator.itemgetter(1), reverse=True)

# ['S', 'D', 'Z', 'N', 'R', 'O', 'B', 'I', 'T', 'G', 'U', 'M', 'Y', 'F']
# ['R', 'C', 'U', 'F', 'Y', 'H', 'D', 'L', 'B', 'T', 'I', 'P', 'M', 'G']
# msg_symbol_frequency = [x[0] for x in msg_frequency_dict]

# EN symbols 'XnX XXnrlhuXtcoXXa' str_1
# EN symbols 'oin e srthldtecaua' str_2
# EN letters 'XsXeXXshdlmXauiXXo' str_1
# EN letters 'inseterhaldcatuomo' str_2
# ET letters 'XuXaXXukodvXirtXXs' str_1
# ET letters 'tluaeankidomiersvs' str_2
# decoded = []
# for symbol in str_2:
#     try:
#         decoded.append(et_letter_frequency[msg_symbol_frequency.index(symbol)])
#     except ValueError:
#         decoded.append('X')
# print(''.join(decoded))

# Try separating into words like this?
# str_1_sep = 'SDZR OZDB IT GNU MYNSF'
# str_2_sep = 'YHDR CRLB UT IPU CMFGF'

# f_1 = ['S', 'D', 'Z', 'N', 'Y', 'O', 'B', 'U', 'T', 'F', 'I', 'M', 'R', 'G']
# f_2 = ['R', 'C', 'U', 'F', 'Y', 'H', 'B', 'L', 'T', 'D', 'I', 'M', 'P', 'G']
# f_m = ['A', 'E', 'I', 'S', 'T', 'L', 'U', 'N', 'K', 'D', 'O', 'M', 'R', 'V']
# Try also with English
# Try longer Estonian replacement
# f_m = et_letter_frequency

# d_1 = []
# for symbol in str_1_sep:
#     if symbol == ' ':
#         d_1.append(symbol)
#     else:
#         d_1.append(f_m[f_1.index(symbol)])
# print(''.join(d_1))
#
# d_2 = []
# for symbol in str_2_sep:
#     if symbol == ' ':
#         d_2.append(symbol)
#     else:
#         d_2.append(f_m[f_2.index(symbol)])
# print(''.join(d_2))

# for i in range(0, 66666):
#     d_1 = []
#     for symbol in str_1_sep:
#         if symbol == ' ':
#             d_1.append(symbol)
#         else:
#             try:
#                 d_1.append(f_m[str_1_sep.index(symbol)])
#             except IndexError:
#                 d_1.append('X')
#     d_2 = []
#     for symbol in str_2_sep:
#         if symbol == ' ':
#             d_2.append(symbol)
#         else:
#             try:
#                 d_2.append(f_m[str_2_sep.index(symbol)])
#             except IndexError:
#                 d_2.append('X')
#     print(''.join(d_1))
#     print(''.join(d_2))
#     print('-----')
#     random.shuffle(f_m)

estonian_alphabet = 'A, B, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, Š, Z, Ž, T, U, V, Õ, Ä, Ö, Ü'.split(', ')
unique_symbols = ['S', 'D', 'Z', 'N', 'R', 'O', 'B', 'I', 'T', 'G', 'U', 'M', 'Y', 'F']

for i in range(0, 66666):
    d_1 = []
    for symbol in str_1:
        try:
            d_1.append(estonian_alphabet[unique_symbols.index(symbol)])
        except IndexError:
            d_1.append(' ')
    d_1 = ''.join(d_1)
    probable_lang = detect(d_1)
    if probable_lang == 'et':
        print(d_1)
    random.shuffle(estonian_alphabet)
