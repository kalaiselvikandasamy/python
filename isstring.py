def new_string(str):
  if(len>=2 and str[:2]=="is"):
    return str
  else:
    return "is" + str
print(new_string("array"))
print(new_string("isempty"))
