#Problem Restatement You have N bulbs in a row, each bulb has a switch.
# Bulbs are either:
# 0 → OFF
# 1 → ON
# Faulty wiring condition:
# If you press switch at index i, it toggles bulb i and every bulb to its right.
# Goal: Find the minimum number of switch presses needed to make all bulbs ON.

def BulbSwitch(arr):
    flip = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] ^ flip == 0:
            count += 1
            flip ^= 1
    return count