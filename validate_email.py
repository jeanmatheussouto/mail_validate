import csv
import sys
from flanker.addresslib import address

print "Validate Emails"
print "--------------------"

f = open(sys.argv[1], 'rU')

mails = []
invalidMails = []
try:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        mails.append(row['email'])

    print "Validando emails"

    result = address.validate_list(mails, as_tuple=True)

    print "--------------------"
    print "Mail Count: ", len(mails)
    print "Invalid Mail Count: ", len(result[1])
    print "--------------------"

    print "Percentage of mails invalid: {:.1%}".format(float(len(result[1])) / float(len(mails)))
finally:
    f.close()
