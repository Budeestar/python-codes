import yagmail

sender_email =["nithin.yadav0010@gmail.com"]
receiver_email =["snithinviswakarma0010@gmail.com"]
subject = "Check THIS out"
sender_password = input(f'Please, enter the password for {sender_email}:\n')

yag = yagmail.SMTP(user="nithin.yadav0010@gmail.com", password=sender_password)

contents = [
  "This is the first paragraph in our email",
  "As you can see, we can send a list of strings,",
  "being this our third one",
]

yag.send(receiver_email, subject, contents)