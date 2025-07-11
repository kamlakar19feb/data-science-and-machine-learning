def analyze_string_characters(input_string):
  counts={}
  for char in input_string:
    if char.isupper():
      if 'uppercase' in counts:
        counts['uppercase']+=1
      else:
        counts['uppercase']=1
    elif char.islower():
      if 'lowercase' in counts:
        counts['lowercase']+=1
      else:
        counts['lowercase']=1
    elif char.isdigit():
      if 'digit' in counts:
        counts['digit']+=1
      else:
        counts['digit']=1
    else:
      if 'special' in counts:
        counts['special']+=1
      else:
        counts['special']=1
  return counts
print(analyze_string_characters("Hello World123!_@"))