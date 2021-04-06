#!/usr/bin/env python3
import json
from netmiko import ConnectHandler
from getpass import getpass

# load the json file as a dictionary.
with open('vms.json') as f:
    data = json.load(f)

# Get pod information for connecting.
pod = input("Enter pod id: ")
podinfo = data['vms'][f"pod" + pod.lower()]
print(f"Connecting to pod {podinfo['id']} with the ip {podinfo['ip']}")
username = input("Username: ")
password = getpass("Password: ")
secret = getpass("Secret (Most likely the same as your password): ")

# Make a connection handler with the information provided plus the json.
virtualmachine = {
    'device_type': 'linux',
    'host':   podinfo['ip'],
    'username': username,
    'password': password,
    'port': 22,
    'secret': secret
}
connection = ConnectHandler(**virtualmachine)

# Use the information to connect, run command, and print it out. Then close connection.
connection.enable()
output = connection.send_command('dpkg --get-selections python3')
print(output)
connection.exit_enable_mode()