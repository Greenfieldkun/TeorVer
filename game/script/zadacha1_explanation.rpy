label zadacha1_explanation:

    nvl clear

    nvl_narrator_white "Итак, начнем с краткой записи условия задачи:"

    nvl_narrator_white "{image=images/dano.png}"

    nvl clear

    nvl_narrator_white "Теперь посмотрим на формулу Байеса:"

    nvl_narrator_white "{image=images/bayes.png}"

    nvl clear

    nvl_narrator_white "Как Вы могли заметить, мы уже можем посчитать числитель."

    nvl_narrator_white "А знаменатель можно найти по формуле полной вероятности:"

    nvl_narrator_white "{image=images/full_chance.png}"

    nvl clear

    nvl_narrator_white "Попробуете найти ответ самостоятельно, или желаете посмотреть решение задачи?"

    $ menu = nvl_menu

    menu:
        nvl_narrator_white "Что сделать?"

        "Дать ответ":
            #nvl clear
            jump zadacha1_answer

        "Посмотреть решение":
            jump zadacha1_solution

