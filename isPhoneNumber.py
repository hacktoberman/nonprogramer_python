def is_Phone?_Number(text):
  if len(text) != 12
    return False
  for i in range(0,3):
    if not text[i].isdecimal():
      return False
  if text[3] != '-':
    return False
  for i in range(4,7):
    if not text[i].isdecimal():
      return False
  if text[7] != '-':
      return False
  for i in range(8,12):
    if not text[i].isdecimal():
      return Falase
  return True

print('Phone Number is 411-321-3211')