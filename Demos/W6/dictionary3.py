song = '''
Humpty Dumpty sat on a wall"
Humpty Dumpty, had a great fall"
All the king's horses and all the king's men"
Couldn't put Humpty together again"
Humpty Dumpty sat, on a wall"
Humpty Dumpty had a great, fall"
All the king's horses and all the king's men
Couldn't put, Humpty together, again"
Humpty Dumpty…"


'''


print(song.lower().replace("\"", "").replace("\'", "").replace(",", "").split())
print(len(song.lower().replace("\"", "").replace("\'", "").replace(",", "").split()))
print(len(set(song.lower().replace("\"", "").replace("\'", "").replace(",", "").split())))