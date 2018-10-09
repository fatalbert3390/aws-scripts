
# 's' is the string you're trying to parse. 
# 'first' is the beginning character
# 'last' is the end character


test_str = "u'Id': '/hostedzone/[ZJ########]',"

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

print find_between(test_str, "e/", "',")


