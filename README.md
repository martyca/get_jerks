# get_jerks
dirty python script to get ssh knockers per country

this parses all the files in /var/log/audit, looks for entries with "terminal=ssh res=failed", regexes the ip from there.
does some python dict building (badly).
and finally outputs a list of tries per country as well as generating a csv output file.
the csv file is handy for creating a geographic heatmap, have a look at https://fusiontables.google.com/
