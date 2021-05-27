def dictdiff(d1, d2):
    l = []
    for key in d1:
        for aux_key in d2:
            if key == aux_key and d1[key] != d2[key]:
                l_aux = {}
                l_aux [f'{key}'] = [f'{d1[key]} - {d2[key]}']
                l.append(l_aux)

    for key in d1:    
        if not key in d2:
            l_aux = {}
            l_aux [f'{key}'] = [f'{d1[key]} - None']
            l.append(l_aux)

    for aux_key in d2:
        if not aux_key in d1:
            l_aux = {}
            l_aux [f'{aux_key}'] = [f'None - {d2[aux_key]}']
            l.append(l_aux)

    print (l)
    return l

if __name__ == "__main__":
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}
    dictdiff(d1, d2)
    d3 = {'a': 1, 'b': 2, 'd': 3}
    d4 = {'a': 1, 'b': 2, 'c': 4}
    dictdiff(d3, d4)
