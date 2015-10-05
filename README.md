# Validate Mails from a csv

This script use https://github.com/mailgun/flanker to verify mails.

## USAGE
```bash
python validate_email.py example.csv
```

### Input
```csv
email,name
jeanmatheussouto@gmail.com,Jean Matheus
@invalid.com, Invalid
asdasd@asfasd.asc, asdas
```

### Output
```
Validate Emails
--------------------
Invalid: True - Mail: @invalid.com
Invalid: True - Mail: asdasd@asfasd.asc
--------------------
Mail Count:  3
Invalid Mail Count:  2
Percentage of mails invalid: 66.7%
```
