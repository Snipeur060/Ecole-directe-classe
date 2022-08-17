import classes.color as colormodule
import http.client
import json
from func.smooth_stop import smoothstop
def request_id():
	msg1 = colormodule.colorsconsole.CBLUE2+"Veuillez entrer votre nom d'utilisateur École Directe: "+colormodule.colorsconsole.ENDC
	username = str(input(msg1))
	msg2 = colormodule.colorsconsole.OKCYAN+"Veuillez entrer votre mot de passe École Directe: "+colormodule.colorsconsole.ENDC
	password = str(input(msg2))
	res = traitement(username,password)
	jsondata(res)
	
def traitement(username,password):
	#def de la co
	conn = http.client.HTTPSConnection("api.ecoledirecte.com")
	#le payload pour renseigner les datas 
	payload = 'data={"identifiant":'+f'"{username}"'+',"motdepasse":'+f'"{password}"'+'}'
	# je def le headers (obligatoire) et je me fait passer pour chrome xd 
	headers = {
                'authority': 'api.ecoledirecte.com',
                'accept': 'application/json, text/plain, */*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-gpc': '1',
                'origin': 'https://www.ecoledirecte.com',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.ecoledirecte.com/',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
              }
	# on lance notre requête avec les valeurs ainsi que les headers
	conn.request("POST", "/v3/login.awp", payload, headers)
	#on get le result
	res = conn.getresponse()
	#on le transforme en format json (qui est possible à lire)
	data = res.read()
	# for debug print(data)
	return data
	
def jsondata(data):
	# on va traiter le json qui nous intéresse
	try:
		# bon ici j'explique pas. C'est juste allez-la ou le donné se trouve en empruntant le bon tunnel xd :-)
		code_classe = json.loads(data.decode("utf-8"))['data']['accounts'][0]['profile']['classe']['code']
		print(colormodule.colorsconsole.OKGREEN,colormodule.colorsconsole.BOLD,"Super nous avons réussi à trouver un code pour votre classe ",colormodule.colorsconsole.OKCYAN, code_classe ,colormodule.colorsconsole.ENDC," Note: ",colormodule.colorsconsole.BOLD,colormodule.colorsconsole.WARNING,"Toutes les personnes possédant le même code seront dans votre classe By PHOBOS Group")
		smoothstop()
	except:
		error = json.loads(data.decode("utf-8"))['code']
		if error == 505:
			# identifiants pas ok
			print(colormodule.colorsconsole.FAIL,colormodule.colorsconsole.BOLD,"Vos identifiants sont invalides",colormodule.colorsconsole.ENDC)
			smoothstop()
		else:
			# encore rien mis et je sais c'est chiant
			print(colormodule.colorsconsole.FAIL,colormodule.colorsconsole.BOLD,"La session école directe n'est pas encore activée veuillez patienter un petit peut jusqu'à son activation",colormodule.colorsconsole.ENDC)
			# for debug print(error)
			smoothstop()
	
