def extract_email_id(id):
    """
    Extracts the email id from the id
    """
    if '@' in id:
        return id.split('@')[0]
    return ''

# print(extract_email_id("jerry.lee@sis.smu.edu.sg"))
# print(extract_email_id("alan_wong.com"))
# print(extract_email_id(""))
# print(extract_email_id("alan_wong@gmail.com"))
# print(extract_email_id('alan_wong.com'))

def extract_multiple_email_ids(emails):
    if ';' in emails:
      split_emails = emails.split(';')
      for i in split_emails:
          print(extract_email_id(i))
    else:
        print(extract_email_id(emails))

extract_multiple_email_ids("jerry.lee@sis.smu.edu.sg;alan_wong@gmail.com;george_tan@yahoo.com")
extract_multiple_email_ids("")
extract_multiple_email_ids("jerry.lee@sis.smu.edu.sg")