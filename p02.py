anos = 0
pop1 = 80000
pop2 = 200000
taxa1 = 0.03
taxa2 = 0.015
while (pop1<pop2):
    anos +=1
    pop1 = pop1 + (pop1*taxa1)
    pop2 = pop2 + (pop2*taxa2)
print(f'A população do país A levará {anos} anos para ultrapassar o país B')
print(f"População País A:{round(pop1)}")
print(f"População País B:{round(pop2)}")








