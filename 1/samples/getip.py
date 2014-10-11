############################################
# This file gives function getifip() which
# you can use to learn the IP address of the
# local system.
# Some code borrowed from:
# http://coderstalk.blogspot.com/2011/04/python-code-to-get-ip-address-from.html
############################################

# The necessary files
import socket, fcntl, struct

#############################################
# Retrieves the ip of the given network card.
# In this assignment, you may assume that 
# network adapter "eth0" is the one that is
# always being used.
# @param ifn - the name of the network card
# In this assignment, you can always set it
# to "eth0"
# @return - the string containing the IP 
# address of the current system.
##############################################
def getifip(ifn):
    	# Open the socket 
	sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# Grab the IP address of the current 
	# interface from the kernel. Convert
	# the original format to string format.
	return socket.inet_ntoa(fcntl.ioctl(sck.fileno(),0x8915,struct.pack(b'256s', ifn[:15]))[20:24])


print("The ip of the current system is: " + getifip(b"eth0"))
