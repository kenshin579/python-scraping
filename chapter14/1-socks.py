import socks
import socket
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())

'''
Tor 설치
># brew install tor 

https://kremalicious.com/simple-tor-setup-on-mac-os-x/

Running Tor
># tor.sh

'''
