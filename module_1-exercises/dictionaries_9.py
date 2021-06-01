# Gets a list of dictionaries
# Returns a dictionary with all the keys in the previous one
# -> If a key is repeated in more than one dictionary, values for that key are stored in a list

dic_list = [
    {
        "name": "alvaro",
        "f_surname": "martinez",
        "l_surname": "quiroga",
        "legal_terms_ok": True
    },
    {
        "name": "juan",
        "f_surname": "martinez",
        "l_surname": "sanchez",
        "legal_terms_ok": False,
        "account_expired": True
    },
    {
        "name": "nuria"
    }
]

# print(dic_list)

new_dict = dict()

for value in dic_list:
    # print(value)
    new_dict.update(value)

print(new_dict)
