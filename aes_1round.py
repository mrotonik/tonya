import numpy as np
from copy import copy
vhod=[100,4,60,2,
      6,4,2,2,
      105,2,20,90,
      1,8,5,5]
print('Входной текст в десятичном:',vhod)
key=['21','f1','ab','11',
     '67','21','54','12',
     '23','23','21','23',
     '12','12','ab','18']
Sbox =np.array([
        ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
        ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
        ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
        ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
        ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
        ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
        ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
        ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
        ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
        ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
        ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
        ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
        ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
        ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
        ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87',' e9', 'ce', '55', '28', 'df'],
        ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']])
column = []
def Mix(test):
    column = []
    state = []
    def galoisMult(a, b):
        p = 0
        hiBitSet = 0
        for i in range(8):
            if b & 1 == 1:
                p ^= a
            hiBitSet = a & 0x80
            a <<= 1
            if hiBitSet == 0x80:
                a ^= 0x1b
            b >>= 1
        return p % 256
    def mixColumn(column):
        temp = copy(column)
        column[0] = galoisMult(temp[0], 2) ^ galoisMult(temp[3], 1) ^ \
                    galoisMult(temp[2], 1) ^ galoisMult(temp[1], 3)
        column[1] = galoisMult(temp[1], 2) ^ galoisMult(temp[0], 1) ^ \
                    galoisMult(temp[3], 1) ^ galoisMult(temp[2], 3)
        column[2] = galoisMult(temp[2], 2) ^ galoisMult(temp[1], 1) ^ \
                    galoisMult(temp[0], 1) ^ galoisMult(temp[3], 3)
        column[3] = galoisMult(temp[3], 2) ^ galoisMult(temp[2], 1) ^ \
                    galoisMult(temp[1], 1) ^ galoisMult(temp[0], 3)

    # mixColumns - это оболочка для mixColumn - генерирует «виртуальный» столбец из
    # таблица состояний и применяет странную математику Галуа
    def mixColumns(state):
        for i in range(4):
            column = []
            # создать столбец, взяв один и тот же элемент из каждой «виртуальной» строки
            for j in range(4):
                column.append(state[j * 4 + i])

            # применить mixColumn к нашей виртуальной колонке
            mixColumn(column)

            # перенести новые значения обратно в таблицу состояний
            for j in range(4):
                state[j * 4 + i] = column[j]
        return (state)
    return (mixColumns(test))

def sdvig(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst
def ShidtRows(test):
    t1=test[:4]
    t2=test[4:8]
    t3=test[8:12]
    t4=test[12:16]
    t2=sdvig(t2,-1)
    t3 = sdvig(t3, -2)
    t4 = sdvig(t4, -3)
    otvet=t1+t2+t3+t4
    return otvet
def sum(a,b):
    c=bin(int(a, 16))
    c1=bin(int(b, 16))
    c=c[-len(c)+2:]
    c1=c1[-len(c1)+2:]
    k1=''
    for i in range(8-len(c)):
        k1=k1+'0'
    #print(k1)
    c=k1+c
    k2=''
    for i in range(8-len(c1)):
        k2=k2+'0'
    #print(k2)
    c1=k2+c1
    ot='00000000'
    for i in range(len(c1)):
        i=int(i)
        if c1[i] != c[i]:
            ot=ot[:i]+str(1)+ot[i+1:]
        else:
            ot=ot[:i]+str(0)+ot[i+1:]
    ot=hex(int(ot, 2))
    if len(ot) == 4:
        ot = ot[-2:]
    elif len(ot) == 3:
        ot = '0' + ot[-1:]

    return ot
vuhid=np.array([])
for i in range(len(vhod)):#SubBytes
    ot=vhod[i]
    ot = hex(int(ot))
    if len(ot) == 4:
        ot = ot[-2:]
    elif len(ot) == 3:
        ot = '0' + ot[-1:]
    i1 = (int(ot[:1], 16))
    i2 = (int(ot[1:], 16))
    vuhid=np.append(vuhid,Sbox[i1,i2])
print('Поесле SybByte:',vuhid)#SybBytes
otvet=[]
for i in range(len(vuhid)):
    ot = vuhid[i]
    ot=int(ot,16)
    otvet.append(ot)
print('Переводим в 10',otvet)#SyBBytes в 10
otvet=ShidtRows(otvet)#ShiftRows
print('После ShiftRo:',otvet)
otvet=Mix(otvet)
print('Mix Colums:',otvet)
otvet1=[]#Для 16(после Mix Colums)
for i in range(len(otvet)):# В 16 система
    ot=otvet[i]
    ot = hex(int(ot))
    if len(ot) == 4:
        ot = ot[-2:]
    elif len(ot) == 3:
        ot = '0' + ot[-1:]
    otvet1.append(ot)
print('Mix Colums в 16',otvet1)#Печатаем
print('Ключ раунда:',key)#Наш ключик)
answer=[]
for i in range(len(otvet1)):
    a=otvet1[i]
    b=key[i]
    answer.append(sum(a,b))
print('Шифр после AddRoundRey:',answer)#


