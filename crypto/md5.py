import hashlib   
for i in range(32,127):
    for j in range(32,127):
        for k in range(32,127):
            m=hashlib.md5()
            m.update('TASC'.encode('UTF-8')+chr(i).encode('UTF-8')+'O3RJMV'.encode('UTF-8')+chr(j).encode('UTF-8')+'WDJKX'.encode('UTF-8')+chr(k).encode('UTF-8')+'ZM'.encode('UTF-8'))
            des=m.hexdigest()
            if 'e9032' in des and 'da' in des and '911513' in des:
                print(des)