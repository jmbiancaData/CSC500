
# Dictionaries 
room_number = {'CSC101': 3004, 'CSC102': 4501, 'CSC103': 6755, 'NET110': 1244, 'COM241': 1411}
instructors = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich', 'NET110': 'Burke', 'COM241': 'Lee'}
meeting_time = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.', 'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.', 'COM241': '1:00 p.m.'}

# Ask for user to enter course number
course = input('Enter the course number: ')

# display course, room, instructor, and time
print('Course {} is in room #{} with instructor {}, at {}'.format(course,room_number[course],instructors[course],meeting_time[course]))