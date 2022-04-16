#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2022, Noa Velasco

from random import choice


player = input('Elige:\n(r)/(s)/(p)')
computer = choice(['p', 'r', 's'])
victoria = [('r', 's'), ('s', 'p'), ('p', 'r')]

if (player, computer) in victoria:
    print('You won!')
elif player == computer:
    print('It\'s a tie.')
else:
    print('You lost.')
