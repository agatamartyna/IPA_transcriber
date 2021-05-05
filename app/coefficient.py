from app.density import neighbourhood_density
from app.segmentise import segmentise

ds = ["kit", "kot", "kat", "kel", "ker", "tet", "net", "het", "ot", "hot", "it", "sket", "oket", "keto"]
ls = ["lepizod", "mepizod", "epizody", "epizodu", "epizodo", "erpizod", "epizold"]


ls = ["kit", "wit"]
words_segmentised = []
for l in ls:
    words_segmentised.append((segmentise(l), l))


# get neighbours of a given word
neighbours = neighbourhood_density("skit", words_segmentised)
# prepare the neighbours for other neighbour-search
neighbours_segmentised = []
for neighbour in neighbours:
    neighbours_segmentised.append((segmentise(neighbour), neighbour))
# get neighbours of neighbours
neighbours_neighbours = []
for neighbour in neighbours:
    neighbour_neighbour = neighbourhood_density(neighbour, neighbours_segmentised)
    for n_n in neighbour_neighbour:
        neighbours_neighbours.append((neighbour, n_n))

#remove reccurring pairs
tuples = []
for tupl in neighbours_neighbours:
    if (tupl[1], tupl[0]) not in tuples:
        tuples.append(tupl)

# get separate items
coefficient_cluster = []
for tupl in tuples:
    if tupl[0] not in coefficient_cluster:
        coefficient_cluster.append(tupl[0])
    if tupl[1] not in coefficient_cluster:
        coefficient_cluster.append(tupl[1])

print(words_segmentised)
