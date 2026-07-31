is_logged_in = True
has_permission = False

can_access = is_logged_in and not has_permission

print("Access Status:", can_access)
print("Is Logged In:", is_logged_in)
print("Has Permission:", has_permission)
print("Is 31 smaller than 26:", 31 < 26)