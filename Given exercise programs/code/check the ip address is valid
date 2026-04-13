def isValidIP(s):
    if s.count('.') != 3:
        return 'Invalid Ip address'
    l = list(map(str, s.split('.')))
    for ele in l:
        if int(ele) < 0 or int(ele) > 255 or (ele[0]=='0' and len(ele)!=1):
            return 'Invalid Ip address'
    return 'Valid Ip address'
ipaddress=input("enter the ip address:")
print(isValidIP(ipaddress))
