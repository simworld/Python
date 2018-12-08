# ABC notation is a shorthand form of musical notation. In basic form it uses the letters A through G to represent the given notes, with other elements used to place added value on these - sharp, flat, the length of the note, key, ornamentation. Later, with computers becoming a major means of communication, others saw the possibilities of using this form of notation as an ASCII code that could facilitate the sharing of music online, also adding a new and simple language for software developers. In this later form it remains a language for notating music using the ASCII character set.
#
# Write a program to read the attached file and print the Id, title (one only), time and key signatures line by line.
#
#     Each tune consists of headers + notation. The headers start with a character followed by a : (colon)
#     The notation follows the headers.
#     Each tune begins with the X: - This is also the index field.
#     Titles begin with T:
#     A tune can have multiple titles, but we are only interested in the first one. If there are more, we just ignore the rest
#     The time signature is stored in the M: line
#     The key signature is stored in he K: line
#     You can ignore the notation, we are just interested in the headers
#
# Below is an example of the sort of output the program should produce:
#
# 195 ... Road to Lisdoonvarna, The ... Time sig: C| ... Key sig: D ...
# 196 ... Jenny's Wedding ... Time sig: C| ... Key sig: D ...
# 197 ... Dark Girl in Blue, The ... Time sig: C| ... Key sig: D ...
# 198 ... Knotted Cord, The ... Time sig: C| ... Key sig: Ador ...
# 199 ... Lucy's Tune ... Time sig: C| ... Key sig: Em ...
# 200 ... Banks of the Liffey, The ... Time sig: C| ... Key sig: G ...
# -------------------------------
# There are 100 tunes in the file
# -------------------------------

'''
X:101
T:Killavil Fancy, The
T:Eilish Brogan
T:Ten Pound Float, The
R:reel
D:Music at Matt Molloy's
D:Frankie Gavin & Alec Finn
Z:Sometimes played doubled.
Z:id:hn-reel-101
M:C|
K:G
~B3G A2BA|GE~E2 cEGE|DGBG A2BA|GEED EFGA|
~B3d A2BA|GE~E2 cEGE|DGBG A2BA|GEED ~E3D||
GABd edge|dB~B2 dBAB|GABd edge|dBAG EDB,D|
GABd edge|dB~B2 dega|(3bag ag egde|gedB AGEG||
"Variations:"
DGBG A2BA|GE~E2 cEGE|DGBG ~A3B|GEFD EGGA|
~B3d ~A3F|GE~E2 cEGE|DGBG ~A3B|GEED EGGD||
G2Bd efge|dBAB dBAB|G2Bd efge|dBAG EGGD|
G2Bd efge|dB~B2 dega|(3bag ag egde|gedB AGED||
'''

tune_count = 0
has_title = False

my_file = open("hnr1.abc", "r")

for line in my_file:
    if line[:2] == "X:":
        tune_count += 1
        has_title = False
        print()
        print(line[2:-1], "...", end=" ")
    elif line[:2] == "T":
        if not has_title:
            has_title = True
            print(line[2:1], "...", end=" ")
    elif line[:2] == "M:":
        print("Time sig:", line[2:-1], "...", end=' ')
    elif line[:2] == "K:":
        print("Key sig:", line[2:-1], "...", end=' ')

my_file.close()

print()
print("-" * 50)
print("There are", tune_count, "tunes in the file")
print("-" * 50)
