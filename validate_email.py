import csv
import sys
from flanker.addresslib import address

print "Validate Emails"
print "--------------------"

f = open(sys.argv[1], 'rU')

total = 0
valid = 0
invalid = 0
try:
    print "Validando emails"
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        total += 1
        email = row['email']
        if address.validate_address(email):
            valid += 1
        else:
            invalid += 1

    print "--------------------"
    print "Mail Count: ", total
    print "Invalid Mail Count: ", invalid
    print "--------------------"

    print "Percentage of mails invalid: {:.1%}".format(float(invalid) /
                                                       float(total))
finally:
    f.close()
