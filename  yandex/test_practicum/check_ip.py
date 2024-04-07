IPV4 = "IPv4"
IPV6 = "IPv6"
ERROR = "Error"


# return IPV4, IPV6 or ERROR constant
def check_ip_address(ip_to_check: str) -> str:
    octets = ip_to_check.split('.')
    if len(octets) == 4:
        return check_ip_v4(octets)

    octets = ip_to_check.split(':')
    if len(octets) == 8:
        return check_ip_v6(octets)
    return ERROR


def check_ip_v4(octets):
    for octet in octets:
        if not octet.isdigit():
            return ERROR
        num = int(octet)
        if str(num) != octet or int(octet) not in range(0, 256):
            return ERROR
    return IPV4


def check_ip_v6(octets):
    for octet in octets:
        if not is_hexadecimal(octet) or len(octet) > 4:
            return ERROR
    return IPV6


def is_hexadecimal(num_str):
    try:
        int(num_str, 16)
        return True
    except ValueError:
        return False


ip_to_check = input()
print(check_ip_address(ip_to_check))

# print(check_ip_address('0.0.0.0'))
# print(check_ip_address('255.255.255.055'))
# print(check_ip_address('255.255.255.55'))
