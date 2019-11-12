# Writeup 9 - Forensics II

Name: *Sara Garcia-Beech*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Sara Garcia-Beech*


## Assignment details

### Part 1 (45 Pts)

1. Warmup: what IP address has been attacked?

142.93.136.81

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

The attackers were using nmap port scanning.

3. What are the hackers' IP addresses, and where are they connecting from?

159.203.113.181

4. What port are they using to steal files on the server?

Port 21, which listens for FTP requests.

5. Which file did they steal? What kind of file is it? Do you recognize the file?

They took findme.jpeg, a JPEG image file.

6. Which file did the attackers leave behind on the server?

They left greetz.fpff

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is not an option.

1337bank could implement PASV, or passive FTP, which is more secure than traditional FTP

### Part 2 (55 Pts)

1. When was greetz.fpff generated?

2019-03-27 00:15:05

2. Who authored greetz.fpff?

fl1nch

3. List each section, giving us the data in it and its type.

Section 1: ASCII Data
Section 2: Coordinates
Section 3: PNG
Section 4: ASCII Data
Section 5: ASCII Data

4. Report at least one flag hidden in greetz.fpff. Any other flag found will count as bonus points towards the competition portion of the syllabus.

CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
