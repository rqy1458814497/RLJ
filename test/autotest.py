#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os

test_cases = ["apb"]
def clean_screen():
    print ('\n' * 100)

def change_dir(dir):
    os.chdir(os.getcwd() + "/" + dir)

def run_test(case):
    change_dir(case)
    ret_code = os.system("rlj")
    if ret_code != 0:
        clean_screen()
        print ("====================================")
        print ("Some thing wrong at test {0}".format(case))
        print ("====================================")
        exit(0)

for i in test_cases:
    run_test(i)