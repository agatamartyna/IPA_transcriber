from app.segmentise import segmentise

def words_density(list):
    words_for_density = []
    for item in list:
        words_for_density.append((segmentise(item), item))

    return words_for_density
