from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import datetime
class LanguageReposView(APIView):
    def _prepare_repos_count_dict(self,data):
        """prepare response with dictionary of repos url and repos count for each language"""
        languages_dict = {}
        for val in data['items']:
            if val['language']:
                if val['language'] in languages_dict:
                    languages_dict[val['language']]['repos'].append(val['html_url'])
                    languages_dict[val['language']]['repos_count'] = languages_dict[val['language']]['repos_count']+1
                else:
                    languages_dict[val['language']]={}
                    languages_dict[val['language']]['repos']=[val['html_url']]
                    languages_dict[val['language']]['repos_count']=1
        return languages_dict


    def get(self, request):
        """get request method to return response with list of repos urls and number of repos for each language  in the last 30 days"""
        ##repo_url
        URL = "https://api.github.com/search/repositories"
        ##get last 30 days date
        date_of_last_30_days = (datetime.datetime.now()- datetime.timedelta(30)).date().strftime("%Y-%m-%d")
        #request example https://api.github.com/search/repositories?q=created>2021-06-10&sort=stars&order=desc
        PARAMS = {'q':'created>'+date_of_last_30_days,'sort':'stars','order':'dec'}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        languages_dict = self._prepare_repos_count_dict(data)
        return Response(languages_dict)

