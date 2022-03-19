import random

def generate_conjunction(siteswap, i):
    if i == 1 and siteswap[0] == siteswap[1]:
        return "next "
    elif i == 2 and siteswap[0] == siteswap[1]:
        return "other "
    elif i == 2 and siteswap == "333":
        return "final "
    else:
        return ""

def generate_sequence(siteswap):
    for i, swap in enumerate(siteswap):
        if swap == "0":
            sequence = random.choice(sequence0)
        elif swap == "1":
            sequence = random.choice(sequence1)
        elif swap == "2":
            sequence = random.choice(sequence2)
        else:
            sequence = " is thrown " + random.choice(throws_array) + " and caught " + random.choice(catches_array) + "."
        conjunjcion = generate_conjunction(siteswap, i)
        print("The " + conjunjcion + swap + sequence)

siteswaps_array = ["423", "441", "504", "522", "531", "603", "612", "630", "711", "720", "801", "900", "333", "333", "333"]
throws_array = ["behind the neck", "under a leg", "behind the back", "under the arm", "over the head", "in the usual fashion", "with a smile", "under a leg onto a foot", "onto a foot", "behind the back onto a foot", ]
catches_array = ["behind the neck", "under the leg", "behind the back", "under the arm", "with a penguin catch", "in the usual fashion", "with a smile"]
sequence0 = [" is empty."]
sequence1 = [" is zapped."]
sequence2 = [" is held."]
siteswap = random.choice(siteswaps_array)
print("The siteswap is " + siteswap + ".")

generate_sequence(siteswap)
