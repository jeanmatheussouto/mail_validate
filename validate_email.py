import csv
import sys
from flanker.addresslib import address

print "Validate Emails"
print "--------------------"

f = open(sys.argv[1], 'rb')

mailCount = 0
invalidMails = []
try:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        mailCount += 1
        mailValid = address.validate_address(row['email'])
        if mailValid is None:
            invalidMails.append(row['email'])
            print "Invalid: {0} - Mail: {1}".format(mailValid is None, row['email'])

    print "--------------------"
    print "Mail Count: ", mailCount
    print "Invalid Mail Count: ", len(invalidMails)

    print "Percentage of mails invalid: {:.1%}".format(float(len(invalidMails)) / float(mailCount))
finally:
    f.close()
