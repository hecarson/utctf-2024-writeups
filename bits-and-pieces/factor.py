from math import isqrt

n = 16895844090302140592659203092326754397916615877156418083775983326567262857434286784352755691231372524046947817027609871339779052340298851455825343914565349651333283551138205456284824077873043013595313773956794816682958706482754685120090750397747015038669047713101397337825418638859770626618854997324831793483659910322937454178396049671348919161991562332828398316094938835561259917841140366936226953293604869404280861112141284704018480497443189808649594222983536682286615023646284397886256209485789545675225329069539408667982428192470430204799653602931007107335558965120815430420898506688511671241705574335613090682013

a_start = 1
for a in range(a_start, n):
    if a % 1000 == 0:
        print(a)

    b = n + a ** 2
    if isqrt(b) ** 2 == b:
        r = isqrt(b) * 2
        s = a * 2
        p = (r + s) // 2
        q = r - p
        print(f"p {p} q {q}")
        break