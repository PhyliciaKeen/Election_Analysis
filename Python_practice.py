print("Hello World")
print("Hello World")
type ('3')
type (3)
type (ballots)
type(73.81)
type("hello world")
type(True)
candidate_name = "Pete"
5+2*3
8//5-3
8+22*2-4
16-3/2+7-1
3**3%5
5+9*3/2-4
(5+2)*3
(8//5)-3
8+(22*(2-4))
16-3/(2+7)-1
3**(3%5)
5+(9*3/2-4)
5+(9*3/(2-4))
counties = ["Arapahoe","Denver","Jefferson"]
counties
counties[0]
print(counties[-1])
print(counties[-2])
len(counties)
counties[0:2]
counties[0:1]
counties[:2]
counties[1:]
counties.append("El Paso")
counties
counties.insert(2, "El Paso")
counties
counties.remove("El Paso")
counties
counties.pop(3)
counties[2] = "El Paso"
counties
list.append("Jefferson")
counties.append("Jefferson")
counties
counties.insert(1, "El Paso")
counties
counties.remove("Arapahoe")
counties
counties.insert(2, "Denver")
counties.insert(1, "Jefferson")
counties
counties.remove("Denver")
counties.remove("Jefferson")
counties
counties.remove("Denver")
counties.remove("Jefferson")
counties.insert(2, "Denver")
counties.insert(1, "Jefferson")
counties
counties.remove("El Paso")
counties
counties.remove("El Paso")
counties
counties.insert(0, "EL Paso")
counties
counties.append("Arapahoe")
counties
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
counties_tuple[1]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters": 422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
voting_data
voting_data.remove({"county","Arapahoe","registered_voters",422829})
voting_data
voting_data.insert(2,{"county":"El Paso","registered_voters":461149})
voting_data.remove({"county":"Arapahoe","registered_voters":422829})
voting_data
voting_data.remove({"county":"El Paso","registered_voters":461149})
voting_data
voting_data.remove({"county":"Denver","registered_voters":463353})
voting_data
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data
counties
counties = ["Arapahoe","Denver","Jefferson"]
counties
if counties[1]=="Denver"
    print(counties[1])
temperature =(input("What is the temperature outside?"))
if temperature > 80:
        print("Turn on the AC")
else:
        print("open the windows")
#What is the score?
score = int(input("What is your test score"))

#Determine the grade.
if score >= 90:
        print('Your frade is an A')
else:
    if score >= 80:
        print("your grade is a B")
    else:
        if score >= 70:
            print("Your grade is a C")
        else:
            if score >= 60:
                print("Your grade is a D")
            else:
                print("Your grade is an F")
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
if "Arapahoe" in counties and "El Paso" in counties:
        print("Arapahoe and El Paso are in the list of counties.")
else:
        print("Arapahoe" or "El Paso is not the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
x = 0
while x <= 5:
    print(x)
    x = x + 1
for county in counties:
        print(county)
counties =["Arapahoe","Denver","Jefferson"]
counties
for county in counties:
    print(county)
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)
for i in range(len(counties))
    print(counties[i])

for num in range(5)
print(num)

for i in range(len(counties)
print(counties[i])

for county in counties_dict:
    print(county)
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)    
for num in range(5):
    print(num)    
for i in range(len(counties)):
    print(counties[1]) 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(counties)
counties = "Arapahoe", "Denver", "Jefferson"
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])

for county,voters in counties_dict.items():
    print(county, voters)
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered Voters,')
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    print(county_dict['county'])  
message_to_candidates = (f"You received{candidate_votes:.} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received{candidate_votes / total_votes * 100:.2f}% of the total votes.")
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidates = (f"You received{candidate_votes:.} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received{candidate_votes / total_votes * 100:.2f}% of the total votes.")
