print('Welcome to the Tip Calculator!')
total = float(input('What was the total bill? $'))
tip_percentage = int(input('How much tip would you like to give? 10, 12, or 15? '))
num_of_people = int(input('How many people to split the bill? 126'))
tip = total * (tip_percentage / 100)
total_by_person = round((total+tip) / num_of_people, 2)
print(f"Each person should pay: ${total_by_person}")