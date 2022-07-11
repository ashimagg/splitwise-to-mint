import json

payload_json_path = 'jsons/payload.json'
mint_categories_path = 'jsons/mint_categories.json'

def get_payload(date, description, category_id, category_name, amount):

    with open(mint_categories_path, "r") as read_content:
        mint_categories = json.load(read_content)

    mint_categories = {cat['name']:cat['id'] for cat in mint_categories['Category']}

    json_obj =  { "date": date,
        "description" : description,
        "category" : {
            "id" : category_id if category_id is not None else mint_categories.get(category_name),
            "name" : None
        },
        "accountId" : None,
        "amount" : amount,
        "parentId" : None,
        "type" : "CashAndCreditTransaction",
        "id" : None,
        "isExpense" : True,
        "isPending" : False,
        "isDuplicate" : False,
        "tagData" : {"tags":[{"id":"106197420_1406544"}]},
        "splitData" : None,
        "manualTransactionType" : "CASH",
        "checkNumber" : None,
        "isLinkedToRule" : False,
        "shouldPullFromAtmWithdrawals" : False    
    }

    return json.dumps(json_obj)