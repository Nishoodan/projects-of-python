file_path = r"C:\Users\NISHOODAN\OneDrive\Documents\projects\python\intermidiate\nis.txt"
dict_count = {}
file = open(file_path,'r')
for i in file:
    words = i.lower().split()
    for j in words:
        j = j.strip(',./?><""')
        dict_count[j] = dict_count.get(j,0)+1
for j, k in dict_count.items():
    print(j,':',k)
