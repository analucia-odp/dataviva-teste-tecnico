input = [
  { "categoria": "Alimentação", "valor": 10 },
  { "categoria": "Transporte", "valor": 5 },
  { "categoria": "Alimentação", "valor": 20 },
  { "categoria": "Lazer", "valor": 50 }
]

def data_clustering_by_category(input_list):
    """ This function takes a list of dictionaries, 
    where each dictionary contains a 'categoria' and a 'valor'.
    It returns a new dictionary where the keys are the 
    unique categories and the values are the total"""
    
    category_totals = {}
    
    for item in input_list:
        category = item["categoria"]
        value = item["valor"]
        
        # Check if the category already exists in the totals dictionary
        if category in category_totals:
            category_totals[category] += value
        # If the category does not exist, initialize it with the current value
        else:
            category_totals[category] = value
            
    return category_totals

print(data_clustering_by_category(input))