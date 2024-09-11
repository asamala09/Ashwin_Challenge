import re

def validate_credit_card(number):
    pattern = r'^[4-6]\d{3}(-?\d{4}){3}$'

    # strip() removes any leading/trailing spaces
    match = re.match(pattern, number.strip())  
    
    if match:
        # Check for consecutive repeated digits
        matched_number = number.replace('-', '')
        if re.search(r'(\d)\1{3,}', matched_number):
            return "Invalid"
        return  "Valid"
    else:
        return "Invalid"





with open(filename) as file:
    i = 0 
    for line in file:
        current_line = line.rstrip()
        if i == 0:
            # Convert the first line to an integer
            number = int(current_line)  
                # Check if the number is between 0 and 100
                if number > 0 and number < 100:  
                    i += 1  # Skip to the next line
                    continue
        print(validate_credit_card(current_line))
        i += 1
    