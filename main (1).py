def egcd(a, b):
    s = 0; temp_s = 1
    t = 1; temp_t = 1
    r = b; temp_r = a
    
    while r != 0:
        co = old_r // r
        temp_r, r = r, temp_r - co * r
        temp_s, s = s, temp_s - co * s
        temp_t, t = t, temp_t - co * t
        
    return temp_r, temp_s, temp_t


def modulo(a, b):
    gcd, x, y = egcd(a,b)
    
    if x < 0:
        x += m
        
    return x
    
def encrypt(e, n, msg):
    cipher = ""
    
    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, n)) + " "
    
    return cipher

def decrypt(d, n, cipher):
    msg = ""
    
    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, n))
    
    return msg

def rsa():
    print("Este es un mensaje encriptado")
    
    p = 11
    q = 13
    n = p * q
    euler = (p-1)*(q-1)
    e = 13
    
    d = modulo(e, euler)
    
    msg = "Este es un mensaje encriptado"
    
    enc = encrypt(e, n, msg)
    dec = decrypt(d, n, enc)
    
    print("Mensaje: " + msg)
    print("Encriptado: " + enc)
    print("Desencriptado: " + dec)
    
    
rsa()