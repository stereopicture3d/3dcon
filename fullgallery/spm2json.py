"""
For creating a list of images formated for Stereopix JSON
from a Stereo Photomaker HTML5 file named
    "index_m.htm".

The output list is in the file
    "jsonlist.txt"
"""

spmfile = open("index_m.htm", 'r').read().splitlines()
outlist = []
for line in spmfile:
    line = line.split("?")
    try:
##        line = (line[1].split(('"'))[0])
##        line = '{ "url": "%s" }' % line
##        outlist.append(line)

        outlist.append('{ "url": "%s" }' % (line[1].split(('"'))[0]))

    except IndexError:
        pass

open("jsonlist.txt", 'w').write(",\n".join(outlist))
