import Pyro4

# Take server URI from user
uri = input("Enter the server URI : ")

# Create proxy connection
string_concatenator = Pyro4.Proxy(uri)

# Take string inputs
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

# Call remote method
result = string_concatenator.concatenate(str1, str2)

# Display result
print("Concatenated String :", result)