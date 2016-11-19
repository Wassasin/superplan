import requests
# import utils

def send_email(userID, recipient, subject, message):
    print "Sending email..."

    return requests.post(
        "https://api.mailgun.net/v3/sandboxc712727e1e4f4886b8d9a9f3b85779c3.mailgun.org/messages",
        auth=("api", "key-7a242797d3698be83bb75fb50fed172e"),
        data={"from": userID + "<notifications@postpone.io>",
              "to": recipient,
              "subject": subject,
              "text": message})

# request = send_email()
# print request.status_code
