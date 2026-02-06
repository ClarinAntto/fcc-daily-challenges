#03-02-2026 | 03-03-2026

def mirror(string):
  return string + string[::-1]

'''def mirror(string):
    reverse_str = string[::-1]
    
    string = string + reverse_str
        (or)
    temp = string + reverse_str
    string = temp + reverse_str
    
    return string '''
