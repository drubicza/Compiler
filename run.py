#!/usr/bin/env python
import os, random, time, unittest, os, sys, subprocess
from time import sleep
import sys, py_compile, struct, imp
from time import sleep
H = '\x1b[95m'
B = '\x1b[94m'
G = '\x1b[92m'
W = '\x1b[93m'
F = '\x1b[91m'
E = '\x1b[0m'
U = '\x1b[4m'
O = '\x1b[33m'
LL = '\x1b[1;38;5;228m'
HB = '\x1b[1;38;5;32m'
RR = '\x1b[1;38;5;225m'
ll = '\x1b[1 38;5;223'
R = '\x1b[31;1m'
Y = '\x1b[33m'
reload(sys)
sys.setdefaultencoding('utf-8')

def clear():
    if sys.platform == 'linux2':
        os.system('clear')
    else:
        if sys.platform == 'win32':
            print 'ERROR'
            sleep(2)
            quit()
        else:
            print 'ERROR'
            sleep(2)
            quit()


def Banner():
    print '\x1b[31;1m'
    print '\n   ______                      _ __\n  / ____/___  ____ ___  ____  (_) /__  _____\n / /   / __ \\/ __ `__ \\/ __ \\/ / / _ \\/ ___/\n/ /___/ /_/ / / / / / / /_/ / / /  __/ /\n\\____/\\____/_/ /_/ /_/ .___/_/_/\\___/_/ \x1b[0;37m\x1b[04mv1.0\x1b[00m\n\x1b[31;1m                    /_/'


def info():
    print HB + 'Author   \x1b[31;1m\xc2\xbb \x1b[33mGunadiCBR\n\x1b[1;38;5;32mVersion  \x1b[31;1m\xc2\xbb \x1b[33m1.0\n\x1b[1;38;5;32mPlatform \x1b[31;1m\xc2\xbb \x1b[33mpython2.7\n\x1b[1;38;5;32mGithub   \x1b[31;1m\xc2\xbb \x1b[33mhttps://github.com/afelfgie\n'


def ch1():
    print '\x1b[31;1m[\x1b[32;1m01\x1b[31;1m] \x1b[35;1m> \x1b[37;1mStart\n\x1b[31;1m[\x1b[32;1m02\x1b[31;1m] \x1b[35;1m> \x1b[37;1mExit\n'


def main():
    clear()
    Banner()
    info()
    ch1()
    try:
        com = raw_input('\x1b[31;1m[\x1b[33;1m*\x1b[31;1m] \x1b[37;0m\x1b[04mChoose\x1b[00m --> \x1b[33;1m')
    except:
        main()

    if com == '01' or com == '1':
        main2()
    else:
        if com == '02' or com == '2':
            print ' '
            print '\x1b[31;1m[\x1b[33;1m-\x1b[31;1m] \x1b[31;1mExiting Program'
            print ' '
            sleep(1.5)
            quit()
        else:
            main()


def main2():
    clear()
    Banner()
    info()
    try:
        ch = raw_input('\x1b[31;1m[\x1b[33;1m*\x1b[31;1m] \x1b[37;1mFile Name: \x1b[33;1m')
    except:
        main2()

    os.system("python2 main.py '" + ch + "'")
    print ' '
    print '\x1b[31;1m[\x1b[33;1m*\x1b[31;1m] \x1b[37;0mCompiling ' + ch + ' ...'
    sleep(2)
    print ' '
    print '\x1b[31;1m[\x1b[33;1m*\x1b[31;1m] \x1b[31mD\x1b[32mO\x1b[33mN\x1b[34mE \x1b[37;1m...'
    sleep(1)
    quit()


main()
