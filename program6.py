men_preferences = {
    'a': ['v', 'w', 'x'],
    'b': ['w', 'v', 'x'],
    'c': ['v', 'w', 'x']
}

women_preferences = {
    'v': ['a', 'b', 'c'],
    'w': ['b', 'c', 'a'],
    'x': ['c', 'a', 'b']
}

engaged_men = []
engaged_women = []
stable_marriages = []

for man in men_preferences.keys():
    while man not in engaged_men:
        for j in range(3):
            woman = men_preferences[man][j]
            
            if woman not in engaged_women:
                stable_marriages.append([man,woman])
                engaged_men.append(man)
                engaged_women.append(woman)
                break
            else:
                idx_current_engagement = engaged_women.index(woman)
                idx_current_partner = women_preferences[woman].index(engaged_men[idx_current_engagement])
                idx_new_partner = women_preferences[woman].index(man)
                if idx_new_partner < idx_current_partner:
                    engaged_men[idx_current_engagement] = None
                    engaged_men.append(man)
                    engaged_women[idx_current_management] = woman
                    break
print(stable_marriages)
