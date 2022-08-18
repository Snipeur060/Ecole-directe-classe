import http.client
import json
from func.checkurl import url_checker
from func.smooth_stop import smoothstop
import classes.color as colormodule
import os
from func.ecole import *
# System call
os.system("")

if __name__ == '__main__':
	#start main function
	result = url_checker("https://api.ecoledirecte.com")
	request_id()		
