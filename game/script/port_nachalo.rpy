label port_nachalo:

    window hide

    $ slowTransition('Расследование В Порту')

    scene street day
    with fade

    show screen guidebook_button  

    narrator "В лобби подпольной торговли оружием Порт не за глаза называли \"шелковым путём\". {w} Слово порт было лишь условным названием невзрачного серого переулка, а не буквально морским причалом. "

    narrator "Дело в том, что торговля с иностранцами всегда проходила в этом месте, а подкупленные полицейские закрывали глаза на контрабанду."

    narrator "Это место Кирагуро знал как свои пять пальцев. Добираясь до туда, он скурпулезно визуализировал Порт в своём воображении, чтобы добравшись до него, заметить то, чего там быть не должно."

    show kira right at left

    k "Ничего себе... тут всё...\n{w}Как обычно!?"

    window hide
    hide screen guidebook_button

    pause 0.1

    show kira right at lookAround
    pause 17.0

    scene street day
    show kira smoke_right
    show screen guidebook_button
    with fade
    pause 1.0

    # narrator "{i}"

      
    


    k "Чернее дегтя..."

    hide screen guidebook_button

    jump zadacha1