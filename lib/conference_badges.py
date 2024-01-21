def badge_maker(name):
    name_of_person = f'Hello, my name is {name}.'
    return name_of_person

def batch_badge_creator(names):
    list_name = []
    for name in names:
        list_name.append(f'Hello, my name is {name}.')
       
    return list_name

def assign_rooms(names):
    list_name =[]
    rooms = [1,2,3,4,5,6,7,8]
    for i in range(len(names)):
        if i < len(rooms):
              list_name.append(f"Hello, {names[i]}! You'll be assigned to room {rooms[i]}!")
        else:
             return "There are no enough rooms for the users"
    return list_name
              

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assignment in assign_rooms(names):
        print(assignment)