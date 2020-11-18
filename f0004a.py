név = input('Kérem a neved. ')
kor = input('Kérem a korod. ') 
kor = int(kor) 
év = input('Milyen évet írunk?' )
év = int(év)
születési_év = év - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')