#!/usr/bin/env python2.7

#put in same directory as downloaded zipped/foldered gists
import os, glob, json, requests
print 
gist=raw_input('Gist? (the string at the end of the url) ')
author=raw_input('Author of gist? ')
gistVers=''

for file in glob.glob(os.getcwd()+'/*'):
	if gist in file:
        	gistVers=file.split('/')[-1].split('-')[1].split('.zip')[0]

gistCommits='https://api.github.com/gists/'+gist+'/commits'

session=requests.session()
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

r=session.get(gistCommits,headers=headers)
gistCurrVers=r.json()[0]['version']

print 'Your version: '+gistVers
print 'Current version: '+gistCurrVers
if gistVers!=gistCurrVers:
    print 'Your gist is out of date! Downloading...'
    downloadurl='https://gist.github.com/'+author+'/'+gist+'/archive/'+gistCurrVers+'.zip'
    local_filename = gist+'-'+downloadurl.split('/')[-1]
    r=session.get(downloadurl, headers=headers, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    print local_filename+' downloaded!!!'
    if gistVers !='':
        print 'Removing '+gist+'-'+gistVers+'.zip!'
        os.remove(gist+'-'+gistVers+'.zip')
else:
    print 'Your gist is up-to-date!'

print 


