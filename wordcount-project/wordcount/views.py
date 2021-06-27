from django.http import HttpResponse
from django.shortcuts import render
import operator

def Home(Request):

	return render(Request, "Home.html")

def Contact(Request):

		return HttpResponse("<h1>Hello there</h1></br> you can contact us on +91 79800-56599")

def Count(Request):
	FullText = Request.GET['FullText']

	print(FullText)

	wordlist=FullText.split()
	Totalcount=len(wordlist)
	dictionary={}
	for word in wordlist:
		if word in dictionary:
			dictionary[word]=dictionary[word]+1
		else:
			dictionary[word]=1
			worddict=dictionary
			leest = sorted(dictionary.items(), key = operator.itemgetter(1), reverse = True)
	return render(Request, "Count.html", {'FullText': FullText, 'Count': Totalcount, 'leest' : leest})


def About(Request):
	return render(Request, "About.html")