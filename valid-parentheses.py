#!/usr/bin/python3
def isValid(s: str) -> bool:
  brackets = {'(':')','[':']','{':'}'}
  prior = ''
  for char in s:
    if char in brackets.keys():
      prior = brackets[char] + prior
      continue
    if char in brackets.values() and len(prior):
        if char == prior[0]:
          prior = prior[1::]
          continue
        return False
    return False
  if len(prior):
    return False
  return True

string = '((){})'
print(isValid(string))
