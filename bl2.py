'''
We are given a string S representing a phone number, which we would like to reformat. String S consists of N characters: digits, spaces and/or dashes. It contains at least two digits.
Spaces and dashes in string S can be ignored. We want to reformat the given phone number in such a way that the digits are grouped in blocks of length three, separated by single dashes. 
If necessary, the final block or the last two blocks can be of length two.
For example, given string S = "00-44 48 5555 8361", we would like to format it as "004-448-555-583-61".
'''

def solution(numberStr):
  number_only = [x for x in numberStr if x.isdigit()]
  numdigits = len(number_only)
  newdigit = ''
  for i in range(1,numdigits+1):
    if numdigits % 3 != 1 or (numdigits - i)>2:
      if (i-1) % 3 == 0 and i>1:
        newdigit += '-'
    else:
      if (numdigits - (i-1)) == 2:
        newdigit += '-'
    newdigit += number_only[i-1]
  return newdigit

print(solution('00-44 48 5555 8361'))
print(solution('0 - 22 1985--324'))
print(solution('555372654'))
print(solution('5553'))
print(solution('55'))
print(solution('55-5'))
