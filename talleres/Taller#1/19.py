def a_romano(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    T = ""
    i = 0
    while num > 0:
        if num >= val[i]:
            T += rom[i]
            num -= val[i]
        else:
            i += 1
    return T
def a_arabigo(rom):
    valores = {'M':1000,'m':1000,'d':500,'D':500,'c':100,'C':100,'l':50,'L':50,'x':10,'X':10,'v':5,'V': 5,'i':1, 'I': 1}
    num = 0
    ante = 0
    for letra in rom:
        valor = valores[letra]
        if valor > ante:
            num += valor - 2 * ante
        else:
            num += valor
        ant = valor
    return num

r =input("digite el numero en romano") 
TT = a_arabigo(r)
print(f"{r} en números arábigos es: {TT}")
n=int(input("Digite el numero"))
resultado=a_romano(n)
print(f"{n} en números romanos es: {resultado}")