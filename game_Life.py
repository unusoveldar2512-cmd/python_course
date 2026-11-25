
book=open(r"C:\Users\User\Downloads\samyjj_bogatyjj_chelovek_v_vavilone.u.txt",
          encoding='utf-8').read()
book=book.lower()
alf= ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
      'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
      'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
      'э', 'ю', 'я']
res=[(i,sum(1 for x in book if x==i)/len(book))for i in alf]
print(res)

