import random

students = ['LeBron James',
'Giannis Antetokounmpo',                
'Kevin Durant',
'Steph Curry',
'Kyrie Irving',
'Joel Embiid', 
'Kawhi Leonard', 
'Paul George', 
'James Harden', 
'Kemba Walker', 
'Khris Middleton', 
'Anthony Davis', 
'Nikola Jokić', 
'Klay Thompson', 
'Ben Simmons', 
'Damian Lillard', 
'Blake Griffin', 
'Russell Westbrook', 
'D\'Angelo Russell', 
'LaMarcus Aldridge', 
'Nikola Vučević', 
'Karl-Anthony Towns', 
'Kyle Lowry', 
'Bradley Beal', 
'Dwyane Wade', 
'Dirk Nowitzki']


def make_random_groups(students, number_of_groups):
    
    #Shuffle list of students
    random.shuffle(students)
    
    #Create groups
    all_groups = []
    for index in range(number_of_groups):
        group = students[index::number_of_groups]
        all_groups.append(group)
    
    #Format and display groups
    for index, group in enumerate(all_groups):
        print(f"✨Group {index+1}✨: {' / '.join(group)}\n")


make_random_groups(students, 10)