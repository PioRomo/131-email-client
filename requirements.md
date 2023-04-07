---- Functional Requirements ----
* The website will be able to send emails
* The website will allow you to create account
* The website will allow you to create a profile and manage it
* The website will have verification through phone number
* The website will be able to send messages
* The website will be able to create/add/remove To Do List
* The website will be able to search for emails
* The website will allow you to switch between clients
* The website will send users notifications
* The website will allow users to organize folders
* The website will allow users to create a contact Book
* The website will implement a Password Requirement

---- Non-functional Requirements ----
* The website will allow for dark and light theme
* The website will run on Google Chrome

---- Func.Req. Use Cases ----
1) The website will be able to send emails 
  > Summary: This app will allow users to send emails to other users
  > Pre-condition: User must be logged in
  > Trigger: "Send" button must be clicked
  > Primary Sequence: 
      > "Send" pop-up with send functionality appears at the bottom right of the screen
      > User inputs email and email content
      > User can optionally input subject, or add images/files
      > User clicks send, and the email is sent
  > Primary Post-Conditions: Email is sent and will be received by receiver
  > Alternative Sequence: 
      > "Send" pop-up with send functionality appears at the bottom right of the screen
      > User inputs email and email content
      > Email does not exist, or is invalid
      > Pop-up prompts user to re-enter email and try again
 
2) The website will you to create an account 
  > Summary: Users will be able to register themselves for our app by creating an account
  > Pre-condition: Users must have a valid phone number
  > Trigger: Clicking the "Create Account" button 
  > Primary Sequence: 
      > Website takes user to account creation page
      > User inputs their phone number
      > User is send verification code through phone number
      > Website prompts user to input verification code 
      > User inputs verification code and is taken to password creation page
      > Website prompts user to create and re-enter password that follows listed criteria
      > User clicks "Welcome" button
  > Primary Post-Conditions: User is now registered and taken to the home page
  > Alternative Sequence: 
      > User enters invalid phone number
      > Website displays error message 
      > Website prompts user to re-enter phone number
   
3) The website will allow you to create a profile and manage it 
4) The website will have verification through phone number 
  > Summary: User will be able to log in with security
  > Pre-condition: User must be on log in page
  > Trigger: "Login" button must be clicked
  > Primary Sequence: 
      > User inputs their login information
      > User clicks login 
      > User will get a verication code sent to their phone number
      > User will enter the verification code and click verify
  > Primary Post-Conditions: User is now verified and logged into the website
  > Alternative Sequence: 
      > User inputs their login information
      > User clicks login
      > User inputs the incorrect code 
      > Pop-up prompts user "incorrect code, please enter the correct code." 

5) The website will be able to send messages
6) The website will be able to create/add/remove toDoList
7) The website will be able to search for email
> Summary: Users will be able to search for a desired email
  > Pre-condition: Users must be logged in and in the inbox
  > Trigger: Clicking the "Search" button 
  > Primary Sequence: 
      > Website takes user to user's inbox
      > User clicks the Search button
      > User inputs keywords into search bar
      > Website prompts user with emails containing keywords 
      > User selects desired email
  > Primary Post-Conditions: User has found the email that they are looking for
  > Alternative Sequence: 
      > User enters unknown keywords
      > Website displays "No emails matched your search"
      > Website prompts user to re-enter keywords
8) The website will implement a password requirement
> Summary: Users must input a password that satisfies the website's password requirement
  > Pre-condition: Users must be in the "Password Creation" page
  > Trigger: Inputting the verification code sent to the phone number
  > Primary Sequence: 
      > Website takes user to "Password Creation" page
      > User inputs password that they want for their email
      > Website checks if the password satisfies the requirements
      > Website prompts user to input the password they inputted again
      > User selects "Welcome"
  > Primary Post-Conditions: User is now registered and taken to the home page
  > Alternative Sequence: 
      > User enters an invalid password
      > Website displays error message
      > Website prompts user to re-enter a qualifying password
      > User enters incorrect password
      > Website displays error message
      > Website prompts user to re-enter the same qualifying password
