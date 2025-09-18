# PASSWORD CHECKER

password = input("Enter password: ")

if not any( p in "!/$~*@"
           for p in password):
    print("Invalid Password(must contain ! or * or @)")
elif len(password) <9:
    print("Weak Password")
elif len(password) < 15:
    print("Moderate Password")
else:
    print("Strong Password ✅")
