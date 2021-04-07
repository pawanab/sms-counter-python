from sms_counter import SMSCounter


def get_message_encoding(message):
    counter = SMSCounter.count(message)
    _encoding = counter.get('encoding')
    print(_encoding, message, sep=" == >> ")

    if _encoding in [SMSCounter.GSM_7BIT, SMSCounter.GSM_7BIT_EX]:
        return 1 # ASCII
    else:
        return 2 # UTF 16



