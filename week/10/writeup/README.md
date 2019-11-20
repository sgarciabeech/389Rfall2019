# Writeup 10 - Crypto I

Name: *Sara Garcia-Beech*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Sara Garcia-Beech*


## Assignment details

### Part 1 (45 Pts)

1. What is the structure of the ledger file format? Include exact byte offsets when static.

For each message, 16 bytes are allocated for the key hash, 16 for the cipher text hash, 16 random bytes, and then the cipher text itself.

2. What specific cryptographic implementations are used by the program? I.e. not "hashing", but a specific algorithm. Why might this pose a risk?

Messages written to the ledger.bin file are encrypted with aes128 symmetric encryption and then an md5 hash is created from that ciphertext. The ledger.bin file itself is encrypted with an md5 hash. This is problematic because both of these encryption algorithms are not considered strong enough anymore.

3. What information, if any, are you able to derive from ledger.bin without decrypting it at all?

The hashed key (hashed twice with md5) could be determined from reading the first 16 bytes.

4. How does the application ensure Confidentiality? How is the encryption key derived?  

Messages are passed through two layers of encryption with the aes128 encryption algorithm and the md5 hashing algorithm, so that the text stored in ledger.bin is illegible. The encryption key is derived by hashing a password with md5, taking the first two bytes of that output, and then hashing it again.

5. How does the application ensure Integrity? Is this flawed in any way?

The application checks both the key hash and the ciphertext hash in the ledger for equality against those of the given password to make sure both are equal. However, if both hashes were modified, the program would not be able to tell.

6. How does the application ensure Authenticity? Is this flawed in any way?

The application has a check to make sure the password is coming as a command line argument, but this is fairly weak security and can be falsified with backticks.

7. How is the initialization vector generated and subsequently stored? Are there any issues with this implementation?

It is stored with manual memory allocation functions, and if an attacker did a binary analysis of the heap during the execution of the program, data could potentially be read from there.

### Part 2 (45 Pts)

The flag is: CMSC389R-{k3y5p4c3_2_sm411}

### Part 3 (10 Pts)

Although I wouldn't go so far as to say companies should be posting their password encryption scripts on the Internet, I do see the point Kerckhoff's principle makes. Concealing every detail about your encryption works well in theory, but in a world where data breaches are common, it is smarter to assume that all information is publicly available and act accordingly. Furthermore, encryption software that is public can be more easily tested by many different hobbyists or experts, and the longer it goes without being cracked, the stronger it proves itself to be. Concealing the software only makes organizations overconfident about its strength, as it may not hold up to scrutiny outside of the organization.
