## Functional Requirements 
* [The website will be able to send emails](#the-website-will-be-able-to-send-emails)
* [The website will allow you to create account](#the-website-will-you-to-create-an-account)
* [The website will allow you to create a profile and manage it](#the-website-will-allow-you-to-create-a-profile-and-manage-it)
* [The website will have verification through phone number](#the-website-will-have-verification-through-phone-number)
* [The website will be able to send messages](#the-website-will-be-able-to-send-messages)
* [The website will be able to create/add/remove To Do List](#the-website-will-be-able-to-create/add/remove-toDoList)
* [The website will be able to search for emails](#the-website-will-be-able-to-search-for-email)
* The website will allow users to change passwords if the users forgot their password
* The website will send users notifications after user action
* The website will allow users to save/archive emails
* The website will allow users to create a contact Book
* [The website will allow users to delete emails](#the-website-will-be-able-to-delete-emails)

## Non-functional Requirements 
* The website will allow for dark and light theme
* The website will run on Google Chrome

## Func.Req. Use Cases
#### The website will be able to send emails 
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
 
## The website will you to create an account 
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
   
  ## The website will allow you to create a profile and manage it 
  > Summary: User will be able to create a profile and change it 
  > Pre-condition: User must be logged in
  > Trigger: user clicks the edit profile button
  > Primary Sequence:
      > User logs in/registers for an account 
      > User navigates to profile screen
      > User clicks "change profile" icon
      > User uploads a new photo
      > User clicks "upload"
  > Primary Post-Condition: User now has an updated profile
  > Alternative Sequence: 
      > User is prompted to edit profile picture 
      > User uploads a non-image file 
      > System prompts user to upload valid file

## The website will have verification through phone number 
  > Summary: User must have valid US phone number to register
  > Pre-condition: User must be on registration page, User must have US phone number
  > Trigger: "Register" button must be clicked
  > Primary Sequence: 
      > User inputs their registration information
      > User clicks register
      > System will use phonenumbers python package to verify number
      > System will ensure number is valid 
      > System registers user and adds user to database
      > User is redirected to login page
  > Primary Post-Conditions: User is now verified and logged into the website
  > Alternative Sequence: 
      > User inputs their registration information
      > User inputs invalid number and clicks register
      > System searches for number 
      > System displays error message and prompts user to re-enter information

## The website will be able to send messages
  > Summary: User will be able to send messages to other users within a chat room
  > Pre-condition: User must be logged in and in a chatspace
  > Trigger: "Send" button must be clicked
  > Primary Sequence: 
     > User creates chatspace
     > User adds other users to chatspace
     > User types message
     > User clicks send button, and message is now viewable by all users in the chatspace
  > Primary post-conditions: User is able to view message in chatspace, and remains in chatspace unless exited
  > Alternative Sequence: 
     > User creates chatspace
     > Attempts to add invalid user
     > System displays error message "Invalid User. Make sure there are no typos!"
     > User adds valid user

## The website will be able to create/add/remove toDoList
> Summary: Users will be able to manage their TODO list by adding, reorganizing, and removing items
> Pre-condition: User has an account and has opened the TODO list
> Trigger: User clicks "manage TODO list" button
> Primary Sequence:
      > User can create Todo list blocks to drag onto a schedule
          > User clicks "create new task" button
          > User enters task name and length
      > User can move existing blocks around on the schedule
          > User holds and drags block to a new location
      > User can remove blocks from the schedule
          > User clicks a block and clicks remove
> Primary Post-Conditions: user has a todo list with many different tasks at different time blocks
> Alternative sequence:
      > User attempts to place a task in a time block that is already being used
      > user is prompted to place the task in a different non-overlapping time slot 

## The website will be able to search for email
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
      
## The website will be able to delete emails
> Summary: Users will be able to delete any emails they receive
  > Pre-condition: Users must be logged in and in the inbox
  > Trigger: Clicking the trash can icon
  > Primary Sequence: 
      > Website takes user to user's inbox
      > User selects email they would like to delete
      > User clicks trash icon on the right-hand side of the email pop-up
      > Email is deleted, system notifies user that email has been deleted, also shows "UNDO" action
  > Primary Post-Conditions: Email is now deleted, and user is still in the inbox
  > Alternative Sequence: 
      > User deletes email by accident
      > System notifies user of email deletion and also shows "UNDO" action
      > User clicks "UNDO"
      > Email is restored 
