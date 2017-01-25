import os
import sys

# files path
KEYBOARD_CONFIG = '/etc/default/keyboard'

def main():
	print_menu()


def print_menu():
	print '========================================'
	print '|             RPi Script                '
	print '========================================'
	print ' '
	print ' 1. Change keyboard layout to US'
	print ' 2. Change network interface to dhcp'
	print ' 3. Start raspi-config'
	print ' 4. Edit wpa_supplicant [To switch network and WiFi password]'
	print ' ======================================='
	print ' x. Exit'
	print ' '

	option = raw_input('Enter your choice: ')
	evaluate_choice[option]()

# define the function blocks
def config_keyboard():
    print 'keyboard .\n'

def config_network():
    print 'network \n'

def config_raspi():
    print 'raspi \n'

def config_wifi():
    print 'wifi \n'

def terminate():
	sys.exit()


evaluate_choice = {'1' : config_keyboard, '2' : config_network, '3' : config_raspi, '4' : config_wifi, 'x' : terminate }

	

if __name__ == '__main__':
	main()