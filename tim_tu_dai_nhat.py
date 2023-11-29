#hello ican friendly''
def tim_tu_lon_Nhat(s):
    tu_dai_nhat =""

    chuoi_con = s.split()
    for text in chuoi_con:
        if (len(text ) > len(tu_dai_nhat)):
            tu_dai_nhat = text
    return tu_dai_nhat


s1 = input("Nhập chuỗi S : ")
print(tim_tu_lon_Nhat(s1))
