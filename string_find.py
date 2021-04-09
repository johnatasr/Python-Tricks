text = "Today is a beautiful day"
text.find('day') # 2

text.rfind('day') # 21
text[text.rfind('day'):] # 'day'
text.find('dayy') # -1
