# # import requests
# #
# # url = "https://api.npoint.io/c790b4d5cab58020d391"
# # response = requests.get(url=url).json()
# # print(response)
# import smtplib
#
# my_email = "missbellumspython@gmail.com"
# password = "imfdmiuxqrsmondr"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(my_email, password)
#     connection.sendmail(my_email, my_email, "hello gyal")
#     connection.close()
#     print("sent gyal")
from flask import request


