# Immutable bytes means cannot be changed after creation.
raw_bytes = b"Hello, Vincent!"

# Mutable bytearray means can be changed after creation.
byte_arr = bytearray(raw_bytes)
byte_arr[0] = 74  # The 74 is a ASCII value for 'J', so it changes the first character from 'H' to 'J'.
print("Raw Bytes:", raw_bytes)
print("Byte Array:", byte_arr)