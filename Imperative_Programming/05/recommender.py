def greeting():
  name = input('What is your name? ')
  print('Nice to meet you {name}!'.format(name=name))
  
  
def numMatches(list1, list2):
  '''Returns the number of elements that match between
     the lists userPrefs and storedUserPrefs.'''
  matches, i, j = 0, 0, 0
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
  
  
def findBestUser(userPrefs, allUsersPrefs):
  '''Given a list of user artist preferences and a
    list of lists representing all stored users'
    preferences, return the index of the stored
    user with the most matches to the current user.'''
    max_matches = 0 # no matches found yet!
    best_index = 0
    for index, pref_list in enumerate(allUsersPrefs):
      curr_matches = numMatches(userPrefs, pref_list)
      if curr_matches > max_matches:
        max_matches = curr_matches
        best_index = index
    return best_index