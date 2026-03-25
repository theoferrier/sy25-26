seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
winners = ['Purdue', 'FDU', 'FAU', 'Memphis', 'Duke', 'Oral Roberts', 'UVA', 'Furman', 'Kentucky', 'Pitt', 'Kansas', 'Howard', 'Texas', 'Penn St', 'UCLA', 'UNC Asheville']

def detect_cinderella_story(seeds, winners):
    cinderella_stories = []
    for seed, winner in zip(seeds, winners):
        if seed >= 10:
            cinderella_stories.append((seed, winner))
    return cinderella_stories
