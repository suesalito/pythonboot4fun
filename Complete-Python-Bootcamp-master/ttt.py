import os
import sys, time
import subprocess as sp

print ('Enter a file name:')
#filename = input()
filename = sys.stdin.readline()
print ('\r')




print (filename)



clear = lambda: os.system('clear')
def testwipe():
    for i in range(0, 31, 10):
        #filename = sys.stdin.read()
        sys.stdout.write('\r')
        sys.stdout.write("\033[F")
        sys.stdout.write('\r>> You have finished %d%%' % i,)
        sys.stdout.flush()
        time.sleep(0.5)

testwipe()

sys.stdout.write('hi there')
#sys.stdout.flush()
sys.stdout.write('\rBob here.')
clear()

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
clear_screen()
clear_screen()
clear_screen()


print('test')
print('test')
print('test')

from IPython.display import clear_output
clear_output()