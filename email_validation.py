from re import split

def fun(s):
    def correct_username(u):
        if not u:
            return False
        for x in u:
            if not (x.isalnum() or x == '-' or x == '_'):
                return False
        return True

    def correct_web(w):
        return w.isalnum()

    def correct_ext(e):
        return e.isalpha() and len(e) <= 3

    email_details = split(r'[@.]', s)
    if len(email_details) != 3:
        return False
    username, web, extension = email_details
    correct = (correct_username(username), correct_web(web), correct_ext(extension))
    if all(correct):
        return True

    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)