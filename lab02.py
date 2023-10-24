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
        
        # Maria Johansson 37 and Kristina Larsson 37