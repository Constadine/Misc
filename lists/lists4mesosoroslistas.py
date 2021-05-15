values = [55, 28, 20, 20, 14, 16, 64, 15, 151, 125]
experiment_Chosen = []
Sum = 0
n=1

print(f"{values}\nΟ πίνακας περιέχει τις τιμές {len(values)} πειραμάτων και φαίνεται παραπάνω.")

ans = int(input(f"Από αριστερά στα δεξιά η αρίθμηση των πειραμάτων είναι: 1-{len(values)}. Επέλεξε ποιών θες το μέσο όρο και όταν τελειώσεις πάτα το 0: "))


while ans != 0:
    if n == len(values):
        experiment_Chosen.append(ans-1)
        print(f"Διάλεξες το πείραμα με τιμή {values[ans-1]} και δεν υπάρχουν άλλα πειράματα.")
        break
    else:
        if ans-1 in experiment_Chosen:
            # print("Im in if")
            ans = int(input(f"Έχεις ήδη εισάγει τη τιμή του {ans}ου πειράματος. Επέλεξε άλλο :"))  
        else:
            # print("Im in else")
            if ans > len(values) or ans == None:
                ans = int(input((f"Πρέπει να δώσεις αριθμό μεταξύ 1-{len(values)}! Προσπάθησε ξανά: ")))
            else:
                experiment_Chosen.append(ans-1)
                ans = int(input(f"Διάλεξες το πείραμα με τιμή {values[ans-1]}. Ποιο άλλο; "))
                n +=1     
                # print(n)
    
for i in range(len(experiment_Chosen)):
    Sum += values[experiment_Chosen[i]]

print(f"Ο μέσος όρος των {str(n-1)} πειραμάτων που διάλεξες είναι: " + str(Sum/(n-1)))

