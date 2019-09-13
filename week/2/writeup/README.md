# Writeup 2 - OSINT

Name: *Sara Garcia-Beech*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Sara Garcia-Beech*

## Assignment Writeup

### Part 1 (45 pts)

I started looking at resources laid out in https://osintframework.com/. Using https://instantusername.com/#/ I found ejnorman84's Instagram profile (https://instagram.com/ejnorman84/), which gave me the information that his real name is Eric J Norman and that he works at Wattsamp Energy. The company website is http://wattsamp.net/. Searching for his name and company on LinkedIn led me to his profile here (https://www.linkedin.com/in/eric-norman-304550192/). Eric Norman is a power plant control specialist who used to work for BP and Koch Industries. I found another social media profile with https://usersearch.org/results_normal.php, his reddit, which can be found here (https://www.reddit.com/user/ejnorman84/comments/). Running "whois wattsamp.net" told me that the company address is 1300 Adabel Dr, El Paso 79835, TX, his phone number is 2026562837, and that his email is ejnorman84@gmail.com.

I then determined information regarding the website by going to https://securitytrails.com/domain/wattsamp.net/dns. The IP address is 157.230.179.99, and the server the website is running on is Apache 2.4.29. It is operated  by Digital Ocean, Inc, a cloud infrastructure provider. Looking at the network developer tools on the website determined that the server is running some instance of Ubuntu. Running the IP through https://www.onyphe.io/search/?query=157.230.179.99%C2%A0%C2%A0 determined that it corresponds to servers housed in North Bergen, New Jersey.

The website contains the hidden file robots.txt here (http://wattsamp.net/robots.txt). Running nmap on 157.230.179.99 determined that the following TCP services are running on the following ports:
- 22: ssh
- 25: smtp
- 80: http
- 110: pop3
- 119: nntp
- 143: imap
- 465: smtps
- 563: snews
- 587: smtp
- 993: imaps
- 995: pop3s
- 1337: kmscontrol


### Part 2 (75 pts)

Now that I had an email, an IP address and a list of potential ports, I began by attempting netcat connections with each. Upon resolving my difficulties with nmap, I determined that it was port 13367 to which I could establish a connection. After that, it was simply a matter of parsing the captcha with regex to send back the correct answer, and running a brute force attack by iterating through the passwords in rocky.txt to determine the right one.
