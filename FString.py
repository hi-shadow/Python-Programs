fname = "gautam"
lname = "vaja"

# fullname = "my name is %s %s" % (fname, lname)  # this is not readable
# print(fullname)

# fullname = "this is {0} {1}"
# fullname = "my name is {} {}"
# name = fullname.format(fname, lname)  # this is also not a readable
# print(name)

# fullname = f"my name is {fname} {lname} "
# print(fullname)

# you can also a define anything in fString like
skils = ["javascript",  "react-js", "php",
         "html", "css ", "tailwind-css", "bootstrap"]
fullname = f"my name is {fname} {lname} and i have a skils of {skils} "
print(fullname)
