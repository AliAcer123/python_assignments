sentence = input("enter your sentence :").lower()

let = []
for i in sentence:
    let.append(i)
c_let = []
for i in let:
    c_let.append( let.count(i))
sonuc = dict(zip(let,c_let))
print(sonuc)
