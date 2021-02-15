
data = {
    'name': 'Megan',
    'age': 22,
}

text: str = "%(name)s is %(age)" % data
print(text)

data = None

if data is None:
    number, text = 22, 'Awesome'
    text = "The number is %(number) and text is %(text)" % locals()
    print(text)