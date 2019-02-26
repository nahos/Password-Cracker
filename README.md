# Password-Cracker

Password cracker is a python 2.7 based program to decode a SHA-1 hash.Given an input hash,the program returns the password corresponding to the hash.

## Installation
Please install python 2.7 from the python [website](https://www.python.org/downloads/)

Please use the package manager -[PIP] to install the following packages:

- Hashlib
- Time
- Sys
- Multiprocessing

EX: pip install hashlib

If you dont have pip, please refer to the below [site](https://pip.pypa.io/en/stable/installing/) to install it.

PS:Make sure to add the path to python in the sytem variable.

## Usage
The breaker.py program uses brute force method find a password.The program takes 3 or 4 (depends on the type of input hash) command line arguments,and they are- (1)The absolute path to the list of commonly used password, (2)The input hash,(3)The third input tells weather the input hash is a normal hash(N) salted hash(S) or a spaced hash(G) i.e the password is 2 words separated by space.(4)If the 3 argument is S i.e if its a  salted hash, please provide the hash of the salt as 4 argument.

"""
[path_to_python] breaker.py <path to Common_PWD.txt> <input hash> <type of hash either N, S or G> <if input is salted hash, enter hash of salt>
"""
EX:
(A)
```
D:\Python2.7>D:\College\Spring_2019\Blockchain\HW_2\sha1_breaker.py\breaker.py D:\College\Spring_2019\Blockchain\HW_2\sha1_breaker.py\Common_PWD.txt b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 N
Password cracked!
The password was found in 15 attempts
The password is letmein

Total time taken is 0.085000038147
```
(B)
```
D:\Python2.7>D:\College\Spring_2019\Blockchain\HW_2\sha1_breaker.py\breaker.py D:\College\Spring_2019\Blockchain\HW_2\sha1_breaker.py\Common_PWD.txt 801cdea58224c921c21fd2b183ff28ffa910ce31 N
Password cracked!
The password was found in 999967 attempts
The password is vjhtrhsvdctcegth

Total time taken is 1.52799987793
```

(C)
```
D:\Python2.7>D:\College\Spring_2019\Blockchain\HW_2\sha1_breaker.py\breaker.py D:\College\Spring_2019\Blockchain\HW_2\sha1_breaker.py\Common_PWD.txt ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 S f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
Password cracked!
The password was found in 546154 attempts
The password is slayerharib

Total time taken is 0.97100019455
```

The fast_breaker.py program finds the password faster.The program takes 3 or 4 (depends on the type of input hash) command line arguments,and they are- (1)The absolute path to the list of commonly used password, (2)The input hash,(3)The third input tells weather the input hash is a normal hash(N) salted hash(S) or a spaced hash(G) i.e the password is 2 words separated by space.(4)If the 3 argument is S i.e if its a  salted hash, please provide the hash of the salt as 4 argument.
```
[path_to_python] fast_breaker.py <path to Common_PWD.txt> <input hash> <type of hash either N, S or G> <if input is salted hash, enter hash of salt>
```



