import os, json, sys

cwd = os.getcwd()

print(cwd)

jsonfile = json.load(open("manifest.json",'r'))
scripts = jsonfile['background']['scripts']
for s in scripts:
	print(cwd+"/"+s)
	if(os.access(cwd+s, os.R_OK)):
		raise ValueError
		break
	else:
		print("OK")
