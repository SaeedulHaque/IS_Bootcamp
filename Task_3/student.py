students = ["Alice", "Bob", "Charlie", "David", "Eve"]
selected=[]
for i in range(len(students)):
    if students[i][0]=="A" or students[i][0]=="D":
        selected.append(students[i])

print("The selected students are:",selected)