hero={"Здоровье":100, "Имя": "герой", "Урон":15}
enemy={"Здоровье":100, "Имя": "враг", "Урон":12}




round_num = 1
while hero["Здоровье"] > 0 and enemy["Здоровье"] > 0:
    print(f"\n--- Раунд {round_num} ---")


    enemy["Здоровье"] -= hero["Урон"]
    print(f"{hero['Имя']} нанес {hero['Урон']} урона {enemy['Имя']}у")

    if enemy["Здоровье"] <= 0:
        print(f"\n{enemy['Имя']} повержен! {hero['Имя']} побеждает!")
        break

    else:
        print(f"У {enemy['Имя']} осталось {enemy['Здоровье']} здоровья")





    hero["Здоровье"] -= enemy["Урон"]
    print(f"{enemy['Имя']} нанес {enemy['Урон']} урона {hero['Имя']}у")



    if hero["Здоровье"] <= 0:
        print(f"\n{hero['Имя']} повержен! {enemy['Имя']} побеждает!")
        break
    print(f"У {hero['Имя']}а осталось {hero['Здоровье']} здоровья")
    round_num += 1