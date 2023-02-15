import requests
import hashlib # to use the hash function
import sys
def req_data(q_char):
    url = 'https://api.pwnedpasswords.com/range/'+ q_char
    response = requests.get(url)
    if response.status_code!=200:
        raise RuntimeError(f'error getting {response.status_code}, check for the proper api')
    return response

def pass_check(res,tail):
     hashh = (line.split(':') for line in res.text.splitlines()) # splits the actual tail and the count that is hacked 
     for h, c in hashh: # to loop through the hashes h for tail and c for count
        if h==tail:
            return c
     return 0




def pawn_pass(password):
    hashpass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # using the hexdigest to convert the object created by using encode to code and upper to convert inot upper case
    fiv, tail = hashpass[:5] , hashpass[5:]
    response = req_data(fiv)
    res = pass_check(response,tail)

    return res

def main(args):
   for passs in args:
    hack = pawn_pass(passs)
    if passs:
        print(f'your password {passs} was found {hack} times please change it')
    else:
        print(f'Yaay your password {passs} is not hacked')
    return 'exited'
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

