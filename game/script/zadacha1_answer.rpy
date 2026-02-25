label zadacha1_answer:

    if not zadacha1_firstTry:

        menu:
            "{i}Стоит попробовать решить в уме еще раз, или прибегнуть к записям...{/i}"
            "Попробовать еще раз":
                jump zadacha1_menu1
            
            "Посмотреть объяснение":
                jump zadacha1_explanation

            "Посмотреть решение":
                jump zadacha1_solution

    jump zadacha1_menu1


label zadacha1_menu1:

    $ menu = renpy.display_menu

    menu:
        "{i}Итак, я думаю, что вероятнее всего это...{/i}"
        "Тигры":
            thoughts "Нет, должно быть, я в чем-то просчитался."
            $ zadacha1_firstTry=False
            jump zadacha1_answer

        "Змеи":
            thoughts "Нет, должно быть, я в чем-то просчитался."
            $ zadacha1_firstTry=False
            jump zadacha1_answer

        "Осы":
            thoughts "Нет, должно быть, я в чем-то просчитался."
            $ zadacha1_firstTry=False
            jump zadacha1_answer

        "Другой вариант":
            jump zadacha1_answer_extra

label zadacha1_answer_extra:

    menu:
        "{i}Итак, я думаю, что вероятнее всего это...{/i}"
        "Тигры или Змеи":
            thoughts "Нет, должно быть, я в чем-то просчитался."
            $ zadacha1_firstTry=False
            jump zadacha1_answer

        "Змеи или Осы": #Правильный вариант 
            thoughts "Да, именно так!" 
            $ zadacha1_firstTry=False
            #jump #продолжение 

        "Осы или Тигры":
            thoughts "Нет, должно быть, я в чем-то просчитался."
            $ zadacha1_firstTry=False
            jump zadacha1_answer

        "Тигры или Змеи или Осы":
            thoughts "Нет, должно быть, я в чем-то просчитался."
            $ zadacha1_firstTry=False
            jump zadacha1_answer

        "Назад":
            jump zadacha1_menu1

