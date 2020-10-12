from utils.app import News
import enquiries

categories = ['Coronavirus', 'Politics', 'Economy',
              'Society', 'Sports', 'Opinion', 'Lifestyle']
choice = enquiries.choose('Choose a category: ', categories)
recipient = enquiries.freetext('Emails (Use comma to separate emails): ')
emails = recipient.split(',')
if choice == 'Coronavirus':
    News(choice).send_mail(emails)
elif choice == 'Politics':
    News(choice).send_mail(emails)
elif choice == 'Economy':
    News(choice).send_mail(emails)
elif choice == 'Society':
    News(choice).send_mail(emails)
elif choice == 'Sports':
    News(choice).send_mail(emails)
elif choice == 'Opinion':
    News(choice).send_mail(emails)
elif choice == 'Lifestyle':
    News(choice).send_mail(emails)
