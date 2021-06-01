class Scoop():

    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoop(self, *args) -> None:
        for s in args:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(s)
            else:
                print("Bowl has reached max scoops!")

    def __repr__(self) -> str:
        return '\n'.join(f.flavor for f in self.scoops) 

class SuperBowl(Bowl):
    max_scoops = 5

    def __init__(self):
        super().__init__()

    def add_scoop(self, *args) -> None:
        for s in args:
            if len(self.scoops) < SuperBowl.max_scoops:
                self.scoops.append(s)
            else:
                print (f'Super bowl has reached max scoops!')

    def __str__(self) -> str:
        values = ''
        for f in self.scoops:
            values = values + f.flavor + ' '
        return f'Super bowl: {values}'

    

if __name__ == "__main__":
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')
    
    b = Bowl()
    b.add_scoop(s1, s2)
    b.add_scoop(s3)
    print(b)

    sb = SuperBowl()
    sb.add_scoop(s1, s2, s3) # 3 scoops
    print(sb)
    sb.add_scoop(s1) # 4 scoops
    print(sb)

    sb.add_scoop(s1) # 5 scoops
    sb.add_scoop(s2) # 6 scoops - limit!
