import re

email_pattern ="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|edu|in)";
po_pattern="([+]\d{2})?\d{10}"
aadhar_pattern="[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}"
date_pattern="(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.]([0-9]{4})"
temp=input()

if(temp.find("email" or "EMAIL" or "Email")):
  email=re.search(email_pattern,temp)
else:
  email=re.search(email_pattern,temp)

po=re.search(po_pattern,temp)

m=re.search(aadhar_pattern,temp)

dat=re.search(date_pattern,temp)

print(email.group())
print(po.group())

print(m.group())
print(dat.group())
