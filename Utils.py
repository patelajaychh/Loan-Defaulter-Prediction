#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 01:35:31 2019

@author: ajay
"""

import datetime
import re

def toDate(str_date, pattern = '%d-%m-%y'):
    """
    coverts given string date into date object
    y - represent short hand presentation i.e. 18 for 2019
    Y - represent full year i.e. 2019, 2018
    """
    date_elements = [int(element) for element in str_date.split(pattern[2])]
    
    if pattern[7]=='y':
        if date_elements[2]>=00 and date_elements[2]<=19:
            date_elements[2] = 20*100+date_elements[2]
        else:
            date_elements[2] = 19*100+date_elements[2]
    return datetime.date(date_elements[2], date_elements[1], date_elements[0])

def date_diff(date1, date2):
    '''
    Takes two objects of type date and return difference in no of days
    '''
    if isinstance(date1 , datetime.date) and isinstance(date1 , datetime.date):
            diff = (date1 - date2)
            return abs(diff.days)
    else:
        print("Error: arguments should be of type datetime.date()")
    

def total_span(str_input):
    """
    """
    list_num = [int(output) for output in re.findall('\d+', str_input)]
    return list_num[0]*12 + list_num[1]
    