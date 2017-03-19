# A very simple music recommender system

import os

PREF_FILE = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 
                'music-rec-store.txt'
            )


def load_users(file_name):
    '''Reads in a file of stored users' preferences
    stored in "file_name." Returns a dictionary containing
    a mapping of user names to a list of preferred artists
    '''
    with open(file_name, 'r') as fin:
        user_dict = dict()
        for line in fin:
            # Read and parse a single line
            user_name, bands = line.strip().split(':')
            band_list = bands.split(',')
            band_list.sort()
            user_dict[user_name] = band_list
    return user_dict
    
    
def get_preferences(user_name, user_map):
    '''Returns a list of the user's preferred artists.
    
        If the system already knows about the user,
        it gets the preferences out of the user_map
        dictionary and then asks the user if they have
        additional preferences. If the user is new,
        it simply askss the user for their preferneces...
    '''
    new_pref = ''
    if user_name in user_map:
        prefs = user_map[user_name]
        print("I  see that  you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please entere another artist or band that you")
        print("like, or just press enter")
        new_pref = input("to see your recommendations: ")
    else:
        prefs = list()
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        new_pref = input("that you like: ")
    
    while new_pref != '':
        prefs.append(new_pref.strip().title())
        print("Please entere another artist of band that you")
        print("like, or just press entere")
        new_pref = input("to see your recommendations: ")
        
    # Always keep the lists in sorted order for ease of comparison
    prefs.sort()
    return prefs
    
    
def get_recommendations(curr_user, prefs, user_map):
    '''Gets recommendations for a user (curr_user) based
        on the users in user_map (a dictionary) and the
        user's preferences in prefs (a list).
        Returns a list of recommended artists.
    '''
    best_user = find_best_user(curr_user, prefs, user_map)
    recommendations = drop(prefs, user_map[best_user])
    return recommendations
    
    
def find_best_user(curr_user, prefs, user_map):
    '''Find the user whose tastes are closest to the current
        user. Return the best user's name (a string)
    '''
    users = user_map.keys()
    best_user = None
    best_score = -1
    for user in users:
        score = num_matches(prefs, user_map[user])
        if score > best_score and curr_user != user:
            best_score = score
            best_user = user
    return best_user
    
    
def drop(list1, list2):
    '''Return a new list that contains only the elements
        in list2 that were NOT in list1.
    '''
    list3 = list()
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    return list3
    
    
def num_matches(list1, list2):
    '''
    Returns the number of elements that match
    between two sorted lists.
    '''
    matches = 0
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches
    
    
def save_user_preferences(user_name, prefs, user_map, file_name):
    '''
    Writes all of the user preferences to the
    file and returns nothing (None).
    '''
    user_map[user_name] = prefs
    with open(file_name, 'w') as fout:
        for user in user_map:
            to_save = '{}:{}'.format(user, ','.join(user_map[user]))
            fout.write(to_save)

            
def main():
    '''The main recommendation function'''
    user_map = load_users(PREF_FILE)
    print("Welcome to the music recommender system!")
    
    user_name = input("Please enter your name: ")
    print("Welcome, {}".format(user_name))
    
    prefs = get_preferences(user_name, user_map)
    recs = get_recommendations(user_name, prefs, user_map)
    
    # Print the user's recommendations
    if len(recs) == 0:
        print("I'm sorry but I have no recommendations")
        print("for you right now.")
    else:
        print("{} based on the users I currently".format(user_name))
        print("know about, I believe you might like:")
        for artist in recs:
            print(artist)
            
        print("I hope you enjoy them! I will save your")
        print("preferred artists and have new")
        print("recommendations for you in the future")
        
    save_user_preferences(user_name, prefs, user_map, PREF_FILE)
    
    
if __name__ == '__main__': main()