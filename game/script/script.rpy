# Определение персонажей игры.

define k = Character('Кирагуро Хуёдзава', color="#b11b3b")

define nvl_narrator_white = Character(kind=nvl_narrator, what_color="#ffffff")

define s = Character('Сакура', color="#38df5c")

define s_phone = Character(kind=s, what_italic=True)

define hint = Character('Подсказка', color="#fbff00")

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
