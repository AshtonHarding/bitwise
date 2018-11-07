#!/usr/bin/env python2
#-*- coding: UTF-8 -*-

## Shifting bits.

left_bit = 0b10100111001

print("im so", str(left_bit)) # :^)

left_bit = left_bit <<  5
right_bit = 0b10100111001 << 5

print(bin(left_bit)," -> ",left_bit)
print(bin(right_bit)," -> ",right_bit)


## Bitwise AND...

answer = 0b0000101010
me_irl = 0b10100111001

print(answer, " & ", me_irl)
print("is", me_irl & answer) # Equates to 40
print("aka", bin(me_irl & answer)) # or rather 0b101000 more obviously.


## Bitwise OR

print(answer, " | ", me_irl)
print("is",me_irl | answer) # 1339
print("aka", bin(me_irl | answer) # 0b10100111011


## Bitwise XOR

print(me_irl ^ answer) # 1299
print(bin(me_irl ^ answer)) #  0b10100010011


## Bitwise NOT

print ~answer # -43
print ~me_irl # -1338

print bin(~answer) # -0b101011
print bin(~me_irl) # -0b10100111010


## Bit masking
def check_bit_4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"

## Turning on bits
a = 0b10111011
mask = 0b100

desired = a | mask

print(bin(desired))


## Quicker masking.
def flip_bit(number, n):
    result = number
    mask = (0b1 << n-1)
    result = result ^ mask
    return bin(result)

print flip_bit(0b111, 2) # Example
