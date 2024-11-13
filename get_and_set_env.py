def returnAPiKey():
    # Open the .env file in read mode
    with open('.env', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into key and value by the first '=' character
            key, value = line.strip().split('=', 1)
            # Check if the key is 'API_KEY'
            if key.strip() == 'API_KEY':
                # Return the value, stripping any surrounding quotes and whitespace
                return value.strip().strip('"').strip("'")
    # Return None if 'API_KEY' is not found
    return None

def returnLanguageKey():
    # Open the .env file in read mode
    with open('.env', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into key and value by the first '=' character
            key, value = line.strip().split('=', 1)
            # Check if the key is 'LANGUAGE'
            if key.strip() == 'LANGUAGE':
                # Return the value, stripping any surrounding quotes and whitespace
                return value.strip().strip('"').strip("'")
    # Return None if 'API_KEY' is not found
    return None

def updateLanguageKey(new_value):
    # Initialize an empty list to store the lines of the file
    lines = []
    # Open the .env file in read mode
    with open('.env', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the line starts with 'LANGUAGE ='
            if line.startswith('LANGUAGE ='):
                # If it does, append the updated LANGUAGE line with the new value
                lines.append(f'LANGUAGE = "{new_value}"\n')
            else:
                # Otherwise, append the original line
                lines.append(line)
    # Open the .env file in write mode
    with open('.env', 'w') as file:
        # Write all the lines back to the file
        file.writelines(lines)

def returnTopicKey():
    # Open the .env file in read mode
    with open('.env', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into key and value by the first '=' character
            key, value = line.strip().split('=', 1)
            # Check if the key is 'TOPIC'
            if key.strip() == 'TOPIC':
                # Return the value, stripping any surrounding quotes and whitespace
                return value.strip().strip('"').strip("'")
    # Return None if 'TOPIC' is not found
    return None

def updateTopicKey(new_value):
    # Initialize an empty list to store the lines of the file
    lines = []
    # Open the .env file in read mode
    with open('.env', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the line starts with 'LANGUAGE ='
            if line.startswith('TOPIC ='):
                # If it does, append the updated LANGUAGE line with the new value
                lines.append(f'TOPIC = "{new_value}"\n')
            else:
                # Otherwise, append the original line
                lines.append(line)
    # Open the .env file in write mode
    with open('.env', 'w') as file:
        # Write all the lines back to the file
        file.writelines(lines)
