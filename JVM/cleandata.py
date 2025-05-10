import re
raw_data=[{
    "name":"anand dwivedi","email":"dwivediaaanand@gmail.com","phone":"(123)456-789"},
    {"name":"kamlesh gaikwad","email":"kamleshGAIKWAD@GMAIL.com","phone":"123.456.789"},
    {"name":"pRERANA RaTHod","email":"prerana_rathod@gmail.com","phone":"+1 23 456 789"}
    ]
def clean_data(customer):
    name=customer['name'].title()
    email=customer['email'].strip().lower()
    phone=re.sub(r'\D','',customer['phone'])
    if phone.startswith('1') and len(phone)==11:
        phone=phone[1:]
    return {"name":name,"email":email,"phone":phone}
result=[clean_data(cust) for cust in raw_data]
for customer in result:
    print(customer)