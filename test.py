
#for i in range(0,10,1):
    #print(i)   
#animal = ["dog", "cat", "elefant"]

#for ani in animal:
    #print(ani)
    
    
#numbers = list(range(100))
  
#print(numbers)


#def hello(n):
    #i =0
    #while i < n:
        #print("hello")
        #i +=1

#def hello2(n):
    #"""This does nothing!"""
    
    #for i in range(n):
        #print("Hello")
        
    
#hello2(5)

#def print_all(*args):
    #for arg in args:
        #print(arg)
        
#print_all(1, 2, 3, 4, 5)
#print_all("apple", "banana", "cherry")
#print_all(1, "hello", [1, 2, 3], (4, 5, 6))

#print(print.__doc__)

#a = [0,1,2,3,4,5,6,7,8,9,10]
#power =[]

#for i in range(len(a)):
    #power.append(a[i]**2)
    
#print(power)


#answ = input("Enter your response: ")

# Define a set of affirmative answers
#yes_responses = {"yes", "yeah", "jop", "ok"}

#if answ in yes_responses:
    #print("you answered yes")


#s = "testing"

#setOfCharacters = set(s)
#print(setOfCharacters)

#lst = [1, 2, 2, 3, 4, 4, 4, 5]
#unique_set = set(lst)
#print(unique_set)

#for i in range(len(lst)):
    #print(lst[i])
    
#tel = {'jack': 4098, 'sape': 4139}
#tel['guido'] = 4127

#my_dict = {
 #   'name': 'Alice',
  #  'age': 30,
   # 'city': 'Wonderland'
#}




summary = []

with open("score2.txt", "r") as file:
    file_lines = file.readlines()

for line in file_lines:
    elements = line.strip().split()
    
    firstName = elements[-3]
    lastName = elements[-2]
    score = int(elements[-1])
    
    data = {
        'First Name': firstName,
        'Last Name' : lastName,
        'Score' : score
    }

    for entry in summary:
        if entry['First Name'] == firstName and entry['Last Name'] == lastName:
            entry['Score'] += data['Score']
            break
    else:
        summary.append(data)
    
for data in summary:
    print(data)
    
bestScore = max(entry['Score'] for entry in summary) 

print("Highest Scores:")
for entry in summary:
    if entry['Score'] == bestScore:
        firstName = entry['First Name']
        lastName = entry['Last Name']
        highestScore = entry['Score']
        print(f"Name: {firstName} {lastName}")
        print(f"Score: {highestScore}")




#for key, value in my_dict.items():
    #print(f'{key}: {value}')

    
    #python prog.py --getLotto to call a function from a different file in the cmd
    
    
    # with open('your_file_path.txt', 'r') as file:
    #for line in file:
        #prefix, number, first_name, last_name, another_number = line.split()
        #print(prefix, number, first_name, last_name, another_number)
        
        # Open the file for reading
#with open('your_file_path.txt', 'r') as file:
    # Iterate over each line in the file
    #for line in file:
        # Split the line into a list of values based on spaces
        #values = line.split()
        
        # Iterate over each value in the list
        #for value in values:
            #print(value)  # Or do any other processing you want