import classes.color as colormodule
import requests

def url_checker(url):
	try:
		get = requests.get(url)
		if get.status_code == 200:
			print(colormodule.colorsconsole.OKGREEN+"Api Online"+colormodule.colorsconsole.ENDC)
			return True
		else:
			print(colormodule.colorsconsole.FAIL+"Api Offline"+colormodule.colorsconsole.ENDC)
			return False
	except:
		print(colormodule.colorsconsole.FAIL+"Api Offline"+colormodule.colorsconsole.ENDC)
		smoothstop()
