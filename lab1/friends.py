users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
     count=0
    for r in friendship:
        if r[0]==user or r[1]==user:
            count= count+1
    return count
    pass

def sort_by_num_friends():
       friendcount=()
    for user in users:
        user_id = user["id"]
        num = num_friends(user_id)
        if len(friendcount)==0:
            friendcount=[(user["name"], num)]
        else:
            friendcount.append((user["name"], num))
    friendcount.sort(key = lambda x:int(x[1]), reverse = True)
    for f in friendcount:
        print(f)
    pass
sort_by_num_friends()
