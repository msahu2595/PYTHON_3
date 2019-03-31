roll_no = [1,2,3,4]
maths = [100,90,80,70]
science = [90,70,60,50]
english = [100,99,95,85]
percentage = []

for marks in list(zip(maths, science, english)):
    percentage.append(round((sum(marks)/(len(marks)*100))*100,2))
print(percentage)

def percentage_stu(*args):
    percentage2 = []
    for marks in list(zip(*args)):
        percentage2.append(round((sum(marks)/(len(marks)*100))*100,2))
    return percentage2
print(percentage_stu([100,90,80,70], [90,70,60,50], [100,99,95,85]))

percentage_stu_new = lambda *args : [((sum(marks)/(len(marks)*100))*100) for marks in list(zip(*args))]
print(percentage_stu_new([100,90,80,70], [90,70,60,50], [100,99,95,85]))



