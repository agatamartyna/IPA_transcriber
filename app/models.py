# sound inventory vowels
OPEN_FRONT = 'a'
CLOSE_CENT = '\u0268'

OPEN_MID_ROUND_NAS_DYPH = '\u0254\u0303w\u0303'
MID_OPEN_FRONT = '\u025B'
MID_OPEN_FRONT_NAS_DYPH = '\u025B\u0303w\u0303'
CLOSE_FRONT = '\u0069'
MID_OPEN_BACK_ROUND = '\u0254'
CLOSE_BACK_ROUND = 'u'
TILDE = '\u0303'
SPACE = ' '

# palatalised
PAL = '\u02B2'

# sound inventory consonants
VD_BILAB_STOP = 'b'
VS_ALV_AFF = 'ts'
VS_PAL_AFF = 't\u0255'
VS_POSTALV_AFF = 't\u0282'
VD_DENT_STOP = 'd'
VD_PAL_AFF = 'd\u0291'
VD_ALV_AFF = 'dz'
VD_POSTALV_AFF = 'd\u0290'
VS_LABDENT_FRIC = 'f'
VD_VEL_STOP = '\u0261'
VS_VEL_FRIC = 'x'
VD_VEL_FRIC = '\u0263'
PAL_APPROX = 'j'
VS_VEL_STOP = 'k'
ALV_LAT_APPROX = 'l'
BILAB_APPROX = 'w'
BILAB_NAS = 'm'
DENT_NAS = 'n'
PAL_NAS = '\u0272'
VS_BILAB_STOP = 'p'
ALV_TRILL = 'r'
VS_ALV_FRIC = 's'
VS_PAL_FRIC = '\u0255'
VS_DENT_STOP = 't'
VD_LABDENT_FRIC = 'v'
VS_POSTALV_FRIC = '\u0282'
VD_ALV_FRIC = 'z'
VD_POSTALV_FRIC = '\u0290'
VD_PAL_FRIC = '\u0291'


# character - ipa symbol maps
ipa_dict = {
    'a': OPEN_FRONT,
    'ą': OPEN_MID_ROUND_NAS_DYPH,
    'b': VD_BILAB_STOP,
    'c': VS_ALV_AFF,
    'ć': VS_PAL_AFF,
    'ch': VS_VEL_FRIC,
    'd': VD_DENT_STOP,
    'dź': VD_PAL_AFF,
    'dz': VD_ALV_AFF,
    'dż': VD_POSTALV_AFF,
    'e': MID_OPEN_FRONT,
    'ę': MID_OPEN_FRONT_NAS_DYPH,
    'f': VS_LABDENT_FRIC,
    'g': VD_VEL_STOP,
    'h': VS_VEL_FRIC,
    'i': CLOSE_FRONT,
    'j': PAL_APPROX,
    'k': VS_VEL_STOP,
    'l': ALV_LAT_APPROX,
    'ł': BILAB_APPROX,
    'm': BILAB_NAS,
    'n': DENT_NAS,
    'ń': PAL_NAS,
    'o': MID_OPEN_BACK_ROUND,
    'ó': CLOSE_BACK_ROUND,
    'p': VS_BILAB_STOP,
    'q': VS_VEL_STOP,
    'r': ALV_TRILL,
    's': VS_ALV_FRIC,
    'ś': VS_PAL_FRIC,
    't': VS_DENT_STOP,
    'u': CLOSE_BACK_ROUND,
    'v': VD_LABDENT_FRIC,
    'w': VD_LABDENT_FRIC,
    'y': CLOSE_CENT,
    'z': VD_ALV_FRIC,
    'ż': VD_POSTALV_FRIC,
    'ź': VD_PAL_FRIC,
    'x': VS_VEL_STOP + VS_ALV_FRIC
}

# vowels
ipa_vowels = [
    OPEN_FRONT,
    OPEN_MID_ROUND_NAS_DYPH,
    MID_OPEN_FRONT,
    MID_OPEN_FRONT_NAS_DYPH,
    CLOSE_FRONT,
    MID_OPEN_BACK_ROUND,
    CLOSE_BACK_ROUND,
    CLOSE_CENT,
    SPACE
]

# voiced - voiceless pairs (equivalent to the set of obstruents)
voicing_dict = {
    VD_BILAB_STOP: VS_BILAB_STOP,
    VD_DENT_STOP: VS_DENT_STOP,
    VD_ALV_AFF: VS_ALV_AFF,
    VD_PAL_AFF: VS_PAL_AFF,
    VD_POSTALV_AFF: VS_POSTALV_AFF,
    VD_VEL_STOP: VS_VEL_STOP,
    VD_LABDENT_FRIC: VS_LABDENT_FRIC,
    VD_ALV_FRIC: VS_ALV_FRIC,
    VD_VEL_FRIC: VS_VEL_FRIC,
    VD_POSTALV_FRIC: VS_POSTALV_FRIC,
    VD_PAL_FRIC: VS_PAL_FRIC
}

# voiceless - voiced pairs
voi_dict_rev = {value: key for key, value in voicing_dict.items()}

# non-continuant obstruents
non_cont_obstr = {
    VD_BILAB_STOP: VS_BILAB_STOP,
    VD_DENT_STOP: VS_DENT_STOP,
    VD_ALV_AFF: VS_ALV_AFF,
    VD_PAL_AFF: VS_PAL_AFF,
    VD_POSTALV_AFF: VS_POSTALV_AFF,
    VD_VEL_STOP: VS_VEL_STOP,
}

# continuant obstruents
cont_obstr = ['w', 'f', 'z', 's', 'sz', 'ż', 'rz',
              'ś', 'si', 'ź', 'zi', 'h', 'ch']

# simplify clusters
clusters_dict = {
    VS_ALV_AFF + CLOSE_FRONT: VS_PAL_AFF + CLOSE_FRONT,
    VS_ALV_FRIC + CLOSE_FRONT: VS_PAL_FRIC + CLOSE_FRONT,
    VD_DENT_STOP + VD_ALV_FRIC + CLOSE_FRONT: VD_PAL_AFF + CLOSE_FRONT,
    VD_ALV_FRIC + CLOSE_FRONT: VD_PAL_FRIC + CLOSE_FRONT,
    VS_ALV_AFF + VS_VEL_FRIC: VS_VEL_FRIC,
    ALV_TRILL + VD_ALV_FRIC: VD_POSTALV_FRIC,
    VS_ALV_FRIC + VD_ALV_FRIC: VS_POSTALV_FRIC,
    VS_ALV_AFF + VD_ALV_FRIC: VS_DENT_STOP+VS_POSTALV_FRIC,
    DENT_NAS + CLOSE_FRONT: PAL_NAS + CLOSE_FRONT,
    VD_DENT_STOP + VD_ALV_FRIC: VD_ALV_AFF,
    VD_DENT_STOP + VD_PAL_FRIC: VD_PAL_AFF
}

# palatalised sounds with multiple character notation
# in pairs one-to-one transcription - sound
soft_clusters_dict = {
    VS_ALV_AFF + CLOSE_FRONT: VS_PAL_AFF + CLOSE_FRONT,
    VS_ALV_FRIC + CLOSE_FRONT: VS_PAL_FRIC + CLOSE_FRONT,
    VD_DENT_STOP + VD_ALV_FRIC + CLOSE_FRONT: VD_POSTALV_AFF + CLOSE_FRONT,
    VD_ALV_AFF + CLOSE_FRONT: VD_PAL_FRIC + CLOSE_FRONT,
    DENT_NAS + CLOSE_FRONT: PAL_NAS + CLOSE_FRONT
}

# sibilants arranged into pairs voiceless - voiced
sibilants_dict = {
    VS_ALV_AFF: VD_ALV_AFF,
    VS_PAL_AFF: VD_PAL_AFF,
    VS_POSTALV_AFF: VD_POSTALV_AFF,
    VS_ALV_FRIC: VD_ALV_FRIC,
    VS_PAL_FRIC: VD_PAL_FRIC,
    VS_POSTALV_FRIC: VD_POSTALV_FRIC
}

# fricatives + affricates
affric_dict = {
    VS_ALV_AFF: VD_ALV_AFF,
    VS_PAL_AFF: VD_PAL_AFF,
    VS_POSTALV_AFF: VD_POSTALV_AFF,
    VS_ALV_FRIC: VD_ALV_FRIC,
    VS_PAL_FRIC: VD_PAL_FRIC,
    VS_POSTALV_FRIC: VD_POSTALV_FRIC,
    VS_VEL_FRIC: VD_VEL_FRIC,
    VS_LABDENT_FRIC: VD_LABDENT_FRIC,
}

# palatals
pals = [
    VS_PAL_AFF,
    VD_PAL_AFF,
    VS_PAL_FRIC,
    VD_PAL_FRIC,
    PAL_NAS
]

# non-palatals
non_pals = [
    VS_BILAB_STOP, VD_BILAB_STOP, VS_DENT_STOP,
    VD_DENT_STOP, VS_LABDENT_FRIC, VD_LABDENT_FRIC,
    '\u0261', 'x', 'k', 'l', 'm', 'r'
]


# vocalics
vocs = [
    PAL_APPROX, BILAB_APPROX, ALV_LAT_APPROX,
    ALV_TRILL, DENT_NAS, BILAB_NAS, PAL_NAS
]


def transcribe(word):

    # one-to-one character-symbol transcription
    ph_word = ''
    for letter in word:
        ph_word += str(ipa_dict[letter])

    # Progressive Voicing Morphological Conditioning
    for i in range(len(word)-1):
        if (
            word[i:i + 2] == 'że' and
            ipa_dict[word[i-1]] in voi_dict_rev
        ):
            ph_word1 = ''
            for letter in word[:i-1]:
                ph_word1 += str(ipa_dict[letter])
            ph_word2 = ''
            for letter in word[i:]:
                ph_word2 += str(ipa_dict[letter])
            vs_item = ipa_dict[word[i-1]]
            vd_item = voi_dict_rev[vs_item]
            ph_word = ph_word1 + vd_item + ph_word2

    # Denasalisation
    for i in range(len(word)):
        if word[i] == 'ę' or word[i] == 'ą':
            if (
                i == len(word) - 1 or
                word[i + 1] == 'l' or
                word[i + 1] == 'ł'
            ):
                ph_word1 = ''
                for letter in word[:i]:
                    ph_word1 += str(ipa_dict[letter])
                ph_word2 = ''
                for letter in word[i+1:]:
                    ph_word2 += str(ipa_dict[letter])
                if word[i] == 'ę':
                    denasalised_item = MID_OPEN_FRONT
                    ph_word = ph_word1 + denasalised_item + ph_word2
                elif word[i] == 'ą':
                    if i != len(word) - 1:
                        denasalised_item = MID_OPEN_BACK_ROUND
                        ph_word = ph_word1 + denasalised_item + ph_word2
                    else:
                        ph_word = ph_word1 + OPEN_MID_ROUND_NAS_DYPH

            else:
                if not (
                    word[i + 1] in cont_obstr or
                    word[i + 1:i + 3] in cont_obstr
                ):
                    ph_word1 = ''
                    for letter in word[:i]:
                        ph_word1 += str(ipa_dict[letter])
                    ph_word2 = ''
                    for letter in word[i + 1:]:
                        ph_word2 += str(ipa_dict[letter])
                    denasalised_item = ''
                    if word[i] == 'ę':
                        denasalised_item = MID_OPEN_FRONT + 'n'
                    elif word[i] == 'ą':
                        denasalised_item = MID_OPEN_BACK_ROUND + 'n'
                    ph_word = ph_word1 + denasalised_item + ph_word2

    # character cluster transcription
    for cluster in clusters_dict:
        if cluster in ph_word:
            ph_word = ph_word.replace(cluster, clusters_dict[cluster])

    # Nasal Assimilation
    for i in range(len(ph_word) - 2):
        if ph_word[i:i + 2] == 'ɛn' or ph_word[i:i + 2] == 'ɔn':
            if ph_word[i + 2] == 'p' or ph_word[i + 2] == 'b':
                ph_word = ph_word[:i + 1] + 'm' + ph_word[i + 2:]
            elif ph_word[i + 2] in [VS_VEL_STOP, VD_VEL_STOP]:
                ph_word = ph_word[:i + 1] + 'ŋ' + ph_word[i + 2:]
            elif ph_word[i + 2:i + 4] in [VS_PAL_AFF, VD_PAL_AFF]:
                ph_word = ph_word[:i + 1] + 'ɲ' + ph_word[i + 2:]
            elif ph_word[i + 2:i + 4] in \
                    [VS_ALV_AFF, VD_ALV_AFF, VS_POSTALV_AFF, VD_POSTALV_AFF]:
                ph_word = ph_word[:i + 1] + 'ɳ' + ph_word[i + 2:]

    #  notation: remove palatal approximant
    #  from sequences  PAL_APPROX + 'i' + VOWEL
    for i in range(len(ph_word) - 2):
        if (
                ph_word[i] in pals and
                ph_word[i + 1] == 'i' and
                ph_word[i + 2] in ipa_vowels
        ):
            ph_word = ph_word[:i + 1] + '&' + ph_word[i + 2:]
    ph_word = ph_word.replace('&', '')

    #  notation: turn 'i' into 'j' in sequences CONSONANT + 'i' + VOWEL
    for i in range(len(ph_word)-3):
        if (
            ph_word[i] in non_pals and
            ph_word[i + 1] == 'i' and
            ph_word[i + 2] in ipa_vowels
        ):
            ph_word = ph_word[:i + 1] + 'j' + ph_word[i + 2:]

    # Final Devoicing
    for voiced in [key for key in voicing_dict.keys()]:
        if ph_word[-2:] == voiced:
            ph_word = ph_word[:-2] + voicing_dict[voiced]
        elif ph_word[-1] == voiced:
            ph_word = ph_word[:-1] + voicing_dict[voiced]

    # Final Devoicing for Pairs of Obstruent Clusters
    # this empirically-based solution not working with
    # final obstruent clusters longer than 2 items
    # because there are none in Polish
    for i in range(len(ph_word) - 1):
        if ph_word[-2:] in voi_dict_rev:
            if len(ph_word) >= 4 and ph_word[-4:-2] in voicing_dict:
                ph_word = ph_word[:-4] + \
                          voicing_dict[ph_word[-4:-2]] + ph_word[-2:]
            elif len(ph_word) >= 3 and ph_word[-3] in voicing_dict:
                ph_word = ph_word[:-3] + \
                          voicing_dict[ph_word[-3]] + ph_word[-2:]
        elif ph_word[-1] in voi_dict_rev:
            if len(ph_word) >= 3 and ph_word[-3:-1] in voicing_dict:
                ph_word = ph_word[:-3] + \
                          voicing_dict[ph_word[-3:-1]] + ph_word[-1]
            elif len(ph_word) >= 2 and ph_word[-2] in voicing_dict:
                ph_word = ph_word[:-2] + \
                          voicing_dict[ph_word[-2]] + ph_word[-1]

    # Regressive Voicing
    for i in range(len(ph_word) - 1):
        if (
                (ph_word[i] in affric_dict) and
                ph_word[i + 1] in non_cont_obstr
        ):
            if ph_word[i - 1:i + 1] in affric_dict:
                vd_item = affric_dict[ph_word[i - 1:i + 1]]
                ph_word = ph_word[:i - 1] + vd_item + ph_word[i + 1:]
            elif ph_word[i] in affric_dict:
                vd_item = affric_dict[ph_word[i]]
                ph_word = ph_word[:i] + vd_item + ph_word[i + 1:]

    # Progressive Devoicing
    for i in range(len(ph_word) - 2):
        if ph_word[i] in voi_dict_rev and ph_word[i + 1] in voicing_dict:
            vless_item = voicing_dict[ph_word[i + 1]]
            ph_word = ph_word[:i + 1] + vless_item + ph_word[i + 2:]

    # Regressive Devoicing
    for i in range(len(ph_word) - 2):
        if ph_word[i] in voicing_dict and ph_word[i + 1] in voi_dict_rev:
            vless_item = voicing_dict[ph_word[i]]
            ph_word = ph_word[:i] + vless_item + ph_word[i + 1:]

    # Surface Palatalisation for CONS + 'j' + VOW
    i = 0
    while i <= len(ph_word)-3:
        if (
                ph_word[i] in non_pals and
                ph_word[i + 1] == 'j' and
                ph_word[i + 2] in ipa_vowels
        ):
            ph_word = ph_word[:i + 1] + PAL + ph_word[i + 1:]
        i = i + 1

    # Surface Palatalisation for CONS + 'i'
    i = 0
    while i < len(ph_word)-1:
        if (
                ph_word[i] in
                ['p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 'l', 'r', 'm'] and
                ph_word[i + 1] == 'i'
        ):
            ph_word = ph_word[:i + 1] + PAL + ph_word[i + 1:]
        i = i + 1

    return ph_word
