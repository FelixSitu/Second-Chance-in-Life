def for_version(items):
   result = []
   for i in range(len(items) - 1, -1, -1):
      result.append(items[i])
   return result

def while_version(items):
   result = []
   index = len(items)-1
   while index >= 0:
      result.append(items[index])
      index -=1
   return result
