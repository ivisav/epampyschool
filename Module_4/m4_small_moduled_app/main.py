#   let's crate an app that will create email for us

import greetings.greet_formal as f_head
import body.body_all
from signature.sig_formal import signature_form as signature


def letter(to_name, from_name):
    mail_head = f_head.formal_greetings(to_name)
    mail_body = body.body_all.body_formal(to_name=to_name, meeting='coffee break')
    mail_sig = signature(from_name)

    mail = f"{mail_head}\n{mail_body}\n\n{mail_sig}"
    return mail


print(letter('Mike', 'Bob'))
