import json
import urllib.parse

splitwise_categories_path = 'jsons/splitwise_categories.json'

# Category ID Mapping Function 
def category_id_switch(import_category):

    # Define mapping of import categories to : Mint Category IDs
    with open(splitwise_categories_path, "r") as read_content:
        switcher = json.load(read_content)
    
    # Get the mint category ID from the map 
    return switcher.get(import_category,20) # For all other unmapped cases return uncategorized category "20"

def get_category(type_id, category_name):
    
    category_id = ''
    # typeID payment overrides all categories 
    if type_id == "Payment":
        category_id = '2101' # Since I was importing credit cards I have mine set to credit card payment. If you are doing bank accounts you many want to change this to payment general

    # if type is NOT payment then do a category check 
    else:
        # if there IS no category name it is uncategorized 
        if len(category_name) == 0: 
            category_id = '20' # mint's uncategorized category

        # If there is a category check it against mapping	
        else : 
            # Use a switch since there may be MANY category maps 
            category_id = category_id_switch(category_name)


    # Set mint category name by looking up name in ID map     
    category_name = urllib.parse.quote(category_name)
    return (category_id, category_name)   


