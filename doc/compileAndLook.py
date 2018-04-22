#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import subprocess


def main():
    subprocess.call(('make', 'clean'))
    subprocess.call(('xelatex', 'learnCPlusPlus.tex'))
    subprocess.call(('bibtex',  'learnCPlusPlus.aux'))
    subprocess.call(('xelatex', 'learnCPlusPlus.tex'))
    subprocess.call(('xelatex', 'learnCPlusPlus.tex'))
    subprocess.call(('evince',  'learnCPlusPlus.pdf'))

if __name__ == '__main__':
    main()
