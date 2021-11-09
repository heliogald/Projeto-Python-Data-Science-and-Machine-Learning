from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from django.http import JsonResponse
import pandas as pd
import json
import re

df = pd.read_csv('app/static/data/matching_results.csv')
data = {}

#Template da Home .drop (['Unnamed: 0', 'runtimes'], axis=1)
def home(request):
    #data['dados']=df[(df['release_year']>2009) & (df['country']=='Brazil')]\
    data['dados']=df \
        .rename({'Publication Number':'Publication'}, axis=1)\
        .dropna ()\
        .head(20)\
        .to_html(index=False,classes=['table','table-striped','mt-5'])
    data['countryFilter']=df['Country'].sort_values().unique()
    return render(request,'index.html',data)

#Requisição para filtro de país
def countryFilter(request):
    if request.body:
        field = json.loads(request.body.decode('utf-8'))
        search = field['Country']
        Match = field['Match']
        df2=df\
        .dropna()
        data['dados']=df2[(df2['Country'].str.contains(search))&(df2['Match'].str.contains( Match, flags=re.IGNORECASE))]\
        .to_html(index=False,classes=['table','table-striped','mt-5'])
        return JsonResponse({'data':data['dados']})