alf= ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
      'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
      'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
      'э', 'ю', 'я']
book1=open(r"C:\Users\User\Downloads\Chekhov_Sochineniya.txt",
           encoding='utf-8').read().lower()
book2=open(r"C:\Users\User\Downloads\Dostoevsky_Povesti_i_rasskazy.txt",
           encoding='utf-8').read().lower()
book_eps=open(r"C:\Users\User\Downloads\Dostoevsky_Prestuplenie_i_nakazanie_Idiot.txt",
                encoding='utf-8').read().lower()
pairs1=[[x+y,0] for x in alf for y in alf]
pairs2=[[x+y,0] for x in alf for y in alf]
pairs3=[[x+y,0] for x in alf for y in alf]

idx = {p[0]: k for k, p in enumerate(pairs1)}
def find_pair(x, pairs):
    j = idx.get(x)
    if j is not None:
        pairs[j][1] += 1
for i in range(len(book1)):
    find_pair(book1[i:i+2], pairs1)
for i in range(len(book2)):
    find_pair(book2[i:i+2], pairs2)
for i in range(len(book_eps)):
    find_pair(book_eps[i:i+2], pairs3)
for x in range(len(pairs1)):
    pairs1[x][1]=pairs1[x][1]/(len(book1)-1)
    pairs2[x][1]=pairs2[x][1]/(len(book2)-1)
    pairs3[x][1]=pairs3[x][1]/(len(book_eps)-1)
d_d1 = sum(abs(pairs2[x][1] - pairs3[x][1]) for x in range(len(pairs1)))
d_ch1=sum(abs(pairs1[x][1] - pairs2[x][1]) for x in range(len(pairs2)))
print(d_d1, d_ch1)
print(d_ch1/d_d1)