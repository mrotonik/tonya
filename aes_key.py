import numpy as np
slovo=input('Введите 16 букв')
slovo=slovo.lower()
slovo=slovo.replace(' ', '')
slovo=slovo[:16]
Text=np.array([['а','e0'],
              ['б','e1'],
              ['в','e2'],
              ['г','e3'],
              ['д','e4'],
              ['е','e5'],
              ['є','ba'],
              ['ж','e6'],
              ['з','e7'],
              ['и','e8'],
              ['і','b3'],
              ['ї','bf'],
              ['й','e9'],
              ['к','ea'],
              ['л','eb'],
              ['м','ec'],
              ['н','ed'],
              ['о','ee'],
              ['п','ef'],
              ['р','f0'],
              ['с','f1'],
              ['т','f2'],
              ['у','f3'],
              ['ф','f4'],
              ['х','f5'],
              ['ц','f6'],
              ['ч','f7'],
              ['ш','f8'],
              ['щ','f9'],
              ['ь','fc'],
              ['ю','fe'],
              ['я','ff']])
w=np.array([['fa','f0','fc','ee'],
            ['ec','e5','ed','ea'],
            ['ee','ec','e8','ea'],
            ['88','e1','69','9b']])
k=[]
for i in range(16):
    k=slovo[i]
    w[int(i//4),int(i%4)]=k

for i in range(16):
    for i3 in range(32):
        if w[i//4,i%4]==Text[i3,0]:
            w[i//4,i%4]=Text[i3,1]












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


def dva_16(_value):
    return hex(int(_value, 2))


print('w0',w[0,])
w0=w[0,]
print('w1',w[1,])
w1=w[1,]
print('w2',w[2,])
w2=w[2,]
print('w3',w[3,])

w3=w[3,]
perem=w3[0]
w3=np.delete(w3,0)
#print(w3)
w3=np.append(w3,perem)
#print(w3)
z1=np.array([])
for i in range(len(w3)):
    pere=w3[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z1=np.append(z1,Sbox[i1,i2])
#print('замена:',z1)
z1[0]=sum(z1[0],'01')
print('z1',z1)
print('#################################')
###############################
z2=np.array([])
w4=np.array([])
w5=np.array([])
w6=np.array([])
w7=np.array([])
w3=w[3,]


for i in range(4):
    w4=np.append(w4,sum(w0[i],z1[i]))
    w5=np.append(w5,sum(w1[i],w4[i]))
    w6=np.append(w6,sum(w2[i],w5[i]))
    w7=np.append(w7,sum(w3[i],w6[i]))

w71=np.array(w7)
perem=w71[0]
w71=np.delete(w71,0)
w71=np.append(w71,perem)

for i in range(len(w7)):
    pere=w71[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z2=np.append(z2,Sbox[i1,i2])
print(z2)
z2[0]=sum(z2[0],'02')

print('w4 ',w4)
print('w5 ',w5)
print('w6 ',w6)
print('w7 ',w7)
print('z2', z2)
print('#################################')


################################

z3=np.array([])
w8=np.array([])
w9=np.array([])
w10=np.array([])
w11=np.array([])
for i in range(4):
    w8=np.append(w8,sum(w4[i],z2[i]))
    w9=np.append(w9,sum(w5[i],w8[i]))
    w10=np.append(w10,sum(w6[i],w9[i]))
    w11=np.append(w11,sum(w7[i],w10[i]))

w111=np.array(w11)
perem=w111[0]
w111=np.delete(w111,0)
w111=np.append(w111,perem)

for i in range(len(w7)):
    pere=w111[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z3=np.append(z3,Sbox[i1,i2])
z3[0]=sum(z3[0],'04')

print('w8 ',w8)
print('w9 ',w9)
print('w10 ',w10)
print('w11',w11)
print('z3', z3)
print('#################################')


################################

z4=np.array([])
w12=np.array([])
w13=np.array([])
w14=np.array([])
w15=np.array([])
for i in range(4):
    w12=np.append(w12,sum(w8[i],z3[i]))
    w13=np.append(w13,sum(w9[i],w12[i]))
    w14=np.append(w14,sum(w10[i],w13[i]))
    w15=np.append(w15,sum(w11[i],w14[i]))

w115=np.array(w15)
perem=w115[0]
w115=np.delete(w115,0)
w115=np.append(w115,perem)

for i in range(len(w7)):
    pere=w115[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z4=np.append(z4,Sbox[i1,i2])
z4[0]=sum(z4[0],'08')

print('w12 ',w12)
print('w13 ',w13)
print('w14 ',w14)
print('w15',w15)
print('z4', z4)
print('#################################')



################################

z5=np.array([])
w16=np.array([])
w17=np.array([])
w18=np.array([])
w19=np.array([])
for i in range(4):
    w16=np.append(w16,sum(w12[i],z4[i]))
    w17=np.append(w17,sum(w13[i],w16[i]))
    w18=np.append(w18,sum(w14[i],w17[i]))
    w19=np.append(w19,sum(w15[i],w18[i]))

w119=np.array(w19)
perem=w119[0]
w119=np.delete(w119,0)
w119=np.append(w119,perem)

for i in range(len(w7)):
    pere=w119[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z5=np.append(z5,Sbox[i1,i2])
z5[0]=sum(z5[0],'10')

print('w16 ',w16)
print('w17 ',w17)
print('w18 ',w18)
print('w19 ',w19)
print('z5', z5)
print('#################################')




################################

z6=np.array([])
w20=np.array([])
w21=np.array([])
w22=np.array([])
w23=np.array([])
for i in range(4):
    w20=np.append(w20,sum(w16[i],z5[i]))
    w21=np.append(w21,sum(w17[i],w20[i]))
    w22=np.append(w22,sum(w18[i],w21[i]))
    w23=np.append(w23,sum(w19[i],w22[i]))

w231=np.array(w23)
perem=w231[0]
w231=np.delete(w231,0)
w231=np.append(w231,perem)

for i in range(len(w7)):
    pere=w231[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z6=np.append(z6,Sbox[i1,i2])
z6[0]=sum(z6[0],'20')

print('w20 ',w20)
print('w21 ',w21)
print('w22 ',w22)
print('w23',w23)
print('z6', z6)
print('#################################')



z7=np.array([])
w24=np.array([])
w25=np.array([])
w26=np.array([])
w27=np.array([])
for i in range(4):
    w24=np.append(w24,sum(w20[i],z6[i]))
    w25=np.append(w25,sum(w21[i],w24[i]))
    w26=np.append(w26,sum(w22[i],w25[i]))
    w27=np.append(w27,sum(w23[i],w26[i]))

w271=np.array(w27)
perem=w271[0]
w271=np.delete(w271,0)
w271=np.append(w271,perem)

for i in range(len(w27)):
    pere=w271[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z7=np.append(z7,Sbox[i1,i2])
z7[0]=sum(z7[0],'40')

print('w24 ',w24)
print('w25 ',w25)
print('w26 ',w26)
print('w27',w27)
print('z7', z7)
print('#################################')



z8=np.array([])
w28=np.array([])
w29=np.array([])
w30=np.array([])
w31=np.array([])
for i in range(4):
    w28=np.append(w28,sum(w24[i],z7[i]))
    w29=np.append(w29,sum(w25[i],w28[i]))
    w30=np.append(w30,sum(w26[i],w29[i]))
    w31=np.append(w31,sum(w27[i],w30[i]))

w311=np.array(w31)
perem=w311[0]
w311=np.delete(w311,0)
w311=np.append(w311,perem)

for i in range(len(w27)):
    pere=w311[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z8=np.append(z8,Sbox[i1,i2])
z8[0]=sum(z8[0],'80')

print('w28 ',w28)
print('w29 ',w29)
print('w30 ',w30)
print('w31',w31)
print('z8', z8)
print('#################################')




z9=np.array([])
w32=np.array([])
w33=np.array([])
w34=np.array([])
w35=np.array([])
for i in range(4):
    w32=np.append(w32,sum(w28[i],z8[i]))
    w33=np.append(w33,sum(w29[i],w32[i]))
    w34=np.append(w34,sum(w30[i],w33[i]))
    w35=np.append(w35,sum(w31[i],w34[i]))

w351=np.array(w35)
perem=w351[0]
w351=np.delete(w351,0)
w351=np.append(w351,perem)

for i in range(len(w27)):
    pere=w351[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z9=np.append(z9,Sbox[i1,i2])
z9[0]=sum(z9[0],'1b')

print('w32 ',w32)
print('w33 ',w33)
print('w34 ',w34)
print('w35',w35)
print('z9', z9)
print('#################################')



z10=np.array([])
w36=np.array([])
w37=np.array([])
w38=np.array([])
w39=np.array([])
for i in range(4):
    w36=np.append(w36,sum(w32[i],z9[i]))
    w37=np.append(w37,sum(w33[i],w36[i]))
    w38=np.append(w38,sum(w34[i],w37[i]))
    w39=np.append(w39,sum(w35[i],w38[i]))

w391=np.array(w39)
perem=w391[0]
w391=np.delete(w391,0)
w391=np.append(w391,perem)

for i in range(len(w27)):
    pere=w391[i]
    i1=(int(pere[:1],16))
    i2=(int(pere[1:],16))
    z10=np.append(z10,Sbox[i1,i2])
z10[0]=sum(z10[0],'36')

print('w36 ',w36)
print('w37 ',w37)
print('w38 ',w38)
print('w39',w39)
print('z10', z10)
print('#################################')




w40=np.array([])
w41=np.array([])
w42=np.array([])
w43=np.array([])
for i in range(4):
    w40=np.append(w40,sum(w36[i],z10[i]))
    w41=np.append(w41,sum(w37[i],w40[i]))
    w42=np.append(w42,sum(w38[i],w41[i]))
    w43=np.append(w43,sum(w39[i],w42[i]))
print('w40 ',w40)
print('w41 ',w41)
print('w42 ',w42)
print('w43',w43)

slovo1=np.hstack((w0,w1,w2,w3))
slovo2=np.hstack((w4,w5,w6,w7))
slovo3=np.hstack((w8,w9,w10,w11))
slovo4=np.hstack((w12,w13,w14,w15))
slovo5=np.hstack((w16,w17,w18,w19))
slovo6=np.hstack((w20,w21,w22,w23))
slovo7=np.hstack((w24,w25,w26,w27))
slovo8=np.hstack((w28,w29,w30,w31))
slovo9=np.hstack((w32,w33,w34,w35))
slovo10=np.hstack((w36,w37,w38,w39))
slovo11=np.hstack((w40,w41,w42,w43))
print(slovo11)