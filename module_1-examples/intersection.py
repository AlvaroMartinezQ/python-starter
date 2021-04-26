# Receives 2 sequences and returns its intersection
# if value from seq2 is in seq1, add it to the list to print (if it hasn't been added yet)

def sec(s1, s2):
    ret = []
    for val1 in s1:
        for val2 in s2:
            if val1==val2 and not val2 in ret:
                ret.append(val1)
    
    print(ret)

seq1 = ['c','a','s','a']
seq2 = ['a']

sec(seq1, seq2)

seq1 = [1,2,1,1,1,1,3,4,5,6,2,2,3,7,7,8,9,0]
seq2 = [1,7]

sec(seq1, seq2)

seq1 = ["hola", "hola mundo"]
seq2 = ["hola"]

sec(seq1, seq2)
