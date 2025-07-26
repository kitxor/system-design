

READ = (1<<0)
WRITE = (1<<1)
EXECUTE = (1<<2)

permission = 5

if permission & READ:
    print("user can read")
else:
    print("user can not read")


if permission & WRITE:
    print("user can write")
else:
    print("user can not write")

if permission & EXECUTE:
    print("user can execute")
else:
    print("user can not execute")


print("assigning write permission")

#give write permission
permission = permission | WRITE


print(f"After adding WRITE: {bin(permission)}")
print(f"Decimal: {permission}")


permission = permission & ~EXECUTE
print(f"after removing EXECUTE: {bin(permission)}")
print(f"decimal: {permission}")


permission = permission ^ WRITE
print(f"after toggling write: {bin(permission)}")
print(f"decimal: {permission}")

print("toggle again")
permission = permission ^ WRITE
print(f"after toggling write: {bin(permission)}")
print(f"decimal: {permission}")
