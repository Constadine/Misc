favorite_Movies = ["Mr.Nobody", "Eye origin", "Coco", "Parasite"]

new_Movie = input("Εισήγαγε τη δική σου αγαπημένη ταινία")

if new_Movie in favorite_Movies:
    print("Δεν έγινε αποθήκευση")
else:
    favorite_Movies.append(new_Movie)
    favorite_Movies.sort()
    print(favorite_Movies)
    print(len(favorite_Movies))


