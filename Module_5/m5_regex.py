import re

emails = [
'bob_sponge@ocean.net',
'test_user@gmail.com',
'emhyr_var_emreis@nilfgaardian.emp',
'59874~!35@0464.test']


# Check if email is valid
for email in emails:
    wrong_em = re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', email)
    if wrong_em is None:
        print(email)
