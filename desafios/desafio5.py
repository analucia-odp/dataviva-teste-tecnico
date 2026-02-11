import csv

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

def main():
    # Read the CSV file and convert it to a list of dictionaries
    input = [] 
    with open('desafios/inputs/desafio5_input.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Convert the 'valor' field to an integer
            row['valor'] = int(row['valor'])
            input.append(row)
    print(data_clustering_by_category(input))

main()