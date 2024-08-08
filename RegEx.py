#[a-z]
import re
sen= "Bangladesh is a beautiful country"
c=re.findall("[a-z]",sen)
print(c)

#^
import re
sen= "Bangladesh is a beautiful country"
c=re.findall("^B",sen)
if c:
  print("Bangladesh is a brautiful country")
else:
  print("Bangladesh is not a beautiful country")  

#$
import re
sen= "Bangladesh is a beautiful country"
c=re.findall("country$",sen)
if c:
  print("Bangladesh is a brautiful country")
else:
  print("Bangladesh is not a beautiful country")    