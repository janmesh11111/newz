from django.shortcuts import render

import requests

def home(request):
	if request.GET.get("btn"):
		try:
			a1 = "https://newsapi.org/v2/top-headlines"
			a2 = "?country=" + "in"
			a3 = "&apiKey=" + "dcf42dec7d614e778d3dcd8616ab8182"
			wa = a1 + a2 + a3
			res = requests.get(wa)
			
			data = res.json()
			
			info =data["articles"]
			return render(request,"home.html",{"msg":info})
		except Exception as e:
			print("issue",e)
			return render(request,"home.html",{"msg":e})
	else:
		return render(request,"home.html")
# Create your views here.
