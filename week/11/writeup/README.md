# Writeup 1 - Web I

Name: *Sara Garcia-Beech*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Sara Garcia-Beech*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

This website was protected from SQL errors by checking that the input (the information after id= in the URL) did not contain the keywords 'or' or 'information', so although it did use blacklisting techniques, it did not appear to be sanitizing possible SQL input. Input of `id=1' -- comment'` returned the same thing as `id=1`, as the code was ignoring the information after the comment, rather than treating the whole input as the id tag. To get information about the SQL tables stored, an input similar to `1'; SELECT * FROM items; -- '`, with the right arguments, might execute the given SQL command.

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

Level 1:

Input: `<script>alert(0);</script>`

Since the HTML was processing the raw input, I could just insert a script tag to execute Javascript.

Level 2:

Input: `<img src="nope" onerror="alert(0);"/>`

Inputting a script tag did not work here, but Javascript can also be executed via image tags' onerror attribute.

Level 3:

Link: `https://xss-game.appspot.com/level3/frame#1.jpg' />";<script>alert(0);</script>`

The HTML was choosing the image to display based on the URL specifications, so by escaping the image tag and inserting a script tag, Javascript could be executed.

Level 4:

Input: `3' + alert(0) + '`

The raw input was being processed in the Javascript code, so by escaping a command and appending an alert, the alert would be executed.

Level 5:

Link: `https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(0)`

The next link chose where to go next with the href attribute, but href can also execute Javascript upon the click of the link.

Level 6:

Link: `https://xss-game.appspot.com/level6/frame#Https://www.google.com/jsapi?callback=alert`

The code loads the file from the URL argument, and although it checks the argument to make sure it doesn't start with http, it is case sensitive, whereas URLs are not.

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
