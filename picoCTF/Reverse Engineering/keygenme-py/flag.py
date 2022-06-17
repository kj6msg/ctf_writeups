import hashlib

username_trial = b"PRITCHARD"
indices = [4, 5, 3, 6, 2, 7, 1, 8]

enc = "".join(hashlib.sha256(username_trial).hexdigest()[i] for i in indices)

print("picoCTF{1n_7h3_|<3y_of_" + enc + "}")
