import classes.color as colormodule
import os
#cette fonction permet de stopper d'une manière plutôt calme le processus
def smoothstop():
		print(colormodule.colorsconsole.FAIL+"Press Enter to exit ..."+colormodule.colorsconsole.ENDC)
		input()
		os._exit(0)
