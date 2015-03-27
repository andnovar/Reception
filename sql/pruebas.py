foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

foo2 = [2, 4, 7, 22, 24, 12]

print reduce(lambda x, y: x + y, foo)

#useful functions

nums = range(2,50)

#sentence = 'It is raining cats and dogs'
#words = sentence.split()
#print words
#['It', 'is', 'raining', 'cats', 'and', 'dogs']

#lengths = map(lambda word: len(word), words)
#print lengths
#[2, 2, 7, 4, 3, 4]


#import commands
#
#mount = commands.getoutput('mount -v')
#lines = mount.split('\n')
#points = map(lambda line: line.split()[2], lines)
# 
#print points
#['/', '/var', '/usr', '/usr/local', '/tmp', '/proc']


L = [2, 1, 4, 3, 5, 1, 2, 1, 1, 6, 5]
#S = set()
#M = []
#for e in L:
#    if e in S:
#        continue
#    S.add(e)
#    M.append(e)
#
#print M

M = list(set(L))
print M