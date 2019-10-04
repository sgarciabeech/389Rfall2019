# Writeup 2 - Pentesting

Name: *Sara Garcia-Beech*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Sara Garcia-Beech*

## Assignment Writeup

### Part 1 (45 pts)

The flag is:  CMSC389R-{p1ng_as_a_$erv1c3}  

I knew that UNIX commands can be chained together by separating them with semi-colons, so when the server prompted me for an IP address, I gave it "157.230.179.99; ls". This was successful, and gave me a list of the root directories. However, when I tried to list a specific directory, or do any command that required arguments, nothing happened. So I switched gears, and tried echoing the command injection and redirecting the input. This allowed me to add arguments to commands, and with some exploration of his file structure, I managed to find flag.txt and output its contents with:

echo ""157.230.179.99; cat home/flag.txt" | nc wattsamp.net 1337

This is a major vulnerability of Eric's system and shows that he does little or no input checking or data sanitization. His server should be checking the inputs it receives to ensure they do not include potentially dangerous input, such as a semicolon to tack on another command. For the IP address input, he should only allow inputs that are formatted as IP addresses, that is to say, four numbers between 0 and 255 separated by periods. Anything else should be rejected. The other option would be to sanitize the input, so that even if his program accepted malicious input, data is treated only as data.

### Part 2 (55 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
