from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd

# Create your views here.
def replaceCountries(x):
    if(x=='Japan'):
        return x.replace('Japan','Japão')
    else:
        return x

def home(request):
    df = pd.read_csv('app/static/data/netflix_titles.csv')
    data = {}
    #print(df.count())
    #print(df.info())
    data['dados']=df\
        .drop(['Unnamed: 0','runtimes'],axis=1)\
        .dropna()\
        .head(20)\
        .to_html(index=False,classes=['table','table-striped','mt-5'])
    data['countryFilter']=df['country'].sort_values().unique()
    #print(data['dados'].count())

    """df['country'] = df['country'].apply(replaceCountries)
    data['dados'] = df.to_html(index=False, classes=['table', 'table-striped', 'mt-5'])"""

    """grupo=df.groupby('country').count()
    data['dados']=grupo[['title','year']]\
        .sort_values(by='title',ascending=False)\
        .to_html()"""
    return render(request,'index.html',data)