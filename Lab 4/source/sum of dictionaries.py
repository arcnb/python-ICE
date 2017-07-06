#Define a function to display sum of the integer elements
def intvaluesum(diction):
    for di in diction:
        #call the KEY labels which we want to combine
        X = di.pop('Lab1')
        Y = di.pop('Ice1')
        di['Lab1+Ice1'] = (X + Y)
    return diction
#List containing 3 dictionary elements
Details= [{'student1' : 'marks', 'Lab1' : 93, 'Ice1' : 91},
          {'student2' : 'marks', 'Lab1' : 95, 'Ice1' : 93},
          {'student3' : 'marks', 'Lab1' : 92, 'Ice1' : 96}]
#Displays the LIST which is effected by the defined function
print(intvaluesum(Details))

