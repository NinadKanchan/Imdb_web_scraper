import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyfiglet
import sys
''' 
IMDb top & popular content scraper
'''
linkToImdb={
'topratedmovie':"https://www.imdb.com/chart/top/?ref_=nv_mv_250",
'mostpopularmovie':"https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm",
'topratedtv':"https://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=Y90GWSEZQ29895M1D1QA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=tvmeter&ref_=chttvm_ql_6",
'mostpopulartv':"https://www.imdb.com/chart/tvmeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=MT8K17M94A9ABJSYPJV2&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_ql_5"
}

def topMovie():
	headers={"Accept-Language":"en-US ,en;q=0.5"}
	url=linkToImdb["topratedmovie"]
	results=requests.get(url,headers=headers)
	soup=BeautifulSoup(results.text,"html.parser")

	titles=[]
	year=[]
	director=[]
	starring=[]
	imdb_rating=[]

	movie_td=soup.find_all('td',class_='titleColumn')
	rating_td=soup.find_all('td',class_='ratingColumn imdbRating')

	for container in movie_td:
		titles.append(container.a.text)
		year.append(container.span.text)
		director.append(container.a.attrs['title'].split(',')[0])
		starring.append(','.join(container.a.attrs['title'].split(',')[1:]))
		if(len(titles)==50):
			break
	for tag in rating_td:
		if(tag.strong):
			imdb_rating.append(tag.strong.text)
		else:
			imdb_rating.append('-')
		if(len(imdb_rating)==50):
			break
	def tabularMovie():
		table=pd.DataFrame(
		{
		'movie':titles,
		'year':year,
		'cast':starring,
		'director':director,
		'rating':imdb_rating
		})
		table['year']=table['year'].str.extract('(\d+)').astype(int)
		table['rating']=pd.to_numeric(table['rating'],errors='coerce')
		return table
	chart=tabularMovie()
	#chart.to_csv('test.csv')
	print(chart)

def popularMovie():
	headers={"Accept-Language":"en-US ,en;q=0.5"}
	url=linkToImdb["mostpopularmovie"]
	results=requests.get(url,headers=headers)
	soup=BeautifulSoup(results.text,"html.parser")

	titles=[]
	year=[]
	director=[]
	starring=[]
	imdb_rating=[]

	movie_td=soup.find_all('td',class_='titleColumn')
	rating_td=soup.find_all('td',class_='ratingColumn imdbRating')

	for container in movie_td:
		titles.append(container.a.text)
		year.append(container.span.text)
		director.append(container.a.attrs['title'].split(',')[0])
		starring.append(','.join(container.a.attrs['title'].split(',')[1:]))
		if(len(titles)==50):
			break
	for tag in rating_td:
		if(tag.strong):
			imdb_rating.append(tag.strong.text)
		else:
			imdb_rating.append('-')
		if(len(imdb_rating)==50):
			break
	def tabularMovie():
		table=pd.DataFrame(
		{
		'movie':titles,
		'year':year,
		'cast':starring,
		'director':director,
		'rating':imdb_rating
		})
		table['year']=table['year'].str.extract('(\d+)').astype(int)
		table['rating']=pd.to_numeric(table['rating'],errors='coerce')
		return table
	chart=tabularMovie()
	#chart.to_csv('test.csv')
	print(chart)

def topTv():
	headers={"Accept-Language":"en-US ,en;q=0.5"}
	url=linkToImdb["topratedtv"]
	results=requests.get(url,headers=headers)
	soup=BeautifulSoup(results.text,"html.parser")

	titles=[]
	year=[]
	starring=[]
	imdb_rating=[]

	movie_td=soup.find_all('td',class_='titleColumn')
	rating_td=soup.find_all('td',class_='ratingColumn imdbRating')

	for container in movie_td:
		titles.append(container.a.text)
		year.append(container.span.text)
		starring.append(container.a.attrs['title'])
		if(len(titles)==50):
			break

	for tag in rating_td:

		if(tag.strong):
			imdb_rating.append(tag.strong.text)
		else:
			imdb_rating.append('-')
		if(len(imdb_rating)==50):
			break
	def tabularTv():
		table=pd.DataFrame(
		{
		'movie':titles,
		'year':year,
		'cast':starring,
		'rating':imdb_rating
		})
		table['year']=table['year'].str.extract('(\d+)').astype(int)
		table['rating']=pd.to_numeric(table['rating'],errors='coerce')
		return table
	chart=tabularTv()
	#chart.to_csv('test.csv')
	print(chart)
def popularTv():
	headers={"Accept-Language":"en-US ,en;q=0.5"}
	url=linkToImdb["mostpopulartv"]
	results=requests.get(url,headers=headers)
	soup=BeautifulSoup(results.text,"html.parser")

	titles=[]
	year=[]
	starring=[]
	imdb_rating=[]

	movie_td=soup.find_all('td',class_='titleColumn')
	rating_td=soup.find_all('td',class_='ratingColumn imdbRating')

	for container in movie_td:
		titles.append(container.a.text)
		year.append(container.span.text)
		starring.append(container.a.attrs['title'])
		if(len(titles)==50):
			break

	for tag in rating_td:
		if(tag.strong):
			imdb_rating.append(tag.strong.text)
		else:
			imdb_rating.append('-')
		if(len(imdb_rating)==50):
			break
	def tabularTv():
		table=pd.DataFrame(
		{
		'movie':titles,
		'year':year,
		'cast':starring,
		'rating':imdb_rating
		})
		table['year']=table['year'].str.extract('(\d+)').astype(int)
		table['rating']=pd.to_numeric(table['rating'],errors='coerce')
		return table

	chart=tabularTv()
	#chart.to_csv('test.csv')
	print(chart)
def main():
	ascii_banner = pyfiglet.figlet_format("IMDb Scraper!")
	print('*'*65)
	print(ascii_banner)
	print('*'*65)
	print(' '*45,'by-Sahil Singh Rawat')
	print('''Enter any one number from given option
		1- Top Rated Movies
		2- Most Popular Movies
		3- Top Rated TV shows
		4- Most Popular TV Shows''')
	while True:
		option=input()
		if(option in ['1','2','3','4','q']):
			break
		else:
			print("Invalid option")
			print("Enter the no. from the given list only")
	if(option=='1'):
		topMovie()
	elif(option=='2'):
		popularMovie()
	elif(option=='3'):
		topTv()
	elif(option=='4'):
		popularTv()
	else:
		sys.exit()

main()