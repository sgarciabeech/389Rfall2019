# Writeup 6 - Binaries I

Name: *Sara Garcia-Beech*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Sara Garcia-Beech*

## Assignment Writeup

### Part 1 (50 pts)

CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)

The crackme program worked by running three successive checks on the different required inputs, and if they all passed, it returned the final flag. Rather than storing the flag as plaintext data, which would have been easy enough to find in the program's stored data, each check called the update_flag function with different parameters to perform bitwise operations on a stored mask. If it was called three times with the correct input, the flag was printed out in its final form.

The checks went in increasing order of difficulty. check1 looked for the existence of an argument run with checkme, and then checked to make sure that argument equaled "Oh God". If you had run `./checkme "Oh God"`, it passed. check2 looked for the existence of an environmental variable called FOOBAR. If FOOBAR existed, it loaded the value of FOOBAR into memory and checking that the value's length was 8. If this was true, it ran a character by character comparison check on the value of FOOBAR, making sure it was equal to " my eyes". It did this by loading the string "seye ym " from memory and running a character by character comparison, comparing the first and last characters, and so on. This check was passed by running `export FOOBAR=" my eyes"` in bash prior to running checkme. The last check, check3, first looked for the existence of a file named sesame in the current working directory. If such a file existed, it opened and tried to load the first 10 characters in that file. If the file had at least 10 characters, it performed a character by character string comparison, comparing the characters to their ASCII values in hexadecimal. For example, the zeroth and fifth characters had to be equivalent to ASCII 0x20, or the space character. Translating all the ASCII hex values and putting them in the right order revealed the string " they burn". Setting the contents of the sesame file equal to this string passed the final check, and the program printed out the final flag.
