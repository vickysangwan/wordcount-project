from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request,'new.html')

# def homepage(request):
	# return HttpResponse('<a href="https://www.youtube.com/">click here</a>')
	# return HttpResponse(<h1>Vikas sangwan</h1>)
def count(request):
	fulltext=request.GET['fulltext']
	wordlist=fulltext.split()
	worddictionary={}
	for word in wordlist:
		if word in worddictionary:
			worddictionary[word]+=1
		else:
			worddictionary[word]=1
	sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
	# print(fulltext)
	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
	return render(request,'about.html')