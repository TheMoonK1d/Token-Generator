### Collect the user's email and user ID (user id is hardcoded should be fetched from DB).
### Concatenate the email and user ID into a single string.
### Add a salt value
### Hash the string multiple times using a secure hashing algorithm (SHA-256).
### The resulting hash is the unique token for that user.
### On the backend, repeat the same steps to generate the same token and compare it to the token provided by the user to verify their identity.
