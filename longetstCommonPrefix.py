def longestCommonPrefix(strs):
        index = 0
        prefix = ''
        if "" in strs:
            return prefix
        while(True):
            try:
              for current_word, next_word in zip(strs,strs[1:]):
                  try:
                    if index+1 <= len(next_word):   
                      # print(current_word,next_word)
                      if current_word[index] != next_word[index]:
                          return prefix
                      continue
                    return prefix
                  except IndexError:
                      return prefix
              prefix += current_word[index]
              index += 1
            except UnboundLocalError:
                return strs[0]

print(longestCommonPrefix(["a","ac"]))