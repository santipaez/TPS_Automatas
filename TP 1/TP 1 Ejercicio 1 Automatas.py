def validate_string(s):
  conditions = [False] * 6
  conditions[0] = any(c.isalnum() for c in s)
  conditions[1] = s.isalpha() or any(c.isalpha() for c in s)
  conditions[2] = any(c.isupper() for c in s)
  conditions[3] = any(c.islower() for c in s)
  conditions[4] = s.isdecimal() or any(c.isdecimal() for c in s)
  conditions[5] = len(s) >= 8
  return conditions

s = input("Ingrese un string: ")
result = validate_string(s)
print(result)
