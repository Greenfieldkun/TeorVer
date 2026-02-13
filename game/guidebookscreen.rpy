init python:
    # Словарь для хранения формул
    formula_guidebook = []
    
    # Функция добавления новых записей
    def add_formula(definition):
        if definition not in formula_guidebook:  # Предотвращаем дублирование
            formula_guidebook.append(definition)


# Экран справочника
screen guidebook():
    modal True
    zorder 100
    
    # Прозрачная кнопка-оверлей для закрытия по клику вне окна
    button:
        background "#0000007e"
        xfill True
        yfill True
        action Hide("guidebook")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1050
        ysize 750
        
        
        # Блокируем распространение кликов внутри фрейма
        button:
            background None
            xfill True
            yfill True
            action NullAction()  # Запрещаем закрытие при клике внутри фрейма
            left_margin 40
            right_margin 40
            
            # Кнопка-крестик в левом верхнем углу (абсолютное позиционирование)
            textbutton "Назад": 
                style "close_button"
                action Hide("guidebook")
                xysize(100,20)
                xalign 0.0
                yalign 0.0
                xoffset 80
                yoffset 20
            
            vbox:
                spacing 20
                
                # Заголовок по центру
                text "Справочник":
                    xalign 0.5
                    yoffset 20
                    size gui.interface_text_size
                    font "palatinolinotype_bold.ttf"
                    color gui.selected_color
                
                null height 20
                
                viewport:
                    # scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    
                    vbox:
                        spacing 16
                        for definition in formula_guidebook:
                            hbox:
                                label "[definition]" style "guidebook_definition"

# Стили для текста

style guidebook_definition:
    size 1
    color "#ff0000"

# Стиль для кнопки закрытия
style close_button:
    xsize 40
    ysize 40
    xalign 0.0
    yalign 0.0
    size 20
    color "#FFF"
    hover_color "#FFF"
    padding (0, 0)

# Кнопка вызова справочника
screen guidebook_button():
    zorder 99
    
    imagebutton:
        idle "guidebook_icon.png"  # Замените на путь к вашей иконке
        hover "guidebook_icon_hover.png"
        action Show("guidebook")
        align (1.0, 0.0)  # Правый верхний угол
        xoffset -20
        yoffset 20
