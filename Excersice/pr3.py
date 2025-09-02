student_scores={"Avdesh":{'age':22,'Marks':100},"Sumit":{'age':22,'Marks':75},"Komal":{'age':22,'Marks':100}}
print(student_scores['Avdesh'])
print(student_scores.keys())
print(student_scores.values())
print(student_scores.items())
new_student={"Aryan":{'age':22,'Marks':50},"Amit":{'age':22,'Marks':50}}
student_scores.update(new_student)
print(student_scores)
