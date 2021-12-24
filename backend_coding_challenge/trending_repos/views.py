from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import datetime
from collections import defaultdict

class LanguageReposView(APIView):
  
  

    def _prepare_repos_count_dict(self,data):
        """prepare response with dictionary of repos url and repos count for each language"""
        d = defaultdict(lambda: defaultdict(list))

        for val in data["items"]:
            if val['language']:
                d[val['language']]['repo_urls'].append(val['html_url'])
                if 'repo_count' in d[val['language']]:
                    d[val['language']]['repo_count']+=1 
                else:
                    d[val['language']]['repo_count']=1
        return d


    def get(self, request):
        """get request method to return response with list of repos urls and number of repos for each language  in the last 30 days"""
        ##repo_url
        URL = "https://api.github.com/search/repositories"
        date_of_last_30_days = (datetime.datetime.now()- datetime.timedelta(30)).date().strftime("%Y-%m-%d")
        #request example https://api.github.com/search/repositories?q=created>2021-06-10&sort=stars&order=desc
        PARAMS = {'q':'created>'+date_of_last_30_days,'sort':'stars','order':'dec'}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        languages_dict = self._prepare_repos_count_dict(data)
        return Response(languages_dict)

