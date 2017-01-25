import os
import sys

# files path
KEYBOARD_CONFIG = '/etc/default/keyboard'
NETWORK_CONFIG = '/etc/network/interfaces'
WPA_CONFIG = '/etc/wpa_supplicant/wpa_supplicant.conf'

# native file path
NATIVE_KEYBOARD_CONFIG = 'rpi/default/keyboard'
NATIVE_NETWORK_CONFIG = 'rpi/default/interfaces'
NATIVE_WPA_CONFIG = 'rpi/default/wpa_supplicant.conf'

# edited file path

EDITED_WPA_CONFIG = 'rpi/config/wpa_supplicant.conf'


# EDITING
REPLACE_SSID = 'sssid'
REPLACE_PSK = 'psskk'

## Commands
COMMAND_REMOVE_KEYBOARD_CONFIG = "sudo rm -rf " + KEYBOARD_CONFIG
COMMAND_REMOVE_NETWORK_CONFIG = "sudo rm -rf " + NETWORK_CONFIG
COMMAND_REMOVE_WPA_CONFIG = "sudo rm -rf " + WPA_CONFIG

# permissions
COMMAND_KEYBOARD_PERM = "sudo chmod 644 " + KEYBOARD_CONFIG
COMMAND_NETWORK_PERM = "sudo chmod 644 " + NETWORK_CONFIG
COMMAND_WPA_PERM = "sudo chmod 600 " + WPA_CONFIG

COMMAND_RASPI_CONFIG = "sudo raspi-config"

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
    os.system(COMMAND_REMOVE_KEYBOARD_CONFIG)
    shutil.copy2(NATIVE_KEYBOARD_CONFIG, KEYBOARD_CONFIG)

    # set permissions
    os.system(COMMAND_KEYBOARD_PERM)


def config_network():
	os.system(COMMAND_REMOVE_NETWORK_CONFIG)
	# copy new config
    shutil.copy2(NATIVE_NETWORK_CONFIG, NETWORK_CONFIG)

    #set permissions
    os.system(COMMAND_NETWORK_PERM)

def config_raspi():
    os.system(COMMAND_RASPI_CONFIG)

def config_wpa():
	# ask for user wifi and password
    ussid = raw_input("Enter your wifi ssid (name): ")
    upsk = raw_input("Enter your wifi password: ")
    # copy the native wpa conf to different folder for editing
    shutil.copy2(NATIVE_WPA_CONFIG, EDITED_WPA_CONFIG)
    # edit or replace the replaceable keywords with user wifi and password
    edit_wpa(EDITED_WPA_CONFIG, ussid, upsk)
    # copy to main dir
    shutil.copy2(EDITED_WPA_CONFIG, WPA_CONFIG)

    # set permissions
    os.system(COMMAND_WPA_PERM)

    os.remove(EDITED_WPA_CONFIG)

def terminate():
	sys.exit()

def edit_wpa(file_name, ssid, psk):
	with open(file_name, 'r') as f:
		new_lines = []
		for line in f.readlines():
			new_lines.append(line.replace(REPLACE_SSID, ssid))
			new_lines.append(line.replace(REPLACE_PSK, psk))
	with open(file_name, 'w') as f:
		for line in new_lines:
			f.write(line)


evaluate_choice = {'1' : config_keyboard, '2' : config_network, '3' : config_raspi, '4' : config_wpa, 'x' : terminate }

	

if __name__ == '__main__':
	main()