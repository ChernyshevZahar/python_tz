def calculzto(name, prise, bonus):
    
    reselt = {name[i]: round(prise[i] * float(bonus[i].strip('%'))/100,2) for i in range(len(name))}
    return reselt

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]


print(calculzto(names,salary,bonus))