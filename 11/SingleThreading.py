from time import *
def sqr(n):
    for x in n:
        sleep(1)
        
def cube(n):
    for x in n:
        sleep(1)
        
n = [1,2,3,4,5,6,7,8]
start = time()
sqr(n)
cube(n)
end = time()

print("Waktu mulai :", start)
print("Waktu selesai :", end)
print("Durasi eksekusi program:", end-start)
