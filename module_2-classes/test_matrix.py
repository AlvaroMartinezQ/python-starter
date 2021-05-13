from matrix import Matrix

if __name__ == "__main__":
    m1= Matrix(3,3,0)
    for value in m1:
        print(value)
    
    m1[0][0]=35
     
    m2 = Matrix(3, 3,11)
    print(m1)
    print(m2)
    print(m1 + m2)
    print(m1 - m2)
     
    m2 += m2
    m2[2][1] = 3
    print(m2)
    
    m2.transpose()
    print(m2)
    
    print((m2 == m1))
    print(m2.get_rank())
