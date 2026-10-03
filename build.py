#!/usr/bin/env python3
"""Build the site: python3 build.py  ->  ../webuild-homepage-v2.html
Reads template.html + content/content.json + content/images/*. See README.md."""
import json,base64,os
h=os.path.dirname(os.path.abspath(__file__));c=json.load(open(h+'/content/content.json',encoding='utf-8'))
uri=lambda f:'data:image/jpeg;base64,'+base64.b64encode(open(f'{h}/content/images/{f}','rb').read()).decode()
for p in c['projects']:p['photos']=[uri(f) for f in p.get('photos',[])]
for k in('commercial_categories','services'):c[k]=[uri(f) for f in c[k]]
j=json.dumps(c,ensure_ascii=False).replace('</','<\\/')
t=open(h+'/template.html',encoding='utf-8').read().replace('/*__SITE__*/null',j)
open(h+'/../webuild-homepage-v2.html','w',encoding='utf-8').write(t)
print('built',len(t)//1024,'KB,',len(c['projects']),'projects')
