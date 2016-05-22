def lista(num):    
    pessoa = range(1,1 + num)
    while len(pessoa) > 1: 
        print pessoa
        pessoa = pessoa[2:] + pessoa[0:1]
    print pessoa
