                            # 0 1 2 3 4 5 6 7 8 9 10 11 12 13  -> index
word = "photosynthesis"     # p h o t o s y n t h  e  s  i  s

#OBS: always stops at the previous index(number)


print(word[2:7]) #Result: otosy    ->   #strts from 2 and ends before 7

print(word[:5])   #Result: photo    ->   #ends before 5

print(word[:])   #Result: photosynthesis  ->   #print whole string

print(word[::3])  #Result: ptyhi    ->    #print 0 and multiple of 3 afterwards

print(word[3::3])  #Result: tyhi    ->    #print 3 and multiple of 3 afterwards

print(word[:-1])   #Result: photosynthesi    ->   #ends before -1

print(word[:-7])   #Result: photosy     ->     #ends before -7

print(word[::-1])  #Result: sisehtnysotohp    ->  #print string in reverse

print(word[5::-1])  #Result: sotohp    ->   #print reverse till 5

# Using slicing with reverse and specific stop:
print(word[8:3:-1])  # Result: tonyt -> Starts from 8 and goes to index 3 (exclusive) in reverse

# Entire string in reverse:
print(word[::-1])  # Result: sisehtnysotohp -> Reverses the whole string

# Reverse from a specific index:
print(word[7::-1])  # Result: ynotohp -> Starts from index 7 and reverses to the beginning

# Reverse from a specific index to a specific index:
print(word[10:4:-1])  # Result: ehtony -> Starts at index 10 and reverses to index 5 (exclusive)

# Extract with a step:
print(word[1:12:2])  # Result: htsyhs -> From index 1 to index 12 (exclusive) with step of 2

# Negative indices with slicing:
print(word[-1:-6:-1])  # Result: siseh -> Starts at the last character and goes back 5 characters

# Reverse specific part:
print(word[6:0:-1])  # Result: ysohto -> Starts at index 6 and reverses to index 1 (exclusive)