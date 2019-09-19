Writeup 1 - OPSEC and Social Engineering
======

Name: *Sara Garcia-Beech*  
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Sara Garcia-Beech*

## Assignment Writeup

### Part 1

I would first approach Eric by calling him pretending to be from his mother's life insurance company. As one of her beneficiaries, there are some things that I would like to clarify with him first. I would say that she has had some issues filling out the information and she directed us to him to help clarify things. To verify it is him I am talking to, I would ask him to answer two security questions. One is about what his mother's maiden name is, and the other one is what her first pet's name was. Off-hand, I could ask what browser she uses, because maybe that had something to do with the issues she was having. Whatever the browser is, I make up something about our website having issues with compatibility with that browser. To build credibility, I would ask him to verify some information about his mother that I had already found through OSINT (her current address, past employment, that sort of thing). When talking about her current addresses, I would ask if there were any other addresses she has held in the past. If that doesn't elicit the answer to her hometown, I would ask if she's always lived in whatever state she currently resides in, making it seem that I'm just making polite small talk. Moving onto the financial information, I say that the life insurance policy has her bank information on records, but we want to make sure that he has access as well. I make some joke about how I'm always forgetting my ATM PIN to break tension, since talking money can make people uncomfortable. Hopefully, this discomfort prompts Eric to bring up some important information regarding the PIN. Given that his mother is older, it is likely that she chose an important set of numbers, such as a birthday or anniversary. If I can learn what the numbers mean, I might be able to find them out with OSINT. If this doesn't work, I can ask Eric to verify a PIN for one of her accounts. He will presumably correct me, and I will explain it as having read from the wrong line on my screen. I will conclude by recapping the conversation and asking him if he has any questions for me.

### Part 2

- One major vulnerability was how easily a brute force attack worked. I would suggest he change his firewall rules to reject more than three unsuccessful connections from the same IP address. This would not fix all possible brute force attacks, as an attacker could find ways to spoof their IP address, but it would at least require more sophisticated attacks.
- Another major vulnerability was the weakness of the password. I would suggest Eric add requirements for all his passwords. Although common wisdom has it that passwords should consist of upper and lowercase letters, numbers, and symbols, the more critical bit is length, at least 12 characters long. I would also suggest he avoid common words and names. Ideally, I would tell him to look into implementing two factor authentication on his website and server, to add an extra layer of security.
- The fact that all the details of his domain's registration (address, email, phone number, etc) were available with a simple whois query is a major vulnerability. I would suggest he look into using a private registration and/or hosting service, which would replace his own contact information with their own. This also has the benefit that some services automatically provide different security options, which he clearly needs.
