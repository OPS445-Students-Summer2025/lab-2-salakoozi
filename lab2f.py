#!/usr/bin/env python3
#Author: Sohail Alakoozi
#Author ID: salakoozi
#Date Created: 2025/05/21

import sys

timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

if timer == 0:
    print('blast off!')
