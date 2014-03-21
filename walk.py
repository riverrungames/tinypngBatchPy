import os  
from os.path import dirname
from urllib.request import Request, urlopen
from base64 import b64encode

key = "in8vnZHN2i1ad_5hiwtTwqps1KSsCfbb"
#CaGJ3ruDxUfwkApZE4RwzmfG4ZkPGv22
#UqyBHn4Lh2N3aJszbWQuDy4qTHI9FGtp

# this folder is custom  
rootdir="."  
print("################################################################################")
for parent,dirnames,filenames in os.walk(rootdir):  
	# 
	for filename in filenames:
		#print("filename with full path:"+ os.path.join(parent,filename))
		
		if filename.find(".png") != -1 and parent.find(".svn") == -1:
			print("proceed "+os.path.join(parent,filename))
			#in8vnZHN2i1ad_5hiwtTwqps1KSsCfbb
			request = Request("https://api.tinypng.com/shrink", open(os.path.join(parent,filename), "rb").read())
			cafile = None
			
			auth = b64encode(bytes("api:" + key, "ascii")).decode("ascii")
			request.add_header("Authorization", "Basic %s" % auth)

			response = urlopen(request, cafile = cafile)
			if response.status == 201:
			  # Compression was successful, retrieve output from Location header.
			  result = urlopen(response.getheader("Location"), cafile = cafile).read()
			  open(os.path.join(parent,filename), "wb").write(result)
			  print(os.path.join(parent,filename)+" successed.")
			else:
			  # Something went wrong! You can parse the JSON body for details.
			  print(os.path.join(parent,filename)+" compression failed.")
	
print("################################################################################")