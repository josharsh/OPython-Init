                            # 0 1 2 3 4 5 6 7 8 9 10 11 12 13  -> index
word = "photosynthesis"     # p h o t o s y n t h  e  s  i  s

#OBS: always stops at the previous index(number)


print(word[2:7]) -> #Result: otosy    ->   #strts from 2 and ends before 7

print(word[:5])  -> #Result: photo    ->   #ends before 5

print(word[:])   -> #Result: photosynthesis  ->   #print whole string

print(word[::3]) -> #Result: ptyhi    ->    #print 0 and multiple of 3 afterwards

print(word[3::3]) -> #Result: tyhi    ->    #print 3 and multiple of 3 afterwards

print(word[:-1])  -> #Result: photosynthesi    ->   #ends before -1

print(word[:-7])  -> #Result: photosy     ->     #ends before -7

print(word[::-1]) -> #Result: sisehtnysotohp    ->  #print string in reverse

print(word[5::-1]) -> #Result: sotohp    ->   #print reverse till 5
