#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import decimal
import time
import requests

from apcontent import alarmpi_content

class weather_yahoo(alarmpi_content):
  def build(self):
    location = self.sconfig['location']

    if self.sconfig['metric'] == str(1):
        metric = '&units=imperial'
    elif self.sconfig['metric'] == str(2):
        metric = '&units=metric'
    else:
        metric = ''

    try:
        weather_url = "http://" + self.sconfig["host"] + location + self.sconfig["path"] + metric
        response_dictionary = requests.get(weather_url).json()

        current = response_dictionary['main']['temp']
        current_low = response_dictionary['main']['temp_min']
        current_high = response_dictionary['main']['temp_max']
        conditions = response_dictionary['weather'][0]['description']
        wind_mph = response_dictionary['wind']['speed']
        print('problem 1')
        wind_degree = 0
        if 'degree' in response_dictionary['wind']:
            print('in if statement')
            wind_degree = response_dictionary['wind']['deg']
        

        weather_yahoo = 'Weather for today is ' + str(conditions) + ' currently ' + str(current) + ' degrees with a low of ' + str(current_low) + ' and a high of ' + str(current_high) + '.  '

        if(wind_mph<5):
            gust = 'It is calm wind '
        elif wind_mph < 10:
            gust = 'With light air '
        elif wind_mph < 15:
            gust = 'With a light breeze '
        elif wind_mph < 20:
            gust = 'With a moderate breeze '
        elif wind_mph < 30:
            gust = 'With a strong breeze '
        else:
            gust = 'It is crazy windy out here '

        if 348.75 < wind_degree or wind_degree <= 11.25:
            wind_direction = 'from the North'
        elif wind_degree > 11.25 and wind_degree <= 33.75:
            wind_direction = 'from the North North East'
        elif wind_degree > 33.75 and wind_degree <= 56.25:
            wind_direction = 'from the North East'
        elif wind_degree > 56.25 and wind_degree <= 78.75:
            wind_direction = 'from the East North East'
        elif wind_degree > 78.75 and wind_degree <= 101.25:
            wind_direction = 'from the East'
        elif wind_degree > 101.25 and wind_degree <= 123.75:
            wind_direction = 'from the East South East'
        elif wind_degree > 123.75 and wind_degree <= 146.25:
            wind_direction = 'from the South East'
        elif wind_degree > 146.25 and wind_degree <= 168.75:
            wind_direction = 'from the South South East'
        elif wind_degree > 168.75 and wind_degree <= 191.25:
            wind_direction = 'from the South'
        elif wind_degree > 191.25 and wind_degree <= 213.75:
            wind_direction = 'from the South South West'
        elif wind_degree > 213.75 and wind_degree <= 236.25:
            wind_direction = 'from the South West'
        elif wind_degree > 236.25 and wind_degree <= 258.75:
            wind_direction = 'from the West South West'
        elif wind_degree > 258.75 and wind_degree <= 281.25:
            wind_direction = 'from the West'
        elif wind_degree > 281.25 and wind_degree <= 303.75:
            wind_direction = 'from the West North West'
        elif wind_degree > 303.75 and wind_degree <= 326.25:
            wind_direction = 'from the North West'
        elif wind_degree > 326.25 and wind_degree <= 348.75:
            wind_direction = 'from the North North West'

        weather_yahoo = weather_yahoo + gust + wind_direction + '. '

    except Exception:
      weather_yahoo = 'Failed to connect to Weather.  '

    if self.debug:
      print weather_yahoo

    self.content = weather_yahoo
