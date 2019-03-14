def sockMerchant(n, ar):
    pairs = 0

    for i in range(n):
        for j in range(1,n):
            if ar[i] == ar[j] and ar[i] != 0 and i!=j:
                print("The i {} element is : {}, The j {} element is {} ".format(i,ar[i],j,ar[j]))

                pairs +=1
                ar[i] =0
                ar[j] = 0
                
    
    return pairs

ar = [10,20,20,10,10,30,50,10,20]
here = sockMerchant(9,ar)

print(here)