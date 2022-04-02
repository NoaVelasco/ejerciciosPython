# if __name__ == '__main__':
#     pyStudents = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         student = [name, score]
#         pyStudents.append(student)
        
        

# pyStudents = [['Harry', 37.21], ['Berry', 37.21], [
#     'Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
pyStudents = [['Harry', 36], ['Berry', 39], [
    'Tina', 46.2], ['Akriti', 41], ['Harsh', 39]]


def nota(n):
    return n[1]
   

pyStudents.sort(key=nota)

print(pyStudents)
mejor = pyStudents[0][1]

print(mejor)

segundones = list(filter(lambda nota:nota[1] != mejor, pyStudents))

print(segundones)

resultado = [x for x in segundones if x[1] == segundones[0][1]]

for i in sorted(resultado):
    print(i[0])

        
