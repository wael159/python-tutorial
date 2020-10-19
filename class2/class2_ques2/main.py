# This is a sample Python script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#question 2 - Use python to retrieve the original file that was hacked
import re
pattern=re.compile(r'[a-z]{3}[A-Z]{3}[a-z]+\-\d{1,2}[A-Z]{3}[a-z]{3}')
hacked = "items_hacked.txt"
lines = open(hacked, 'r').readlines()
lines=''.join(lines)
new_words=pattern.findall(lines)
new_products=[]
for i in new_words:
    word1=i.replace(re.findall('[a-z]{3}[A-Z]{3}', i)[0],'')
    word2=word1.replace(re.findall('[A-Z]{3}[a-z]{3}', word1)[0],'')
    new_products.append(word2)
open("new_items.txt", 'w').write('\n'.join(new_products))
