'''In this lab we will create a program that can encrypt and decrypt strings using a simple algorithm.
The algorithm we will use is the following:
* To encrypt a string, we reverse it and add 1 to the ASCII code for each character. For example, if we take the word:
python
When we encrypt the word it becomes:
opiuzq
Notice that the p in python has become q in the encrypted string and we have switched the order.

To decrypt a string we do the opposite. We reverse the order again, but this time subtracting 1 from the ASCII code for each character in the string.

Your output should look something like:

Enter plaintext: some random text

Encrypting some random text
s -> t
o -> p
m -> n
e -> f
-> !
r -> s
a -> b
n -> o
d -> e
o -> p
m -> n
-> !
t -> u
e -> f
x -> y
t -> u

Encrypted string is uyfu!npeobs!fnpt

Enter cyphertext: uyfu!npeobs!fnpt

Decrypting uyfu!npeobs!fnpt
u -> t
y -> x
f -> e
u -> t
! ->
n -> m
p -> o
e -> d
o -> n
b -> a
s -> r
! ->
f -> e
n -> m
p -> o
t -> s

Decrypted string is some random text

Here are some encrypted strings for you to decrypt:


/ztbF!tj!hojnnbshpsq!/hojnnbshpsq!fwpM!J
/sfuvqnpd!b!op!ovs!pu!tofqqbi!utvk!ubiu!hojwmpt.nfmcpsq!op!zbttf!ob!tj!nbshpsq!B
ubfsh!tj!opiuzQ
fujsx!pu!fwbi!uoeje!vpz!fojm!fiu!tj!fupsx!sfwf!vpz!fepd!gp!fojm!utfc!fiU'''

import math


def encrypt_decrypt(text, opt): #Create a function that get text and the option (Encrypt or Decrypt)
    new_text = ""
    for char in text[::-1]:
        if opt == 1:
            temp = ord(char) + 1
            new_text += chr(temp)
        elif opt == 2:
            temp = ord(char) - 1
            new_text += chr(temp)
    if opt == 1:
        print("The text encrypted is", new_text)
    elif opt == 2:
        print("The text decrypted is", new_text)
    return new_text

optionStr = ""
text = ''
temp = ''

while optionStr != "0":
    print("Secret Sentence - Encrypt/Decrypt a Text")
    print("----------------------------------------")
    print("Choose an option:")
    print("Press 1 to Encrypt a text")
    print("Press 2 to Decrypt a text")

    optionStr = input("Please choose: ")

    if optionStr == "1":
        text = str(input("Please insert a text to encrypt: "))
        encrypt_decrypt(text, 1)
    elif optionStr == "2":
        text = str(input("Please insert a text to decrypt: "))
        encrypt_decrypt(text, 2)
    break
