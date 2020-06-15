# Email-Automation
Bulk email sender using python 3


We are using pandas library and SMTPlib to automate the process of sending bulk emails.

Steps to run the program
  1.Create an env
  2.pip install pandas
  3. Replace the text Email_User - with your email id and Email_password with your password
  
  Note: I have stored the password as environment variables, which is a better practice.
  
  4.Place an excel sheet and any attachments in the same folder as the python script.Change the name of the file in line 45 
  5.Run from the terminal 
  
  Note: This script is for gmail extensions check out more on python.org about smtp libraries and the port numbers.
  
  
SMTP library gives us an easy option to send emails in an organized way. It has all the functions to add attachments,     organize the subject and to include HTML in the email.

Pandas is used here to read the excel sheet of email ids and personalize email for each.

The excelsheet need not have headings, it can consist names in the first column and email in the secons
  
  
