# GuviUserRegistration

User registratin:
  email/username should have "@" and followed by "." eg:- sherlock@gmail.com,nothing@yahoo.in
  It should not be like this eg:- @gmail.com
  there should not be any "." immediate next to "@" eg:-my@.in

password:
  (5 < password length > 16)
  Must have minimum one special character,
  one digit,
  one uppercase,
  one lowercase character

Once the username and password are validated,
  store those values in a file "Registered_Users.txt"

Login
  1. When the user chooses to Login, check whether his/her credentials exist in the file or not based on the user input
  2. If doesn’t exist ask them to go for Registration.
  3. If they have chosen forget password you should be able to retrieve their original password based on their username provided in the user input
  4. If nothing matches in your file you should ask them to Register
