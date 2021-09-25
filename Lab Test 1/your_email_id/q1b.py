# Name: Yong Yu En, Elvis
# Email ID: elvis.yong.2021

def is_official_language(country, language):
    # Replace the code below with your implementation.
    if country == 'Belgium' and (language == 'Dutch' or language == 'French' or language == 'German'):
        return True
    elif country == 'Canada' and (language == 'English' or language == 'French'):
        return True
    elif country == 'Philippines' and (language == 'English' or language == 'Filipino'):
        return True
    elif country == 'Singapore' and (language == 'Chinese' or language == 'English' or language == 'Malay' or language == 'Tamil'):
        return True
    return False