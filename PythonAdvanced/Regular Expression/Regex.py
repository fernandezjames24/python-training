import re


def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")

#the following pattern accepts a format e.g zxc@email.com       
pattern = r"(^[a-zA-Z0-9_{}.`?-]+@[a-zA-Z0-9]+.[a-z{2}]+$)" 
test_email(pattern)
