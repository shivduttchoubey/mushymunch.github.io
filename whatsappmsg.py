# i want to send a message over whatsapp and want to automate the process 

# write a python code where you ask for phone and name .

# insert the name in a template and send the message

# write a python code for the same

import pywhatkit

def send_whatsapp_message(phone_number, name, message):
  """Sends a WhatsApp message to the specified phone number.

  Args:
    phone_number: The phone number of the recipient.
    name: The name of the recipient.
    message: The message to be sent.
  """

  template = "Hi {name}, how are you? This is a message from Python."
  message = template.format(name=name)
  pywhatkit.sendwhatmsg(phone_number, message)

if __name__ == "__main__":
  phone_number = input("Enter the phone number: ")
  name = input("Enter the name: ")
#   message = input("Enter the message: ")
  send_whatsapp_message(phone_number, name, message,)
