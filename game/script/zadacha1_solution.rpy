label zadacha1_solution:

    nvl clear

    nvl_narrator_white "Итак, для начала переведём проценты в целые числа:"

    nvl_narrator_white "{image=images/dano_converted.png}"

    nvl clear

    nvl_narrator_white "Затем найдём полную вероятность P(A) по формуле:\nP(A) = P(H1)×P(A|H1) + P(H2)×P(A|H2) + ... + P(Hn)×P(A|Hn)"

    nvl_narrator_white "{image=images/full_chance_solved.png}"

    nvl clear

    nvl_narrator_white "Далее находим апостериорные вероятности P(Hi|A) по формуле Байеса:\nP(Hi|A)=(P(Hi)×P(A|Hi))/P(A)"

    nvl_narrator_white "{image=images/bayes_solved.png}"

    nvl clear

    nvl_narrator_white "Теперь остаётся только сравнить вероятности, и дать верный ответ!"

    $ menu = nvl_menu

    menu:
        "Дать ответ":
            #nvl clear
            $ zadacha1_firstTry=True
            jump zadacha1_answer
