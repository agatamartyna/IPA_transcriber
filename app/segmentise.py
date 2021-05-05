from app.models_Warsaw import transcribe_text_Warsaw

doubles = {
    'ts':'VS_ALV_AFF',
    't\u0255':'VS_PAL_AFF',
    't\u0282':'VS_POSTALV_AFF',
    'd\u0291':'VD_PAL_AFF',
    'dz':'VD_ALV_AFF',
    'd\u0290': 'VD_POSTALV_AFF'
}

def segmentise(word):
    word_items = [item for item in transcribe_text_Warsaw(word)]

    for i in range(len(word_items) - 4):
        if word_items[i:i+4] == ['ɛ', '̃', 'w', '̃'] or word_items[i:i+4] == ['ɔ', '̃', 'w', '̃']:
            word_items[i] = ''.join(word_items[i:i+4])
            for j in range(3):
                word_items.remove(word_items[i + 1])
                word_items.append(' ')

    for i in range(len(word_items) - 1):
        if word_items[i] + word_items[i+1] in doubles:
            word_items[i] = word_items[i] + word_items[i+1]
            word_items.remove(word_items[i+1])
            word_items.append(' ')

    for i in range(len(word_items) - 1):
        if word_items[i+1] == 'ʲ':
            word_items[i] = word_items[i] + word_items[i+1]
            word_items.remove(word_items[i+1])
            word_items.append(' ')

    word_items = [item for item in word_items if item != ' ']

    # remove palatalisation
    word_segmentised = []
    for item in word_items:
        if len(item) == 2 and item[1] == 'ʲ':
            word_segmentised.append(item[0])
        else:
            word_segmentised.append(item)

    return word_segmentised

