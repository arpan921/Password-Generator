import random
def return_character(character_list):
  position = random.randint(0,len(character_list)-1)
  return character_list[position]
  
def make_random_list(list_of_characters,number_of_allowed_char):
    return_list=[]
    for character in range(number_of_allowed_char):
        position = random.randint(0,len(list_of_characters)-1)
        return_list.append(list_of_characters[position])
    return return_list

def randomize_characters(character_list):
    final_result = []
    length = len(character_list)
    for i in range(length):
        final_result.insert(i,'..')

    for i in range(length):
        position = random.randint(0,length-1)
        if final_result[position]=='..':
            final_result[position]=character_list[i]
        else:
            while(final_result[position]!='..'):
                position = random.randint(0,length-1)
            final_result[position]=character_list[i]

    return final_result
            


        



  