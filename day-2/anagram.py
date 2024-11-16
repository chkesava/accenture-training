def is_anagram_or_not(string_1,string_2):
    string_1_freq={}
    string_2_freq={}
    if len(string_1)!=len(string_2):
        return False
    for i in range(len(string_1)):
        if string_1[i] not in string_1_freq:
            string_1_freq[string_1[i]]=1
        else:
            string_1_freq[string_1[i]]+=1
        if string_2[i] not in string_2_freq:
            string_2_freq[string_2[i]]=1
        else:
            string_2_freq[string_2[i]]+=1
    return string_1_freq==string_2_freq

string_1=input()
string_2=input()
print(is_anagram_or_not(string_1,string_2))
