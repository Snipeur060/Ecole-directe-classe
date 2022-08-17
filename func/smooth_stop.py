import classes.color as colormodule
import os
def smoothstop():
		print(colormodule.colorsconsole.FAIL+"Press Enter to exit ..."+colormodule.colorsconsole.ENDC)
		input()
		os._exit(0)
