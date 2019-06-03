#!/usr/bin/python3
import os
import datetime

login = os.getlogin()
status = os.system('systemctl status openvpn')
restart = os.system('systemctl restart openvpn')

print(datetime.datetime.now())
print(login)
print(status)
