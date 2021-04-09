import requests

from annoy_scammers.generators import *


def annoy_scammer(url="https://reschedule-delivery-hermes.com/complete.php"):
    name = get_name()
    dob = get_dob()
    address = get_address()

    data = {
        'pcode': get_postcode(),
        'fname': name,
        'phone': get_phone_number(),
        'dob': dob,
        'address': address,
        'ccname': name,
        'ccnum': get_card_number(),
        'expiry': get_expiry_date(),
        'cvv': get_cvv(),
        'acct': get_account_number(),
        'sort': get_sort_code(),
    }

    r = requests.post(url, data=data)

    if r.ok:
        print(
            f"{name}, born {dob.replace(' ', '')}, living at {address}, just sent their personal details to the scammer!")
    else:
        print("Response not ok :(")
        print(r.text)
