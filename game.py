import os
import random

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage


### CREDENTIALS

with open("openai_api_key.txt", "r", encoding="UTF-8") as f:
    key = f.read()
os.environ["OPENAI_API_KEY"] = key

### FACTS (sacados de https://www.fundeu.es/blog/10-palabras-navidenas-que-quiza-no-conozcas/)

fact1 = '''
La Navidad es una época de regalos en todos los lugares donde se celebra, pero no en todos ellos es el mismo personaje el encargado de la agotadora tarea de repartirlos. La tradición española de los Reyes Magos está extendida en muchos países hispanohablantes y convive con la que señala como regalador oficial a san Nicolás, el santo que, quizá por generoso, tiene más nombres distintos. En algunos sitios es conocido como Santa Claus (a veces pronunciado como Santa Clos o Santi Clo), aunque también simplemente como Santa o hasta Colacho para los costarricenses, que parecen tener mucha confianza con él. Por supuesto, es también Papá Noel en medio mundo, mientras que en Chile, donde prefieren la expresión Pascua a Navidad, lo llaman el Viejo o Viejito Pascuero. En otros países es el mismísimo Niño Jesús o Niño Dios quien lleva los presentes. Y en la República Dominicana, la Vieja Belén llega, ya en enero, al rescate de los que no recibieron regalos de ninguno de los anteriores. 
'''

fact2 = '''
Los angelitos son un complemento indispensable en la decoración navideña: presiden el árbol, sobrevuelan el nacimiento o se asoman a ventanas y puertas. Pero en la República Dominicana la palabra tiene un significado añadido: allí muchos grupos de amigos o familiares juegan al angelito, es decir, intercambian pequeños regalos entre varias personas sin que ninguna sepa de quién los recibió. Es lo que en otros lugares se conoce como amigo invisible, amigo secreto o Santa secreto. 
'''

fact3 = '''
Belén, nacimiento, pesebre y portal son las palabras más habituales para referirse a la representación del nacimiento de Jesús que adorna millones de iglesias y hogares. En Costa Rica emplean también la voz pasito, que se aplica al conjunto de las cinco principales figuras: la Virgen María, san José, el Niño Jesús, la mula y el buey. 
'''

fact4 = '''
Muchas exquisiteces pueblan las mesas navideñas, pero seguro que no conocías la hallaca, que, como explica el Diccionario de la Lengua Española, es un ‘pastel de harina de maíz, relleno de un guiso elaborado con varias clases de carne o de pescado en trozos pequeños y otros ingredientes, que, envuelto en hojas de plátano o cambur, se hace especialmente por Navidad’ en Venezuela. Claro que también se pueden comer catibías en la República Dominicana, tamales y nacatamales en todo Centroamérica, picana en Bolivia y otras mil maravillas de nombres tan prometedores como su sabor. 
'''

fact5 = '''
Que un alfajor es un dulce delicioso es una verdad incuestionable para los golosos del mundo entero. O no. Porque, en realidad, son varios dulces deliciosos, que seguramente comparten origen árabe (y aún más antiguo), como indica su etimología recogida en el Diccionario: «Del árabe hispano fašúr, este del persa afšor ‘jugo’, y este del pelvi afšurdan ‘exprimir’». Pero mientras que en buena parte de América, en especial en el Cono Sur, se trata de dos o más galletas unidas por una capa de dulce (generalmente de leche) y a menudo cubiertas por chocolate, azúcar o glaseado, en España, sobre todo en Andalucía y Murcia, es un cilindro compacto hecho con pasta de almendras, miel y nueces que se come sobre todo en Navidad. Y aún hay más delicias que reciben ese mismo nombre en México, Honduras, Nicaragua y Venezuela. Habrá que probarlas todas… 
'''

fact6 = '''
La natilla, así en singular, es un postre imprescindible en las mesas navideñas colombianas (‘plato típico de Navidad que se hace con maíz cocido, molido y colado, panela, canela y otras especias, y que se solidifica al enfriarse’). Parece ser un pariente más o menos cercano de las natillas, en plural, un postre de consistencia cremosa muy popular en España y que se come en todas las épocas de año. 
'''

fact7 = '''
El mazapán, ese dulce hecho con almendras molidas y azúcar que se prepara en muchos lugares del mundo, está en España indisolublemente unido a la Navidad. Lo que puede que no sepan todos sus golosos seguidores es de dónde viene esa palabra tan sonora y llena de aes. El Diccionario apunta que su origen parece ser la voz árabe hispana pičmáṭ, a su vez derivada del griego παξαμάδιον paxamádion ‘bizcochito’ y que puede haber evolucionado hasta la forma actual influida por las palabras masa y pan. 
'''

fact8 = '''
Los brindis con champán (o champaña) son comunes estos días en todos los países del ámbito hispanohablante, y en todo el mundo en realidad. Pero en algunos lugares la bebida de origen francés no está sola en las celebraciones navideñas. En Chile, por ejemplo, es costumbre tomar en estas fechas una bebida con el curioso nombre de cola de mono (o colemono), un cóctel hecho con aguardiente, leche, café, azúcar y especias. 
'''

fact9 = '''
Seguro que conoces el aguinaldo, pero quizá no sepas la cantidad de significados que tiene la palabra, muchos de ellos relacionados con estas fiestas. Un aguinaldo es un regalo de Navidad, pero también la paga extraordinaria o la bonificación de fin de año que los trabajadores cobran en algunos países, un canto propio de estas fiestas (Venezuela, Puerto Rico y otros), una celebración religiosa (la novena de aguinaldos en Ecuador y Colombia) y hasta una planta tropical muy frecuente en Cuba y que florece… en Navidad. La explicación a tantos significados la encontramos en la etimología de la palabra: viene de aguilando y esta a su vez parece provenir del latín hoc in anno, o sea, ‘en este año’, muy adecuada para todas esas cosas (regalos, pagas, cantos, oraciones o plantas) que llegan justo cuando el calendario está dejando caer las últimas hojas. 
'''

fact10 = '''
Seguramente te sorprenderá saber que en el Diccionario de la Lengua Española, además de la palabra nochebuena, figura nochebueno, que es ‘una torta grande amasada con aceite, almendras, piñones y otras cosas, para la colación de Nochebuena’ y también un ‘tronco grande de leña que ponen en el fuego la noche de Navidad’. Aunque el término se utiliza poco, la verdad es que las dos realidades a las que se refiere parecen dos muy buenos acompañantes para pasar una feliz noche del 24 de diciembre. 
'''

facts = [
    fact1,
    fact2,
    fact3,
    fact4,
    fact5,
    fact6,
    fact7,
    fact8,
    fact9,
    fact10,
]

random.shuffle(facts)

### PROMPT

system_message = f'''
Genera un dato ficticio sobre una o varias palabras del español de todo el mundo relacionadas con la Navidad.
En la medida de lo posible, invéntate palabras, sus definiciones y sus etimologías, ya que se trata de curiosidades lingüísticas.
Las palabras curiosas pueden denominar tradiciones, platos, aodrnos, a los protagonistas de la celebración...

Es importante que todo lo que digas sea ficticio, que NO sea verdad, pero que parezca verdad.
Tu texto se va a presentar junto a otro que sí es verdad, para que el usuario juegue a adivinar cuál es verdad.

Te dejo algunos ejemplos para que los imites:

Ejemplo 1
---------
{facts[0]}

Ejemplo 2
---------
{facts[1]}

Ejemplo 3
---------
{facts[2]}

Ejemplo 4
---------
{facts[3]}

'''

messages = [
    SystemMessage(system_message),
]

### LLM

llm_name = "gpt-3.5-turbo-0125"
model = ChatOpenAI(model=llm_name, temperature=0.9)

### INVOCATION

score = 0
for num, fact in enumerate(facts):
    rsp = model.invoke(messages)

    adivinanzas = [rsp.content, fact]
    random.shuffle(adivinanzas)

    print("RONDA ", num+1, "/10", sep="")
    print("A ver si sabes cuál de estos dos datos es verdad!")
    print()
    print("Dato 1:")
    print()
    print(adivinanzas[0])
    print("------------------------")
    print("Dato 2:")
    print()
    print(adivinanzas[1])
    print()

    numero = int(input("Cuál piensas que es verdad? "))
    eleccion = adivinanzas[numero-1]
    
    if eleccion.endswith(" \n"):
        print("Acertaste!")
        score += 1
    else:
        print("Vaya! Esa no era la buena")
    
    print()

print("Este es tu score final:")
print(score)

    
    
    