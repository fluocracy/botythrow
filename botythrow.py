
#OPTIONS

import random
psiteswap = ["423", "441", "504", "522", "531", "603", "612", "630", "711", "720", "801", "900", "333", "333", "333"]
pthrow = ["behind the neck", "under a leg", "behind the back", "under the arm", "over the head", "in the usual fashion", "with a smile", "under a leg onto a foot", "onto a foot", "behind the back onto a foot", ]
pcatch = ["behind the neck", "under the leg", "behind the back", "under the arm", "with a penguin catch", "in the usual fashion", "with a smile"]
sequence0 = [" is empty."]
sequence1 = [" is zapped."]
sequence2 = [" is held."]
siteswap = random.choice(psiteswap)
siteswap1 = siteswap[0]
siteswap2 = siteswap[1]
siteswap3 = siteswap[2]
print("The siteswap is " + siteswap + ".")

def generatesequence(siteswap1, fsiteswap1):
    throw = random.choice(pthrow)
    catch = random.choice(pcatch)
    if siteswap1 == "0":
        sequence = random.choice(sequence0)
    elif siteswap1 == "1":
        sequence = random.choice(sequence1)
    elif siteswap1 == "2":
        sequence = random.choice(sequence2)
    else:
        sequence = " is thrown " + throw + " and caught " + catch + "."
    print("The " + fsiteswap1 + sequence)
fsiteswap1 = siteswap1
generatesequence(siteswap1, fsiteswap1)
if siteswap2 == siteswap1:
    fsiteswap2 = "next " + siteswap2
else:
    fsiteswap2 = siteswap2

generatesequence(siteswap2, fsiteswap2)
if siteswap3 == siteswap2:
    fsiteswap3 = "other " + siteswap3
if siteswap == "333":
    fsiteswap3 = "final 3"
else:
    fsiteswap3 = siteswap3
generatesequence(siteswap3, fsiteswap3)
