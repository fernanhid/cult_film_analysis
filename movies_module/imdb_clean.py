import re
from datetime import datetime
from datetime import datetime3


def get_year(release_date):
    try:
        return int(datetime.strptime(release_date.split('(')[0].strip(), '%d %B %Y').strftime("%Y"))
    except:
        return release_date
    
def get_day(release_date):
    try:
        return datetime.strptime(release_date.split('(')[0].strip(), '%d %B %Y').strftime("%A")
    except:
        return release_date
    
def clean_genre(genre_string):
    try:
        return re.findall(r"[\w']+", genre_string)[0]
    except:
        return 'NaN'

def get_month(release_date):
    try:
        return datetime.strptime(release_date.split('(')[0].strip(), '%d %B %Y').strftime("%B")
    except:
        return release_date
    
def clean_cash(gross_string):
    try:
        return int(gross_string.split('(')[0].strip().replace('$', '').replace(',',''))
    except:
        return 'NaN'
    
def clean_release(data_string):
    try:
        return datetime.strptime(data_string.split('(')[0].strip(), '%d %B %Y')
    except:
        return data_string
    
def clean_runtime(data_string, value = False):
    if value == False:
        try:
            return int(data_string.strip().split()[0])
        except:
            return data_string
    elif value == True:
        try:
            return datetime.timedelta(minutes = int(data_string.strip().split()[0]))
        except:
            return data_string
        
def clean_country(country_string):
    try:
        return country_string.split('|')[0]
    except:
        return country_string
    