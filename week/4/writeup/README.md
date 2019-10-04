# Writeup 2 - Pentesting

Name: *Sara Garcia-Beech*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Sara Garcia-Beech*

## Assignment Writeup

### Part 1 (45 pts)

The flag is:  CMSC389R-{p1ng_as_a_$erv1c3}  

I knew that UNIX commands can be chained together by separating them with semi-colons, so when the server prompted me for an IP address, I gave it "157.230.179.99; ls". This was successful, and gave me a list of the root directories. However, when I tried to list a specific directory, or do any command that required arguments, nothing happened. So I switched gears, and tried echoing the command injection and redirecting the input. This allowed me to add arguments to commands, and with some exploration of his file structure, I managed to find flag.txt and output its contents with:

`echo "157.230.179.99; cat home/flag.txt" | nc wattsamp.net 1337`

This is a major vulnerability of Eric's system and shows that he does little or no input checking or data sanitization. As a basic tenet of his server's security, he should assume that any input the server receives has the potential to hold malicious code or attacks, and should be treated accordingly. His server should be checking the inputs it receives to ensure they do not include potentially dangerous input, such as a semicolon to tack on another command. For the IP address input, he should only allow inputs that are formatted as IP addresses, that is to say, four numbers between 0 and 255 separated by periods. Anything else should be rejected. The other option would be to sanitize the input, so that even if his program accepted malicious input, data is treated only as data. In other words, even if the above command was used, "157.230.179.99; cat home/flag.txt" would be treated only as an IP address, with the escaped semicolon being treated only as a character, not as a command. Input fields are a major attack vector and potential weakness in any system, and any intelligent attacker will try to leverage them to access a system. Eric Norman has quite a way to go before he can call his server secure.

### Part 2 (55 pts)

The program I used to create an interactive shell can be found in stub.py. I began by making a basic shell that exited only with the commands exit or quit. I approached the various commands by creating a new connection for each command, which meant that the server state would not be saved between commands. This meant that I would have to keep track of the present working directory on my own. I would also have to make sure that each command was taking place in the present working directory, so I added a cd command before all commands to make sure the directory was correct. For the pull request, I tried running an scp command, but when that didn't yield good results, I switched gears. From the command line, I echoed the contents of the remote file and then redirected that output into the local file specified. This had the unfortunate downside of also adding the ping request information, but as a makeshift solution, it did its job. The only other command I took care of manually was the help command, which just printed the manual for the new commands. The rest of the commands were just sent directly to the server for its own shell to deal with, preceded by a cd command to ensure the right directory was set as the present working directory.
