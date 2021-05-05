from app.models import ipa_dict
from app.segmentise import segmentise

lines = [line.strip() for line in open('C:/Users/dom/Downloads/sjp-odm-20210427/odm.txt', encoding="utf8")]
lines_split = []
for line in lines:
    for item in line.split(', '):
        flag = 0
        for character in item.lower():
            if character not in ipa_dict:
                flag = 1
        if flag == 0:
            lines_split.append(item)

words_segmentised = []
for line in lines_split:
    words_segmentised.append((segmentise(line), line))

