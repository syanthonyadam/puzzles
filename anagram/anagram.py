def find_anagrams(word, candidates):
    
    input_list = [x for x in word.lower()] # obtaining a list of all letters
    input_dict = {} # initializing empty dictionary
    result_list = []

    for letter in input_list:
        if letter not in input_dict.keys():
            input_dict[letter] = 1
        else:
            input_dict[letter] = input_dict[letter] + 1

    for cand in candidates:
        cand_list = [x for x in cand.lower()] # obtaining the candidate list
        cand_dict = {} # empty dictionary

        for letter in cand_list:
            if letter not in cand_dict.keys():
                cand_dict[letter] = 1
            else:
                cand_dict[letter] = cand_dict[letter] + 1

        if input_dict == cand_dict:
            result_list.append(cand)

    return result_list

