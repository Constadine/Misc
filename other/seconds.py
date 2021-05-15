seconds = int(input("Γράψε τα δευτερόλεπτα προς μετατροπή:"))

hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60


print(f"Είναι {hours}" + (" ώρα" if hours == 1 else " ώρες") + f" {minutes}" + (" λεπτό" if minutes == 1 else " λεπτά") + f" και {seconds}" + (" δευτερόλεπτο." if seconds == 1 else " δευτερόλεπτα."))
