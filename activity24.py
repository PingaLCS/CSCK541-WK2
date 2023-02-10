import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

x = re.findall("ai", txt)
print(x)

anchor = 'The ship set sail on the ocean'
anchor_n = 'Ships set sail on the ocean to go places'

anchor01 = re.findall('^[Tt]he', anchor)
print(anchor01)
