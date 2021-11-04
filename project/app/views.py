from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from django.http import JsonResponse
import pandas as pd
import json
import re

df = pd.read_csv('app/static/data/netflix_titles.csv')
data = {}

#Template da Home
def home(request):
    #data['dados']=df[(df['release_year']>2009) & (df['country']=='Brazil')]\
    data['dados']=df \
        .drop (['Unnamed: 0', 'runtimes'], axis=1) \
        .dropna () \
        .head(20)\
        .to_html(index=False,classes=['table','table-striped','mt-5'])
    data['countryFilter']=df['country'].sort_values().unique()
    return render(request,'index.html',data)

#Requisição para filtro de país
def countryFilter(request):
    if request.body:
        field = json.loads(request.body.decode('utf-8'))
        search = field['country']
        title = field['title']
        df2=df.dropna()
        data['dados']=df2[(df2['country'].str.contains(search))&(df2['title'].str.contains(title,flags=re.IGNORECASE))]\
        .to_html(index=False,classes=['table','table-striped','mt-5'])
    return JsonResponse({'data':data['dados']})