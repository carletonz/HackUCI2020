# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from drive import drive

app = Flask(__name__)
d = drive()

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    
    resp = MessagingResponse()
    
    cmd = request.form['Body']
    print(cmd)
    cmd = cmd.split()
    
    if cmd[0] == 'S':
        d.forward(0)
        resp.message("Command Received: Stopped")
    elif cmd[0] == 'F':
        try:
            speed = float(cmd[1])
            d.forward(speed)
            resp.message("Command Received: Forward")
        except:
            d.forward(0)
            resp.message("Invalid number")
    elif cmd[0] == 'T':
        try:
            speed = float(cmd[1])
            d.turn(speed)
            resp.message("Command Received: Turn")
        except:
            d.forward(0)
            resp.message("Invalid number")
    else:
        d.forward(0)
        resp.message("Invalid command")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
