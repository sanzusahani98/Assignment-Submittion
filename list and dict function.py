#Question 1
#Do Experiment with 5 List's In-built functions and post it to Github
List = ['Maths', 'chemistry', 'physics','english'] 
List.append('hindi') 
print(List)


List = ['Maths', 'chemistry', 'physics','english'] 
List.insert(2,'geography')      
print(List)  



List1 = [1, 2, 3, 7] 
List2 = [2, 3, 4, 5, 8] 
List1.extend(List2)         
print(List1) 


List = [1, 2, 3, 4, 5] 
print(sum(List)) 




List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.count(1))


#Question 2
#Do Experiment with 5 Dictionary’s In-Built Functions, and post it to Github

dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}
print(dict.keys())


dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}
print(dict.items())


dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}
print(dict.values())


dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}
dict.pop('Marks')
print(dict)


dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}
dict.pop('Marks')
print(dict)