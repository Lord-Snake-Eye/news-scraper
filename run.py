from utils.app import News
import enquiries

categories = ['Coronavirus', 'Politics', 'Economy',
              'Society', 'Sports', 'Lifestyle']
choice = enquiries.choose('Choose a category: ', categories)

use_file = enquiries.choose('Use file for emails?', ['yes', 'no'])

email_list = []

if use_file == 'yes':
    with open('emails.txt', 'r') as file:
        f = file.readlines()
        for email in f:
            email_list.append(email.strip())
else:
    recipient = enquiries.freetext('Emails (Use comma to separate emails): ')
    email_list.append(recipient.split(','))
    email_list = email_list[0]


if choice == 'Coronavirus':
    News(choice).send_mail(email_list)
elif choice == 'Politics':
    News(choice).send_mail(email_list)
elif choice == 'Economy':
    News(choice).send_mail(email_list)
elif choice == 'Society':
    News(choice).send_mail(email_list)
elif choice == 'Sports':
    News(choice).send_mail(email_list)
elif choice == 'Lifestyle':
    News(choice).send_mail(email_list)
