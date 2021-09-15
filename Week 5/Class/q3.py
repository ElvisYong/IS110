def is_valid_username(username):
      if (not username) or username.isspace() or len(username) > 8:
          return False

      digit_special = False
      for i, char in enumerate(username):
          if char.isupper():
              return False
          if not char.isalnum() and not char in '_.!#$%?':
            return False
      return True

username_list = ['ab{cdefgh','abcdefghi','ab$cd','ab_cd','ab-cd','ab:cd','','ab cd','abcDef','abc8ef']
for username in username_list:
    print("The username '" + username +"' is valid : " + str(is_valid_username(username)))
