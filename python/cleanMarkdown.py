#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir, makedirs
from os.path import join, exists
from time import sleep
from re import sub, search
from slugify import slugify

posts = []

if __name__ == "__main__":
    SOURCE_DIR = "source"
    IMAGES_DIR = join(SOURCE_DIR, "assets")
    POST_IMAGES_DIR = join(IMAGES_DIR, "posts")
    PROJ_DIR = join(SOURCE_DIR, "_source")
    OUT_DIR = join(SOURCE_DIR, "_posts")

    for filename in [f for f in listdir(PROJ_DIR) if f.endswith(".md")]:
        fullPath = join(PROJ_DIR, filename)
        chikChikCount = 0
        thisPost = {}
        with open(fullPath) as txt:
            content = ""
            for line in txt.read().splitlines():
                if(line == '---'):
                    chikChikCount += 1
                elif(':' in line and chikChikCount < 2):
                    (key, val) = line.split(':', 1)
                    thisPost[key.strip()] = val.strip()
                elif chikChikCount >= 2:
                    # replaces orphan tags
                    line = sub(r"</?em>", "*", line)
                    line = sub(r"</?strong>", "**", line)
                    line = sub(r"</?p>", "", line)
                    line = sub(r"<br */>", "", line)
                    line = sub(r"&nbsp;", "", line)
                    line = sub(r"jpeg", "jpg", line)

                    # replaces html-encoded characters
                    line = sub("&#8211;", "-", line)
                    line = sub("&#8217;", "'", line)
                    line = sub("&#8220;", '"', line)
                    line = sub("&#8221;", '"', line)
                    line = sub("&#8230;", '...', line)

                    if("img" in line):
                        # replaces <img> with ![]()
                        line = sub(r"< *img.*?src *?= *?\"(([^ ]*?/)+(.+?))\".*?>", r"![](\3)", line)
                        # cleans up "sized" image file references
                        line = sub(r"-[0-9]+x[0-9]+\.(\w{3})", r".\1", line)
                        # cleans up <a>
                        line = sub(r"< *a *?href *?= *?\"(.*?)\" *?>(.*?)< *?/ *?a *?>", r"\2", line)
                    else:
                        # for non img <a> (external links)
                        line = sub(r"< *a *?href *?= *?\"(.*?)\" *?>(.*?)< *?/ *?a *?>", r"[\2](\1)", line)
                    content += "%s\n"%line

            thisPost['content'] = content
            posts.append(thisPost)
            txt.close()

    # write out
    for p in posts:
        cleanTitle = sub(r" *\([0-9 \-]+\)","",p['title']).strip()
        outputFileName = slugify(cleanTitle)
        coverFileName = slugify(cleanTitle, max_length=17, word_boundary=True, save_order=True)
        description = p['description'] if 'description'in p else ''
        fullOutputPath = join(OUT_DIR,outputFileName+".md")
        if(p['layout'] != 'post'):
          pageOutputDirectory = join(SOURCE_DIR, outputFileName)
          if not exists(pageOutputDirectory):
            makedirs(pageOutputDirectory)
          fullOutputPath = join(pageOutputDirectory, "index.md")
        with open(fullOutputPath, 'w') as out:
            out.write("---\n")
            out.write("layout: %s\n"%p['layout'])
            out.write("title: %s\n"%cleanTitle)
            out.write("description: %s\n"%description)
            out.write("url: %s/\n"%outputFileName)
            out.write("date: %s\n"%sub(r"\+[0-9:]+","",p['date']))
            out.write("cover: /assets/covers/%s.jpg\n"%coverFileName)
            out.write("---\n")
            # add image paths
            thisContent = sub(r"\!\[\]\((.*?)\)", r"![](/assets/posts/%s/\1)"%outputFileName, p['content'])
            # add audio paths
            thisContent = sub(r"(src=\")(.+\.mp3)(\")", r"\1/assets/posts/%s/\2\3"%outputFileName, thisContent)
            out.write("%s"%thisContent)
            out.close()
        if not exists(join(POST_IMAGES_DIR, outputFileName)):
            makedirs(join(POST_IMAGES_DIR, outputFileName))
