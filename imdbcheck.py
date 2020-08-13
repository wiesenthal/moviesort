from imdb import IMDb
im = IMDb()

def checkAll(file):
    f = open(file, 'r')
    f2 = open('imdbOut.txt', 'w')
    for line in f.readlines():
        line = line.strip()
        print(line)
    
        movie = im.search_movie(line)[0]
        im.update(movie, info=['vote details'])
        f2.write(line + ': ')
        f2.write(str(movie['arithmetic mean']) + '\n')
        f2.flush()
    f.close()
    f2.close()

checkAll('out.txt')
