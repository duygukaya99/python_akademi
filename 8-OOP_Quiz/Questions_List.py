# import Classes # class içindeki questiona erişmek için
# Soru1 = Classes.Questions("sorudjksdk", ["a şıkkı", "b", "c", "cevap"])
# question_list = [Soru1, Soru2, Soru3] # bu şekilde tek tek oluşturmak uzun

from Classes import Questions as Q

# soru = Q("soru1", ["a", "b"], "cevap")
question_list = [
    Q("Bazı aylar 30, bazıları 31 çeker; kaç ayda 28 gün vardır?", ["11", "12", "1"], "12"),
    Q("Sadece bir tek kibritiniz var, içinde bir gaz lambası, bir gaz sobası, ve bir de mum bulunan karanlık ve soğuk bir odaya girdiniz… Önce hangisini yakarsınız?", ["Kibrit", "Mum", "Gaz Lambası"], "Kibrit"),
    Q("Doktorunuz size 3 hap verir ve bunları yarımşar saat arayla almanızı tavsiye ederse, ilaçların tamamını bitirmeniz ne kadar sürer?", ["11", "3", "1"], "3")  
]
