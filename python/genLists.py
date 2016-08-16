#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir, system
from os.path import join, isdir
from datetime import datetime 
from time import sleep
from re import sub

posts = []
def getDate(i):
    return i['date']

if __name__ == "__main__":
    SOURCE_DIR = "source"
    POST_DIR = join(SOURCE_DIR, "_posts")
    POST_PERMALINK_DIR = "post"
    PAGE_TITLE = "memememe"
    PAGE_DESCRIPTION = "memememememememememememe"

    for filename in [f for f in listdir(POST_DIR) if f.endswith(".md")]:
        fullPath = join(POST_DIR, filename)
        chikChikCount = 0
        thisPost = {}
        with open(fullPath) as txt:
            for line in txt.read().splitlines():
                if(line == '---'):
                    chikChikCount += 1
                if(':' in line and chikChikCount < 2):
                    (key, val) = line.split(':', 1)
                    thisPost[key.strip()] = val.strip()
            if(thisPost['layout'] == 'post'):
              posts.append(thisPost)
            txt.close()

    # order each category by descending date (most recent first)
    posts.sort(key=getDate, reverse=True)
    with open(join(SOURCE_DIR, "index.md"), 'w') as out:
        out.write("---\n")
        out.write("layout: home\n")
        out.write("title: '%s'\n"%PAGE_TITLE)
        out.write("description: '%s'\n"%PAGE_DESCRIPTION)
        out.write("url: /%s/\n"%POST_PERMALINK_DIR)
        out.write("posts: \n")
        for post in posts:
            tabString = "  - "
            for (pKey, pVal) in post.iteritems():
                out.write(tabString+pKey+": "+pVal+"\n")
                if(pKey == 'date'):
                  mDate = datetime.strptime(pVal, '%Y-%m-%dT%H:%M:%S')
                  out.write(tabString+"daymonthyear: %s-%s-%s\n"%(mDate.strftime('%d'),
                                                                  mDate.strftime('%b'),
                                                                  mDate.strftime('%y')))
                tabString = "    "
        out.write("---\n")
        out.close()
