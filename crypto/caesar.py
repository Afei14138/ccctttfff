# 凯撒密码不改变原有长度，对照 flag 格式可以得到加密规律
txt = "afZ_r9VYfScOeO_UL^RWUc"
j = 5
for i in txt:
    print(chr(ord(i)+j),end='')
    j += 1