def convert_phone(phone):
    if phone==None:
        return phone
    elif len(phone)==10 and phone.startswith("07"):
        return "+254"+phone[1:]
    elif len(phone)==13 and phone.startswith("+254"):
        return phone[1:]
    elif len(phone)==12 and phone.startswith("254"):
        return phone
    elif len(phone)==9 and phone.startswith("7"):
        return "+254"+phone
    elif len(phone)==10 and phone.startswith("01"):
        return "+254"+phone[1:]
    else: 
        return phone
def human_readable_convert_phone(phone):
    if phone.startswith("+254"):
        return phone.replace("+254","0")
    if phone.startswith("254"):
        return "0"+phone[3:]
    return phone