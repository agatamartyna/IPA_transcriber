import re
from app.models import transcribe, ipa_vowels, voicing_dict, voi_dict_rev, non_cont_obstr, cont_obstr,clusters_dict, \
    soft_clusters_dict, sibilants_dict, pals, non_pals, vocs

def transcribe_text_Warsaw(text):

    # lowercase all letters
    text = text.lower()

    # extract alphabetic substrings
    words = re.findall(r'[a-ząćęłńóśźż]+', text)

    # phonemic transcription of words taken individually (regional processes not applied)
    ph_words = []
    if words:
        for word in words:
            ph_words.append(transcribe(word))


    # pre-voiced-obstruent revoicing
    for i in range(len(ph_words) - 1):
        if (
                len(ph_words[i]) >= 4 and
                ph_words[i][-4:-2] in voi_dict_rev and
                ph_words[i][-2:] in voi_dict_rev and
                ph_words[i + 1][0] in voicing_dict
        ):
            ph_words[i] = (ph_words[i][:-4]) + (voi_dict_rev[(ph_words[i][-4:-2])]) + (voi_dict_rev[(ph_words[i][-2:])])
        elif (
                len(ph_words[i]) >= 3 and
                ph_words[i][-3:-1] in voi_dict_rev and
                ph_words[i][-1] in voi_dict_rev and
                ph_words[i + 1][0] in voicing_dict
        ):
            ph_words[i] = (ph_words[i][:-3]) + (voi_dict_rev[(ph_words[i][-3:-1])]) + (voi_dict_rev[(ph_words[i][-1])])
        elif (
                len(ph_words[i]) >= 3 and
                ph_words[i][-3] in voi_dict_rev and
                ph_words[i][-2:] in voi_dict_rev and
                ph_words[i + 1][0] in voicing_dict
        ):
            ph_words[i] = (ph_words[i][:-3]) + (voi_dict_rev[(ph_words[i][-3])]) + (voi_dict_rev[(ph_words[i][-2:])])
        elif (
                len(ph_words[i]) >= 2 and
                ph_words[i][-2] in voi_dict_rev and
                ph_words[i][-1] in voi_dict_rev and
                ph_words[i + 1][0] in voicing_dict
        ):
            ph_words[i] = (ph_words[i][:-2]) + (voi_dict_rev[(ph_words[i][-2])]) + (voi_dict_rev[(ph_words[i][-1])])
        elif (
                len(ph_words[i]) >= 2 and
                ph_words[i][-2:] in voi_dict_rev and
                ph_words[i + 1][0] in voicing_dict
        ):
            ph_words[i] = (ph_words[i][:-2]) + (voi_dict_rev[(ph_words[i][-2:])])
        elif (
                (ph_words[i][-1]) in voi_dict_rev and
                ph_words[i + 1][0] in voicing_dict
        ):
            ph_words[i] = (ph_words[i][:-1]) + (voi_dict_rev[(ph_words[i][-1])])

    # Regressive Final Revoicing before prepositions 'w' and 'z' standing before voiced consonants or sonorants
    for i in range(len(ph_words) - 2):
        if (
                (ph_words[i][-1] in voi_dict_rev or ph_words[i][-1] in ipa_vowels or ph_words[i][-4:] in ipa_vowels) and
                (ph_words[i + 1][0] in voi_dict_rev and len(ph_words[i + 1]) == 1) and
                (ph_words[i + 2][0] in ipa_vowels or ph_words[i + 2][0] in vocs or ph_words[i + 2][0] in voicing_dict)
            ):
            if len(ph_words[i]) >= 4 and ph_words[i][-4:-2] in voi_dict_rev and ph_words[i][-2:] in voi_dict_rev:
                ph_words[i] = ph_words[i][:-4] + voi_dict_rev[ph_words[i][-4:-2]] + voi_dict_rev[ph_words[i][-2:]]
            elif len(ph_words[i]) >= 3 and ph_words[i][-3:-1] in voi_dict_rev and ph_words[i][-1] in voi_dict_rev:
                ph_words[i] = ph_words[i][:-3] + voi_dict_rev[ph_words[i][-3:-1]] + voi_dict_rev[ph_words[i][-1]]
            elif len(ph_words[i]) >= 3 and ph_words[i][-3] in voi_dict_rev and ph_words[i][-2:] in voi_dict_rev:
                ph_words[i] = ph_words[i][:-3] + voi_dict_rev[ph_words[i][-3]] + voi_dict_rev[ph_words[i][-2:]]
            elif len(ph_words[i]) >= 2 and ph_words[i][-2] in voi_dict_rev and ph_words[i][-1] in voi_dict_rev:
                ph_words[i] = ph_words[i][:-2] + voi_dict_rev[ph_words[i][-2]] + voi_dict_rev[ph_words[i][-1]]
            elif len(ph_words[i]) >= 1 and ph_words[i][-1] in voi_dict_rev:
                ph_words[i] = ph_words[i][:-1] + voi_dict_rev[ph_words[i][-1]]
            ph_words[i + 1] = voi_dict_rev[ph_words[i + 1]]


    # extract non-alphabetic substrings
    non_words = re.findall(r'[^a-ząćęłńóśźż]+', text)


    # put transcriptions of alphabetic strings and non-alphabetic substrings back together
    res = []
    maxi = max([len(ph_words), len(non_words)])
    if maxi == len(ph_words) and len(ph_words) != len(non_words):
        for i in range(len(ph_words)-1):
            res.append(ph_words[i])
            res.append(non_words[i])
        res.append(ph_words[-1])
    elif len(ph_words) == len(non_words):
        if text and text[0].isalpha():
            for i in range(len(ph_words)):
                res.append(ph_words[i])
                res.append(non_words[i])
        else:
            for i in range(len(ph_words)):
                res.append(non_words[i])
                res.append(ph_words[i])
    elif maxi == len(non_words) and len(ph_words) != len(non_words):
        for i in range(len(non_words)-1):
            res.append(non_words[i])
            res.append(ph_words[i])
        res.append(non_words[-1])

    result = ''.join(res)

    return result

if __name__ == "__main__":
    text = input("Wpisz tekst: ")
    print(transcribe_text_Warsaw(text))