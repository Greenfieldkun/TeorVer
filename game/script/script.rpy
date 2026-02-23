# Определение персонажей игры.

define k = Character('Кирагуро Хуёдзава', color="#beb1ce") #b11b3b

define nvl_narrator_white = Character(kind=nvl_narrator, what_color="#ffffff")

define s = Character('Ликорис', color="#ff3918") #38df5c

define s_phone = Character(kind=s, what_italic=True)

define hint = Character('Подсказка', color="#fbff00")

define thoughts = Character(None, what_italic=True)

# Определение ПЕРЕХОДОВ

define slow_dissolve = Dissolve(1.0)

define circleirisin = ImageDissolve("imagedissolve circleiris.png", 2.0, 8 , reverse=True)

define circleirisout = ImageDissolve("imagedissolve circleiris.png", 2.0, 8)

#Определение СТИЛЕЙ и ЦВЕТОВ

style def:
    color "#FFB251"

style hl:
    color "#FFB251"
    font "palatinolinotype_bold.ttf"

#Определение ПЕРЕМЕННЫХ

init python:

    zadacha1_firstTry = True

#Определение АНИМАЦИЙ

transform walkAround:
    # Начальная позиция слева
    xalign 0.0
    yalign 1.0
    
    # 1. Идем от левого края к правому
    parallel:
        ease 6.0 xalign 1.0
    
    parallel:
        ease 0.3 yoffset 7  # покачивание вокруг поднятой позиции
        ease 0.3 yoffset 15
        repeat 10
    
    # Пауза в правом углу
    pause 0.5
    
    # 2. Поворот налево
    xzoom -1
    pause 0.3
    
    # 3. Идем от правого края к левому
    parallel:
        ease 6.0 xalign 0.0
    
    parallel:
        ease 0.3 yoffset 7
        ease 0.3 yoffset 15
        repeat 10
    
    # Пауза в левом углу
    pause 0.5
    
    # 4. Поворот направо (лицом к зрителю)
    xzoom 1
    pause 0.3
    
    # 5. Идем в центр
    parallel:
        ease 3.0 xalign 0.5  # от левого края до центра
    
    parallel:
        ease 0.3 yoffset 7
        ease 0.3 yoffset 15
        repeat 5  # меньше шагов, т.к. путь короче
    
    # 6. Финальная остановка в центре
    ease 0.3 xalign 0.5 yoffset 15


transform lookAround:
    xalign 0.5
    xzoom 1.0
    
    # Осмотрелся направо
    ease 0.7 xzoom -1.0
    pause 0.8  # задержка, смотрит направо
    
    # Осмотрелся налево
    ease 0.7 xzoom 1.0
    pause 0.8  # задержка, смотрит налево
    
    # Еще раз направо (более быстро)
    ease 0.4 xzoom -1.0
    pause 0.4
    
    # Возврат в центр
    ease 0.5 xzoom 1.0


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

init python:
    def slowTransition(text, duration=2.5, speed=8):
        renpy.scene()
        renpy.show("black")
        renpy.with_statement(dissolve)

        renpy.show_screen("slow_text", display_text=text, speed=speed)
        renpy.pause(duration)
        renpy.hide_screen("slow_text")
        
        renpy.with_statement(dissolve)
        renpy.pause(0.5)
        
        return

screen slow_text(display_text, speed=8):
    text "{color=#ffffff}{font=distroy.23.ttf}{size=100}" + display_text + "{/size}{/font}{/color}":
        xalign 0.5
        yalign 0.5
        slow_cps speed

label start:

    jump prolog

    return
