import hashlib
import time
import sys

pwd_file = sys.argv[1]
inp = sys.argv[2]
type = sys.argv[3]
no_of_input = len(sys.argv)
if (no_of_input >4):
    salt = sys.argv[4]

def sha1_hash(pwd):
    pwd = pwd.replace("\n", "")
    sha1 = hashlib.sha1()
    sha1.update(pwd)
    digest = sha1.hexdigest()
    return digest

def decode(inp, pwds,salt = ''):
    i = 0
    for pwd in pwds:
        digest = sha1_hash(salt+pwd)
        if digest == inp:
            return i
            break
        i = i+1
    return -1


if __name__ == '__main__':
    start_time = time.time()
    fp = open(pwd_file, "r")
    lines = fp.readlines()
    fp.close()

    if type == 'N':
        attempts = decode(inp,lines)
    elif type == 'S':
        salt_w = lines[decode(salt,lines)]
        attempts = decode(inp, lines,salt_w)
    elif type == 'G':
        attempts = 0
        for line in lines:
            for pwd in lines:
                p = line + " " + pwd
                digest = sha1_hash(p)
                if digest == inp:
                    print("Password cracked!")
                    print("The password was found in " + str(attempts) + " attempts")
                    print("The password is " + p)
                    end_time = time.time()
                    total_time = end_time - start_time
                    print("Total time taken is " + str(total_time))
                    exit(0)

                attempts = attempts+1

    end_time = time.time()
    if attempts == -1:
           print("Password could not be found")
    else:
           print("Password cracked!")
           print("The password was found in " + str(attempts) + " attempts")
           if(type != "S"):
                print("The password is " + lines[attempts])
           else:
               print("The password is " + salt_w.replace("\n","")+lines[attempts])


    total_time = end_time - start_time
    print("Total time taken is " + str(total_time))
