label choice1:

    scene street day   
    show kira right    
    show screen guidebook_button
    with fade

    k "Хм, вот как. Цифры показывают неоднозначную картину: либо Осы, либо Змеи, менее вероятно - Тигры."

    k "Тогда стоит взять курс на первых двух. С кого бы начать расследование?"

    hide kira
    with fade

    menu:
        thoughts "С кого начать?"

        "Змеи":
            k "Хорошо, начнем со Змей."
            jump end

        "Осы":
            k "Хорошо, начнем с Ос."
            jump end

        "Не знаю":
            jump choice1_random

label choice1_random:

    show kira right
    k "Тогда подкину монетку."

    if renpy.random.randint(0, 1) == 0:
        "Орёл! Начнем со Змей."
        jump end
    else:
        "Решка! Начнем с Ос."
        jump end

    
