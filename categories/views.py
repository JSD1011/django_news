from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    records={}
    url = requests.get('https://inshortsapi.vercel.app/news?category=world')
    mydata = url.json()
    records['allnewsdata'] = mydata
    return render(request,'index.html',records)

def top(request):
    records={}
    url = requests.get('https://inshortsapi.vercel.app/news?category=business')
    mydata_two = url.json()
    records['topnewsdata'] = mydata_two
    return render(request,'top.html',records)
def trending(request):
    records ={}
    url = requests.get('https://inshortsapi.vercel.app/news?category=politics')
    mydata_three = url.json()
    records['trendingdata'] = mydata_three
    return render(request,'trending.html',records)

def science(request):
    records={}
    url = requests.get('https://inshortsapi.vercel.app/news?category=science')
    mydata_four = url.json()
    records ['sciencedata'] = mydata_four
    return render(request,'science.html',records)

def ep(request):
    records = {}
    url = requests.get('https://inshortsapi.vercel.app/news?category=entertainment')
    mydata_fifth = url.json()
    records ['epdata'] = mydata_fifth
    return render(request,'ep.html',records)

def sports(request):
    records = {}
    url = requests.get('https://inshortsapi.vercel.app/news?category=sports')
    mydata_sixth = url.json()
    records ['sportsdata'] = mydata_sixth
    return render(request,'sports.html',records)