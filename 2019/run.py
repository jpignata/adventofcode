#!/usr/bin/env python3

import os
import timeit

for directory, _, files in sorted(os.walk('.')):
    if 'solve.py' in files:
        print('---', f'Day {directory[2:]}')

        if 'input.txt' in files:
            cmd = f'cat {directory}/input.txt | python3 {directory}/solve.py'
        else:
            cmd = f'python3 {directory}/solve.py'

        start = timeit.default_timer()
        os.system(cmd)
        elapsed = timeit.default_timer() - start
        print('---', 'Time:', elapsed, end='\n\n')
