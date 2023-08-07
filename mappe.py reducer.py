#Approach 1


#!/usr/bin/env python

#mapper.py part
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')

    if len(columns) >= 10:  # Ensure the line has enough columns
        app_id = columns[1]
        num_games_owned = columns[8]

        try:
            num_games_owned = int(num_games_owned)
            print(f"{app_id}\t{num_games_owned}")
        except ValueError:
            pass

#recuder.py part
#!/usr/bin/env python

import sys

current_app_id = None
total_games_owned = 0
num_users = 0

for line in sys.stdin:
    line = line.strip()
    app_id, num_games_owned = line.split('\t')

    if current_app_id and current_app_id != app_id:
        average_games_owned = total_games_owned / num_users
        print(f"{current_app_id}\t{average_games_owned}")
        current_app_id = app_id
        total_games_owned = int(num_games_owned)
        num_users = 1
    else:
        current_app_id = app_id
        total_games_owned += int(num_games_owned)
        num_users += 1

if current_app_id:
    average_games_owned = total_games_owned / num_users
    print(f"{current_app_id}\t{average_games_owned}")



#Approach 2

#mapper.py part

#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    
    if len(fields) >= 12:
        steamid = fields[0]
        num_reviews = int(fields[10])
        print(f"{steamid}\t{num_reviews}")

#reducer.py part

#!/usr/bin/env python

import sys

current_steamid = None
total_reviews = 0
num_users = 0

for line in sys.stdin:
    steamid, num_reviews = line.strip().split('\t')
    num_reviews = int(num_reviews)
    
    if current_steamid == steamid:
        total_reviews += num_reviews
        num_users += 1
    else:
        if current_steamid:
            average_reviews = total_reviews / num_users
            print(f"{current_steamid}\t{average_reviews}")
        
        current_steamid = steamid
        total_reviews = num_reviews
        num_users = 1

if current_steamid:
    average_reviews = total_reviews / num_users
    print(f"{current_steamid}\t{average_reviews}")

