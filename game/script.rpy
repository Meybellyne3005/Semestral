image imagenCiudad = "ciudad.png"
image imagenInterrogar = "sala_interrogatorio.png"
image carro1="carro_1.png"
image carro2="carro_2.jpg"
image celular="celular.jpg"
image piso="piso.png"
image casavecino="CasaV.png"
image victima="1.png"
image a1="a1.jpg"
image a2="a2.jpg"
image a3="a3.jpg"
image estacion="estacion.jpg"

image art normal = "art_normal.png"
image art pensando = "art_pensando.png"
image art enojado= "art_enojado.png"
image burt normal = "burt_normal.png"
image carl normal = "carl_normal.png"
image carl gritando = "carl_gritando.png"
image detective normal = "detective_normal.png"
image detective pensando = "detective_pensando.png"
image detective enojado = "detective_enojado.png"
image detective orden = "detective_orden.png"


define art = Character('Art', color="#90ee90")
define carl= Character('Carl', color="#ff0000")
define burt = Character('Burt', color="#ffff00")
define detective = Character('Detective', color="#e0ffff")

label start:
    scene imagenCiudad 
    "Un nuevo crimen a sucedido en la ciudad..."
    "Un cuerpo fue hallado sin vida..."
    "Hay tres sospechosos..."
    "La estacion de policia mando a su mejor detective a investigar el caso"
    scene imagenInterrogar

    show detective normal 
    detective "Señor Art, usted ha sido señalado como sospechoso del homicidio de la victima, tiene algo que decir"
    hide detective normal 
    show art normal
    art "Yo soy inocente!"
    hide art normal
    show detective normal
    detective "Algo mas aparte de eso?"
    hide detective normal
    show art pensando
    art "Se que Burt era amigo de la victima"
    show detective normal
    detective "Entiendo..."
    hide detective normal
    show art normal
    art "ah! Carl y la victima eran enemigos a muerte!"
    hide art normal
    show detective normal
    detective"Tomare en cuenta eso, gracias!"

    detective "Señor Burt, parece que esta involucrado en algo grave, que nos tiene que decir al respecto"
    hide detective normal
    show burt normal 
    burt "Yo estaba fuera de la ciudad, no se nada!"
    hide burt normal
    show detective normal
    detective "No creo que sea cierto"
    hide detective normal
    show burt normal
    burt "Es la verdad! ni siquiera conocia a la victima!"
    hide burt normal
    show detective normal
    detective "es raro, escuchamos lo contrario"
    hide detective normal
    show burt normal
    burt "Calumnias!! son solo eso!"
    hide burt normal

    show detective normal
    detective "Señor Carl, usted es el ultimo implicado en el homicidio, quisiera hablarnos sobre el caso?"
    hide detective normal
    show carl gritando
    carl "No deberia contestar preguntas! yo soy inocente de todo esto!"
    hide carl gritando
    show detective normal
    detective "Y no sabe mas nada que nos pueda ayudar?"
    hide detective normal
    show carl normal
    carl "No se quien lo hizo"
    carl "Aunque yo vi esos dos, Art y Burt manejando dentro de la ciudad"
    hide carl normal
    show detective normal
    detective "Esto nos va servir de mucha ayuda"
    hide detective normal
    show carl normal
    carl "No he matado a nadie!"
    hide carl normal

    with dissolve 

    show detective pensando

    python:
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult('/home/edez/Documents/Renpy-files/Semestral/game/adriandetective.pl')
        asesino = list(prolog.query('murderer(X)'))
        detective("Por ahora el homicida es %s"%asesino[0]['X'])

    detective "Mejor sigo investigando para ver si aclaro el caso..."

    python:
      i=0
      culpaBurt=0
      culpaArt=0
      culpaCarl=0
      pista1=True
      pista2=True
      pista3=True
      pista4=True
      pista5=True
      pista6=True
      pista7=True

   
    "El detective solo tiene 3 oportunidades para tratar de aclarar el caso..."
    while i < 3:
      scene imagenCiudad
      menu:

        "Revisar Carro de Art y Burt" if pista1:
          scene carro1
          detective "En el carro de Art no habia nada fuera de la comun"
          scene carro2
          detective "Pero en el de Burt olia a perfume de mujer"
          python:
             i+=1
             culpaBurt+=1
             pista1=False
           
        "Registrar pertenencias de la victima" if pista2:
          scene celular
          detective "Los registros de llamadas fueron borrados, sospechoso!"
          detective "Tampoco hay fotos guardadas"
          python:
             i+=1
             culpaCarl+=1
             pista2=False

        "Volver a revisar la escena del crimen" if pista3:
          scene piso
          detective "Hay rastros de cenizas de cigarrillo en el piso"
          detective "La victima no era fumadora"
          python:
             i+=1
             culpaBurt+=1
             pista3=False
 
        "Asegurarse que Art sea culpable preguntandole mas" if pista4:
          scene imagenInterrogar
          show detective normal
          detective "Señor Art, temo que todas las declaraciones lo señalan a usted como el culpable"
          detective "Si tiene algo mas que decir es el momento adecuado"
          hide detective normal
          show art enojado
          art "Ya no dire mas nada sin tener a un abogado!"
          hide art enojado
          show detective normal
          detective "Nervioso Señor Art, puedo arrestarlo ya si quiero"
          hide detective normal
          show art enojado 
          art "Cuando la llame esta tarde parecia nerviosa! no dire mas"
          hide art enojado
          show detective normal
          detective "..."
          hide detective normal
          python:
             i+=1
             culpaCarl+=1
             pista4=False

        "Preguntarle a los vecinos" if pista5:
          scene casavecino
          detective "Al parecer los vecinos no estan"
          detective "Es raro! es como si el homicidio estuviera planeado para cuando la gente no estuviera"
          python:
             i+=1
             culpaCarl+=1
             pista5=False

        "Mirar a la victima nuevamente" if pista6:
          scene victima
          detective "Aparte de los signos de forcejeo pareciera que fue amarrada de los pies"
          detective "Porque tendria el cabello mojado cuando iba a salir supuestamente..."
          python:
             i+=1
             culpaArt+=1
             pista6=False
       
        "Revisar los apartamentos de los sospechosos" if pista7: 
          scene a1
          detective "Apartamento de Art Limpio, pareciera que fuera a mudarse o ocultando algo"
          scene a2
          detective "Apartamento de Burt Desordenado, pero tampoco hay nada fuera de lo comun"
          scene a3
          detective "Apartamento de Carl, Todo tranquilo, hay fotos de Carl con la victima, parecen que es de meses atras"
          python:
             i+=1
             culpaBurt+=1
             pista7=False

    
    python:
      if(culpaBurt > culpaCarl and culpaBurt > culpaArt):
       mato = 'murderer(burt).'
      else:
        if(culpaCarl > culpaBurt and culpaCarl > culpaArt):
           mato = 'murderer(carl).'
        else:
          mato = 'murderer(art).'

    scene estacion
    show detective pensando

    detective "Que hago?..."
    "El detective tiene que elegir entre dejarse llevar por los primeros testimonios"
    "Que parecen que muestran claramente quien es el culpable"
    "O sumar los rastros de la investigacion mas los testimonios..."

    menu:
      "Que hara el detective??"


      "Usar los testimonios mas los rastros de la investigacion":
            show detective enojado
            detective "No tengo mas nada que decir!, el caso esta resuelto"
        
            python:
                from pyswip import Prolog
          
                new_prolog_code = open('/home/edez/Documents/Renpy-files/Semestral/game/murder.pl','w')
                new_prolog_code.write(mato)
                new_prolog_code.close()
                prolog = Prolog()
                prolog.consult('/home/edez/Documents/Renpy-files/Semestral/game/murder.pl')
                homicida = list(prolog.query('murderer(X)'))
                detective ("El asesino es %s"%homicida[0]['X'])
           
            hide detective enojado
            show detective orden
            detective "ARRESTENLO!"
      



      "Dejarse llevar por los testimonios":
            show detective enojado
            detective "No tengo mas nada que decir!, el caso esta resuelto"
        
            python:
               from pyswip import Prolog
               prolog = Prolog()
               prolog.consult('/home/edez/Documents/Renpy-files/Semestral/game/adriandetective.pl')
               asesino = list(prolog.query('murderer(X)'))
               detective("...el homicida es usted Señor %s"%asesino[0]['X'])
            
            hide detective enojado
            show detective orden
            detective "ARRESTENLO!"
   

    hide detective orden         
    scene imagenCiudad
    "FIN DEL JUEGO"
    return

