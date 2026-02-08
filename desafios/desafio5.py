input = [
  { "categoria": "Alimentação", "valor": 10 },
  { "categoria": "Transporte", "valor": 5 },
  { "categoria": "Alimentação", "valor": 20 },
  { "categoria": "Lazer", "valor": 50 }
]

def data_clustering_by_category(input_list):
    category_totals = {}
    
    for item in input_list:
        category = item["categoria"]
        value = item["valor"]
        
        if category in category_totals:
            category_totals[category] += value
        else:
            category_totals[category] = value
            
    return category_totals

print(data_clustering_by_category(input))