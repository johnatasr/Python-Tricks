from dateutil.parser import parse

logline = 'INFO 2020-01-01T00:00:01 Happy new year, human.'
timestamp = parse(logline, fuzzy=True)
print(timestamp)
# 2020-01-01 00:00:01