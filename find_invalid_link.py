#coding=utf-8


import requests
from bs4 import BeautifulSoup
from requests_file import FileAdapter
import os
import glob

"""
directory for printable html files and pdf files
"""
p_docs_dir = r'C:\apache-jmeter-5.2\printable_docs'


"""
find *.html file under currect dir and sub-dir
return an iter with full-path
"""
pathname = os.path.join(p_docs_dir, "**/*.html")
all_html = glob.iglob(pathname)


"""
"""
error_log = list()

for html_file in all_html:
    with open(html_file, encoding='utf-8') as f:
        soap = BeautifulSoup(f, features="html.parser")
        
    # extract all unique links from soap CSS select.

    unique_links = sorted(set([i.attrs['href'] for i in soap.select("a[href]")]))
    
    '''
    requests not support 'file:///' in default.
    so I install `requests-file` to solve it. 
    '''
    rs = requests.session()
    rs.mount('file://', FileAdapter())
    
    parent_dir = os.path.dirname(html_file)
    
    for z in unique_links:
        if z.startswith('http'):
            pass
        elif z.startswith('#'):
            x = html_file + z
        elif z.startswith('mailto'):
            continue
        else:
            x = os.path.join(parent_dir, z)
        #print(x)
    
        
        y = os.path.join('file:///' + x.replace("\\", "/"))
        
        r = rs.get(y)
        #print(r.request.url)
        #r = requests.get(x)
        
        #print(y)
        
        if r.status_code != 200:
            error_log.append("Source File: {}".format(html_file))
            error_log.append("ERROR: {}".format(r.status_code))
            error_log.append("Origin attr: {}".format(z))
            error_log.append("Request URL: {}".format(y))
            error_log.append("===========================\n")
            
        #print(len(error_log))
        
with open(r'c:\xml-error.log', mode='w', encoding='utf-8') as f:
    f.writelines('\n'.join(error_log))
    
# how many question found.
print(len(error_log)//5)
    
