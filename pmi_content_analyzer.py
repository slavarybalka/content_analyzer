### PMI Content Analyzer by Slava Rybalka on July, 2016
### Python 3.4.2

### 1. Input a list of URLs
### 2. Analyze the contents of these pages. 
### 3. Check if a certain phrase is in text and if yes, return the URL


# -*- coding: utf-8 -*-


import urllib
import http.client
from urllib.parse import urlparse
import urllib.request
from urllib.error import URLError, HTTPError
import socket
from socket import timeout
import re
import time
import sys
import codecs
import string
from collections import defaultdict
import textstat3 as textstat

test_data = """Playing games has always been thought to be important to the development of well-balanced and creative children; however, what part, if any, they should play in the lives of adults has never been researched that deeply. I believe that playing games is every bit as important for adults as for children. Not only is taking time out to play games with our children and other adults valuable to building interpersonal relationships but is also a wonderful way to release built up tension."""

t = textstat.textstatistics()

if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


opener = urllib.request.FancyURLopener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

#socket.setdefaulttimeout(10)

f = open('C:/Python34/progs/seo_content_wizard/pmi_pages.txt')
#lines = f.read().splitlines()
lines_1 = ['http://www.propertyware.com', 'http://www.realpage.com']

keyword = 'insurance'
counter = 0
resulting_urls = []

###########
# Request #
###########

# getting the contents of the URL
def query_url(url): 
    url = "http://" + url.replace("http://",'').replace("https://",'') # sanitizing the URI

    request = opener.open(url)
    try:
        results = request.read()
        print(results)

    except ValueError as e:
        print('Error:', e)
        results = None
        pass
    
    return results

# removing the noise
def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)



#############
# Execution #
#############



print(lines_1)
print(len(lines_1))

for webpage in lines_1:
    counter +=1
    print("Processing", counter, 'out of', len(lines_1))

    try:
        req = opener.open(webpage)
        results = req.read().decode('utf-8')
        #check_readability(results)
        reading_score = t.flesch_reading_ease(test_data)
        print(reading_score)
        if keyword in results:
          print(webpage)
          resulting_urls.append(webpage)
            
    except HTTPError as e:
        print('HTTP error:', e.code)
        pass
    except URLError as e:
        print('We failed to reach a server:', e.reason)
        pass
    except socket.timeout:
        print('socket timeout')
        pass
    except http.client.BadStatusLine as e:
        print('HTTP error not recognized, error code not given')
        pass
    except ValueError as e:
        print('Error:', e)
        pass
    except AttributeError:
        print("AttributeError found, skipping")
        pass

'''
for i in resulting_urls:
    print(i)
'''