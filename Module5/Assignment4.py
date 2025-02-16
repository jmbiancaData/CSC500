# Part 1

# Rainfall aggregator
num_months = 0
total_rain = 0
avg_rain = 0


num_years = int(input("Enter the number of years to enter rainfall results for: "))

for i in range(1, num_years + 1):
    print('Rainfall for year {}'.format(i))
    for j in range(1,13):
        rain = float(input("Rainfall in inches for month {}: ".format(j)))
        total_rain += rain
        num_months +=1

avg_rain = total_rain / num_months

print('\nRainfall results:')
print('Months: {:.0f}'.format(num_months))
print('Total rain: {}'.format(total_rain))
print('Average rain: {}'.format(avg_rain)) 

# new lines to separate output
print()
print()
# Part 2

# Bookstore points

points = 0
num_books = int(input("Enter the number of books purchased over the last month: "))

if num_books < 2:
    points = 0
elif num_books < 4:
    points = 5
elif num_books < 6:
    points = 15
elif num_books < 8:
    points = 30
elif num_books >= 8:
    points = 60

print("Points:")
print("You have {} points because you purchased {} book(s)".format(points, num_books))