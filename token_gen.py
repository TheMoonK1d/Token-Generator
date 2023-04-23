## STEPS ##
# Create a Hash function
 # Convert the string to bytes before hashing
 # Create a SHA-512 hash object
 # Update the hash object with the message
 # Get the hexadecimal representation of the hash
# Get user email
# Get UID (This is hard coded for testing...it should be fetched from firebase)
# Create a new key that holds 'email value' lowercased plus 'uid value' and pass it to the hash function
# Create a salt value (in our case a haiku poem about 'summer love' gernerated by ChatGPT)
# Create a second key that holds the reversed salt value
# Create a token by hashing the first key and the second key
##DONE
import hashlib
def hash(string):
    message = string.encode('utf-8')
    hash_object = hashlib.sha512()
    hash_object.update(message)
    hash_hex = hash_object.hexdigest()
    return hash_hex
email = input("Enter your email ")
uid = "8NkkeWLYd1asGQgBDlQFci6oLsQ2"
key_one = hash(email.lower()+uid)
salt = hash("SummerSunGlowing,WarmthIgnitesATenderFlame,LoveBloomsInTheHeat.")
key_two = salt[::-1]
token = hash(key_one+key_two)
print("Token: "+token)


