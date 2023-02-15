# we use hashing to save users password as a hashed value
import requests
#url = 'https://api.pwnedpasswords.com/range'+'password'#password
#url = 'https://api.pwnedpasswords.com/range'+'5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8' # here we have to provide hashed value to prevent leakage of passsowrd
url = 'https://api.pwnedpasswords.com/range/'+'5BAA6' #providinf only first five characters as there is a chance of the hash code getting hacked


response = requests.get(url)
print(response) # gives positive response and if it is 400 it means that the connection is not secured 
# if the response is 200 it is  secured
# the api gives all the hacked passwords that start with the given hash code

