# The Stocker
## Introducción al problema
La economía es parte de la vida de todas las personas. Desde ahorrar hasta hacer trading con criptomonedas. La velocidad con la que está avanzando este mundo es muy alta y así como muchos pueden seguirla minuto a minuto, muchos otros quedan atrás y no saben como entrar. Por este motivo hemos decidido crear The Stocker. Una red social enfocada completamente en aquellas personas que desean aprender más acerca del mundo financiero directamente desde los expertos.
## Nuestra solución
### Rangos
En The Stocker, los usuarios podrán ver publicaciones de aquellos temas de finanzas que más les interesan. Pero lo último que quisiéramos es que la plataforma se llene de desinformación. Entonces, para asegurarnos de que reciban contenido de calidad y confiable, implementamos un sistema de rangos de usuarios. ¿Cómo funciona esto? Los usuarios, a medida que interactúen en la plataforma, irán recibiendo feedback de los demás usuarios a través de “upvotes” y “downvotes”. El rango del usuario se calcula a partir de todos estos upvotes y downvotes de todas sus publicaciones o comentarios. Si publica contenido útil y confiable recibirá “upvotes” y subirá de rango. A mayor rango del usuario, más cosas puede hacer en nuestra plataforma. Por ejemplo, un usuario recién creado no puede publicar contenido propio sino que tiene que empezar a ganarse reputación a través de upvotes con sus comentarios en otras publicaciones.Pero, si en algún momento comienza a publicar contenido que a la gente no le sirva, ya sea porque es falso o perjudicial para la comunidad, probablemente recibirá “downvotes” lo que lo harán bajar su rango y perder los beneficios antes obtenidos. De esta forma consideramos que el contenido publicado será preciso y confiable. Y cuidamos a aquellas personas que vienen a The Stocker a aprender.
### Subject of the Month
Por otro lado, también nos pareció importante darle a los usuarios la capacidad de comunicar sobre qué les gustaría aprender. Por esto lo que pensamos fue que cada mes se puede votar un tema en específico como puede ser: criptomonedas, plazo fijo, créditos o tasas de interés. Y cuando termina el mes, se cierra la votación y el tema más votado será nombrado el nuevo “Tema del mes”. Durante un mes, todas los upvotes en publicaciones sobre este tema suman doble para el rango, incentivando así el contenido de este tema. Hay una sección específica de nuestra aplicación que reúne todos los contenidos relacionados con este tema. Además, en esta sección se encuentran las empresas que tienen relevancia en la categoría ganadora, dándoles así más visibilidad y hasta una opción de invertir en ellas. Esto es, cuando un usuario se dirige al perfil de una de estas empresas, tiene la opción de pagar un monto y a cambio recibe acceso un foro exclusivo estilo AMA (Ask Me Anything) de la empresa de interés.
### Otras funcionalidades
Sobre estas dos funcionalidades que consideramos las diferenciales de nuestra aplicación, tenemos también una sección de Tendencias, en la que se podrá ver las publicaciones más destacadas del último tiempo y también cuáles fueron los temas más hablados. También tenemos una sección de Explorar en la cuál el objetivo es que aquí un usuario pueda entrar para descubrir sobre temas que no había leído mucho antes. Tenemos en mente también que exista un simulador financiero en el cual se le daría dinero ficticio al usuario y vaya experimentando con distintas opciones, como invertir en la bolsa de valores y vaya viendo que tan buena fue esa inversión después en comparación a otras posibles opciones. Esta última funcionalidad también pensamos que podría ser clave para implementar en profundidad en el futuro cercano. Y finalmente, consideramos que un sistema de mensajería es básico para completar el concepto de red social y lograr también que el usuario pueda sentirse más partícipe de la comunidad al interactuar directamente con otras personas que también usan la plataforma.
### Tecnologías
Durante estos días implementamos el front-end con Vue, para así tener una mejor experiencia del usuario con una Single Page Application. Usamos una base de datos postgres para guardar todo tipo de información de la aplicación. Y para unir el front-end con la base de datos, decidimos hacer una API en Python utilizando el framework “FastAPI”
### Modelo de negocio
Todo suena muy lindo, pero ¿cómo sería viable esto económicamente? Principalmente, como toda red social, tenemos en mente generar ingresos mediante anuncios personalizados. Especialmente podríamos conseguir que haya instituciones financieras interesadas en mostrar sus ofertas a personas que justamente están interesadas en hacer provecho de ellas. En segunda instancia, cobraríamos una pequeña comisión cuando las personas inviertan en una empresa del tema del mes.

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
