import json
import pygeoip
import re
import requests
import sys

# Global Variables
IP_ADDR = ''
IPV4_REGEX = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
IPV6_REGEX = r"""
	^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$|
	^::(?:[0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}$|
	^[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4}$|
	^[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:){0,4}[0-9a-fA-F]{1,4}$|
	^(?:[0-9a-fA-F]{1,4}:){0,2}[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:){0,3}[0-9a-fA-F]{1,4}$|
	^(?:[0-9a-fA-F]{1,4}:){0,3}[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:){0,2}[0-9a-fA-F]{1,4}$|
	^(?:[0-9a-fA-F]{1,4}:){0,4}[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:)?[0-9a-fA-F]{1,4}$|
	^(?:[0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4}::[0-9a-fA-F]{1,4}$|
	^(?:[0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}::$
	"""


def initial_input():
	"""
	Gets user initial input
	"""
	global IP_ADDR
	aux = input('Choose an option to start.\n\t[1] Geolocate your IP\n\t[2] Enter a different IP\n\n\t[0] Exit\n\nAnswer: ')

	while aux not in ["1","2","0"]:
		aux = input('\nPlease choose one of the options (1 to use your IP, 2 to enter a different IP)\nAnswer: ')

	if aux == "2":
		IP_ADDR = input('\nEnter the IP address: ')

		if len(re.findall(IPV4_REGEX, IP_ADDR)) > 0 or len(re.findall(IPV6_REGEX, IP_ADDR)) > 0:
			pass 
		else:
			while len(re.findall(IPV4_REGEX, IP_ADDR)) <= 0 and len(re.findall(IPV6_REGEX, IP_ADDR)) <= 0:
				IP_ADDR = input("Please enter a valid IPV4 or IPV6 address.\nAnswer: ")	

	return int(aux)


def display_info(json_response):
	"""
	Displays the information on the console
	"""
	print(json_response)


def main():
	print('Welcome to IPy 2 Geo!\n1')

	input_option = initial_input()

	if input_option	== 1:
		json_res = requests.get('https://ipinfo.io/json').json()
	elif input_option == 2:
		url = "https://ipinfo.io/{}/json".format(IP_ADDR)
		json_res = requests.get(url).json()
	else:
		print('Thank you for using IPy 2 Geo!')
		sys.exit(0)

	display_info(json_res)


if __name__ == "__main__":
	main()