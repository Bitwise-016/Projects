from hashlib import sha256 #e destul de evident ca fara libraria asta nu avem hash-ul, nu?
MAX_NONCE = 100000000000 #un numar exorbitant de incercari maxime, aici umbli daca stii ca dificultatea va fi ridicola sau infima
#nonce mai este cunoscut si drept proof of work, numarul nostru de iteratii practic
def SHA256(text): #este o scurtare a scrisului, pare a functie de dragul de a avea functii, dar e gandita pentru claritate
    return sha256(text.encode("ascii")).hexdigest() #in acest mic return, se intampla magia obtinerii unui potential hash, luam text-ul, trecut in ascii si apoi folosim pe el hexdigest, la care ii generam sha-ul, ta-dah, am obtinut un hash de 256 de biti/64 hexadecimali

def mine(block_number, tranzactii, previous_hash, zerouri): #ok, cine-s parametrii lui mine? Pai, numarul block-ului curent (exorbitant la nivelul scrierii codului), lista de tranzactii pentru acel block, hash-ul anterior si dificultatea/nr de zerouri
    prefix_str = '0'*zerouri #De unde pana unde inmultiri cu string-uri? Suntem in Python, e destul de logic, un exemplu, '0'*4 iti ofera '0000'
    for nonce in range(MAX_NONCE): #cine e nonce si de ce e in range? Nonce e ghicirea noastra
        text = str(block_number) + tranzactii + previous_hash + str(nonce) #formatul textului care trebuie trecut in hash
        new_hash = SHA256(text) #generarea hash-ului in sine
        if new_hash.startswith(prefix_str): #python are o functie sfanta de startswith, o folosim pentru a verifica numarul de 0-uri in hash-ul nostru
            print(f"Ai minat bitcoini in {nonce} iteratii") #anunta numarul de iteratii la finalul minatului
            return new_hash

    raise BaseException(f"Am incercat de {MAX_NONCE} ori, nimic nou sub soare") #este o functie de oprire, daca a ajuns aici,probabil ca dificultatea este exorbitanta si ar fi bine sa treci pe dogecoin

if __name__=='__main__':
    tranzactii=''' 
    Cosmin->Vlad->20,
    George->Mihai->45
    ''' #niste exemple de tranzactii in bitcoini, mama ce bogati sunteti Cosmin si George
    dificultate=6 #cine e dificultate? Pai asta e numarul de 0-uri de la inceputul hash-ului, 4 e pasnic pentru radiatorul pe baza de i7, dar cu cat mai mare numarul cu atat mai mult dureaza
    import time
    start = time.time() #ce se intampla aici? Simpla curiozitate de a vedea timpul in care s-a intamplat toata treaba
    print("A inceput minatul") #un mesaj prietenos pentru a anunta inceputul minatului
    new_hash = mine(5,tranzactii,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', dificultate) #apelul functiei de minare
    total_time = str((time.time() - start)) #calculul timpului total de minare
    print(f"Gata minatul, a durat doar {total_time} secunde")
    print(new_hash) #hash-ul victorios
#comentariile lui Filip, sincer, bitcoin miner-ul astae este doar un hash brute forcer pompos, dar sunt 15 linii de cod care chiar fac ceva, eu sunt fericit