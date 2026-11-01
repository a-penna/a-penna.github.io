# Política de privacidad de Girostella

**Última actualización: 25 de octubre de 2026**

La presente política de privacidad describe el tratamiento de los datos personales realizado a través de la aplicación móvil **Girostella** (en adelante, la «Aplicación»), de conformidad con el Reglamento (UE) 2016/679 (en adelante, el «RGPD») y las demás disposiciones aplicables en materia de protección de datos personales.

## 1. Responsable del tratamiento

El responsable del tratamiento es **Girostella**.

Correo electrónico: **[alessandro_penna@icloud.com](mailto:alessandro_penna@icloud.com)**

## 2. Datos tratados por la Aplicación

Girostella está diseñada conforme al principio de minimización de datos.

La Aplicación no requiere la creación de una cuenta propia de Girostella y no utiliza servidores gestionados por el Responsable del tratamiento para recopilar datos del juego. No integra SDK independientes de análisis estadístico ni servicios de terceros específicamente destinados a informar sobre fallos de la aplicación, sin perjuicio del tratamiento de datos técnicos y de diagnóstico realizado por los servicios publicitarios descritos en la sección 6.

La Aplicación no solicita acceso a la ubicación GPS, la cámara, el micrófono, los contactos, las fotografías, el calendario ni los datos de salud. Tampoco exige a los usuarios que proporcionen su nombre, dirección, número de teléfono o dirección de correo electrónico para jugar.

Durante su uso, se almacenan localmente en el dispositivo los datos necesarios para el funcionamiento del juego, incluidos las puntuaciones, los récords, el progreso, los elementos cosméticos desbloqueados o seleccionados, las preferencias de sonido y respuesta háptica, la información sobre los potenciadores encontrados anteriormente, los identificadores técnicos de las transacciones ya procesadas y las puntuaciones que puedan estar pendientes de sincronización con Game Center.

Estos datos permanecen en el espacio de almacenamiento privado de la Aplicación en el dispositivo y no se transmiten a servidores gestionados por el Responsable del tratamiento. Normalmente se eliminan al desinstalar la Aplicación, salvo las posibles copias conservadas en las copias de seguridad del dispositivo y la información almacenada de forma independiente por los servicios de Apple.

La Aplicación también utiliza Google Mobile Ads y Google User Messaging Platform, que pueden tratar información técnica, identificadores, datos publicitarios e información sobre el uso de la Aplicación, tal como se describe en la sección 6.

El Responsable del tratamiento no mantiene una base de datos propia con las direcciones IP de los jugadores. No obstante, los proveedores de servicios externos utilizados por la Aplicación pueden recibir direcciones IP y otra información técnica necesaria para prestar sus respectivos servicios.

## 3. Game Center

Girostella utiliza **Apple Game Center** para la autenticación opcional de los jugadores, la gestión de las clasificaciones, el envío y la sincronización de puntuaciones y el reconocimiento de los logros del juego.

A través de GameKit, la Aplicación puede recibir temporalmente la información necesaria para el funcionamiento del servicio, incluidos los identificadores de Game Center, las puntuaciones y la información utilizada para mostrar las clasificaciones.

Los nombres de usuario, avatares y otra información del perfil de Game Center pueden mostrarse según la configuración del jugador y las funciones proporcionadas por Apple, pero no se almacenan en servidores gestionados por el Responsable del tratamiento.

### Clasificaciones e información del juego

Girostella utiliza Apple Game Center para gestionar y sincronizar las clasificaciones. Para ello, la Aplicación transmite a Apple las puntuaciones obtenidas por los jugadores y determinada información asociada a los elementos del juego, necesaria para mostrar correctamente las clasificaciones y verificar la integridad de los resultados.

Esta información no incluye datos de identidad civil y puede hacerse visible a otros jugadores a través de las funciones de Game Center.

### Almacenamiento local de información de otros jugadores

Para ofrecer una visualización más coherente de las naves espaciales en las clasificaciones, Girostella almacena en el dispositivo determinada información del juego relativa a otros jugadores encontrados a través de Game Center.

Esta información incluye códigos relacionados con las naves espaciales, las estelas y las colecciones, el contexto técnico asociado a la puntuación y la fecha de la partida.

Cada registro está asociado a una clave seudonimizada generada a partir del identificador de Game Center mediante una función criptográfica y un valor aleatorio local. El identificador original de Game Center y el nombre del jugador no se almacenan en la memoria caché.

La memoria caché contiene un máximo de **25.000 registros** y no tiene un período de conservación fijo. Cuando se supera este límite, se eliminan primero las entradas más antiguas. Normalmente, los datos se eliminan al desinstalar la Aplicación, salvo las posibles copias conservadas en las copias de seguridad del dispositivo.

Esta información no se transmite al Responsable del tratamiento, a Google ni a otros terceros y no se utiliza con fines publicitarios, de elaboración de perfiles ni de análisis estadístico.

El tratamiento se basa en el interés legítimo del Responsable del tratamiento en garantizar una visualización coherente de la información del juego en las clasificaciones, de conformidad con el artículo 6, apartado 1, letra f), del RGPD.

### Amigos y logros de Game Center

Girostella permite reconocer a los amigos de Game Center que aparecen en las clasificaciones mediante un indicador visual específico.

Para ello, la Aplicación utiliza la información proporcionada por la clasificación exclusiva para amigos, sin solicitar acceso a la agenda de contactos del dispositivo ni obtener de forma independiente una lista completa de contactos.

Los identificadores necesarios para la comparación se utilizan exclusivamente en memoria, durante un máximo de cinco minutos, y no se almacenan de forma permanente.

La Aplicación también utiliza los logros de Game Center, incluido el logro **Founder**, para registrar la consecución de determinados objetivos y permitir la recuperación de las recompensas asociadas mediante la misma cuenta de Game Center.

Las puntuaciones obtenidas sin conexión pueden almacenarse temporalmente en el dispositivo hasta su sincronización.

Apple trata los datos gestionados a través de Game Center de acuerdo con su propia política de privacidad y las condiciones aplicables al servicio.

El uso de Game Center es opcional. Sin autenticación, es posible que algunas funciones, como las clasificaciones, la sincronización de puntuaciones y los logros vinculados a la cuenta, no estén disponibles.

## 4. Compras dentro de la Aplicación

Las posibles compras dentro de la Aplicación se gestionan a través de **StoreKit 2 y la App Store**.

Girostella ofrece compras no consumibles relacionadas con elementos cosméticos del juego, como naves espaciales y estelas.

El Responsable del tratamiento no recibe ni almacena números de tarjetas bancarias, datos de cuentas bancarias, credenciales de la cuenta de Apple ni información completa sobre los métodos de pago.

La Aplicación recibe la información técnica necesaria para verificar y gestionar las compras, incluidos los identificadores de productos, los resultados de las transacciones y los identificadores técnicos asociados a estas.

La información necesaria para gestionar los elementos adquiridos y evitar el procesamiento duplicado de transacciones puede almacenarse localmente en el dispositivo.

Los pagos, la facturación, los reembolsos y el historial de compras son gestionados por Apple de conformidad con sus propias condiciones y políticas de privacidad.

## 5. Comprobación de actualizaciones

Al iniciarse, Girostella puede descargar desde **GitHub Pages** un archivo de configuración público que contiene información sobre la versión mínima compatible de la Aplicación y determinados ajustes de las clasificaciones.

La solicitud no incluye puntuaciones, datos de progreso, identificadores de Game Center ni otros datos personales añadidos por la Aplicación.

Como sucede habitualmente en las comunicaciones por Internet, el proveedor del servicio puede recibir la dirección IP del dispositivo e información técnica relacionada con la solicitud. El posible tratamiento y conservación de esta información se rige por las condiciones y políticas de privacidad del proveedor.

El Responsable del tratamiento no utiliza esta conexión para recopilar datos del juego, elaborar perfiles ni supervisar individualmente a los usuarios.

## 6. Publicidad y gestión del consentimiento

Girostella es un juego gratuito que utiliza **Google Mobile Ads (AdMob)** para mostrar anuncios de vídeo recompensados.

Los anuncios se ofrecen exclusivamente cuando un jugador, después de perder una partida, decide ver un vídeo para obtener una segunda oportunidad y reanudar el juego.

La Aplicación no muestra anuncios de tipo banner ni vídeos publicitarios obligatorios durante el desarrollo normal de las partidas.

### Datos tratados por los servicios publicitarios

Para la prestación, medición, seguridad y mejora de los servicios publicitarios, Google Mobile Ads puede recopilar y tratar, según sus propias modalidades y finalidades:

- Direcciones IP e información de ubicación geográfica aproximada deducida de la dirección IP;
- Identificadores del dispositivo, de la Aplicación o específicos del desarrollador;
- Información sobre los anuncios mostrados y las interacciones con los vídeos publicitarios;
- Datos relativos al uso de la Aplicación y a las interacciones con ella;
- Información de diagnóstico, registros de fallos y datos de rendimiento.

Parte de esta información puede asociarse a identificadores técnicos y ser utilizada por Google y los proveedores publicitarios implicados, de conformidad con sus respectivas condiciones y las preferencias de privacidad aplicables.

El Responsable del tratamiento no recibe directamente una base de datos individualizada de los datos recopilados por Google a través de sus SDK publicitarios.

### Consentimiento y preferencias publicitarias

Para los jugadores situados en el Espacio Económico Europeo, el Reino Unido y Suiza, Girostella utiliza **Google User Messaging Platform (UMP)** para mostrar, cuando sea necesario, un mensaje informativo sobre las finalidades del tratamiento y los proveedores publicitarios implicados.

A través de dicho mensaje, los jugadores pueden otorgar su consentimiento, rechazarlo o gestionar las distintas opciones disponibles.

Las preferencias pueden modificarse posteriormente en **Ajustes → Preferencias de anuncios**, cuando esta función sea necesaria y esté disponible a través del sistema de gestión del consentimiento.

Los proveedores publicitarios pueden tratar determinados datos sobre la base del consentimiento o, cuando corresponda y de conformidad con la normativa, sobre otras bases jurídicas, incluido el interés legítimo. Las finalidades, los proveedores y las opciones correspondientes se describen en el mensaje de consentimiento de Google.

El rechazo del consentimiento no impide utilizar el juego. Sin embargo, la disponibilidad de los vídeos publicitarios recompensados puede variar en función de las preferencias expresadas, la normativa aplicable y la disponibilidad de anuncios.

Para obtener más información sobre los tratamientos realizados por los servicios publicitarios, pueden consultarse:

- [Política de Privacidad de Google](https://policies.google.com/privacy?hl=es);
- [Cómo utiliza Google la información de sitios web o aplicaciones que usan sus servicios](https://policies.google.com/technologies/partner-sites?hl=es).

## 7. Asistencia

Si un usuario se pone voluntariamente en contacto con el Responsable del tratamiento por correo electrónico, pueden tratarse su dirección de correo electrónico, el nombre que haya facilitado, el contenido de la solicitud, los posibles archivos adjuntos y la información técnica proporcionada por el usuario.

Estos datos se utilizan exclusivamente para responder a la solicitud, prestar asistencia, gestionar posibles controversias o cumplir obligaciones legales.

Se recomienda a los usuarios que no envíen datos personales que no sean necesarios para atender su solicitud.

## 8. Finalidades y bases jurídicas del tratamiento

| Finalidad | Base jurídica |
|---|---|
| Funcionamiento de la Aplicación y conservación del progreso | Ejecución del servicio solicitado, artículo 6.1.b) del RGPD |
| Game Center, clasificaciones, logros y sincronización | Ejecución del servicio solicitado, artículo 6.1.b) del RGPD |
| Almacenamiento local seudonimizado de información de otros jugadores | Interés legítimo en garantizar la correcta visualización de las clasificaciones, artículo 6.1.f) del RGPD |
| Gestión de las compras dentro de la Aplicación | Ejecución de un contrato, artículo 6.1.b) del RGPD |
| Prevención de errores, procesamiento duplicado y abusos | Interés legítimo en garantizar la seguridad y el correcto funcionamiento del servicio, artículo 6.1.f) del RGPD |
| Comprobación de la versión y los ajustes de la Aplicación | Ejecución del servicio solicitado, artículo 6.1.b) del RGPD |
| Tratamientos publicitarios que requieren consentimiento | Consentimiento del interesado, artículo 6.1.a) del RGPD |
| Otros tratamientos publicitarios permitidos por la normativa aplicable | Bases jurídicas indicadas por los proveedores, incluido, cuando corresponda, el interés legítimo conforme al artículo 6.1.f) del RGPD |
| Asistencia a los usuarios | Ejecución del servicio o interés legítimo en gestionar las solicitudes, artículos 6.1.b) y 6.1.f) del RGPD |
| Cumplimiento de obligaciones legales | Obligación legal, artículo 6.1.c) del RGPD |
| Formulación, ejercicio o defensa de reclamaciones | Interés legítimo, artículo 6.1.f) del RGPD |

Cuando el tratamiento se base en el consentimiento, este podrá retirarse mediante los mecanismos proporcionados por el servicio de gestión de preferencias, sin que ello afecte a la licitud de los tratamientos realizados antes de su retirada.

Cuando el tratamiento se base en el interés legítimo, el interesado podrá ejercer su derecho de oposición en los supuestos previstos en el artículo 21 del RGPD.

## 9. Destinatarios de los datos

El Responsable del tratamiento no vende directamente los datos personales de los jugadores ni mantiene una base de datos destinada a su comercialización.

Los datos podrán ser tratados, cuando sea necesario, por:

- **Apple**, en relación con los servicios Game Center, App Store y StoreKit;
- **Google**, a través de Google Mobile Ads y Google User Messaging Platform, así como por los posibles proveedores publicitarios implicados en la difusión de anuncios;
- El proveedor de **GitHub Pages**, en relación con las solicitudes necesarias para descargar el archivo de configuración público;
- El proveedor del servicio de correo electrónico utilizado para la asistencia;
- Asesores profesionales o autoridades públicas en los casos previstos por la ley.

La información almacenada en la memoria caché local de las clasificaciones no es comunicada por el Responsable del tratamiento a estos destinatarios.

Los tratamientos realizados mediante servicios externos están sujetos a sus respectivas políticas de privacidad y a las condiciones establecidas por la normativa aplicable.

## 10. Transferencias internacionales de datos

El Responsable del tratamiento no gestiona servidores propios destinados al almacenamiento de datos del juego.

El uso de servicios proporcionados por Apple, Google y GitHub puede implicar el tratamiento de datos personales fuera del Espacio Económico Europeo.

Estos tratamientos están sujetos a las condiciones, políticas de privacidad y garantías adoptadas por los respectivos proveedores, de conformidad con las disposiciones aplicables en materia de transferencias internacionales de datos personales.

La información relativa a las transferencias internacionales y a las posibles garantías aplicables podrá solicitarse al Responsable del tratamiento o consultarse en las políticas de privacidad de los proveedores correspondientes.

## 11. Conservación de los datos

El progreso, las preferencias y los demás datos almacenados exclusivamente en el dispositivo se conservan normalmente hasta que se desinstala la Aplicación, salvo las posibles copias conservadas en las copias de seguridad del dispositivo.

La memoria caché local de información de otros jugadores contiene un máximo de **25.000 registros**, sin un plazo de conservación predeterminado. Cuando se supera este límite, se eliminan primero las entradas más antiguas. Normalmente, los datos se eliminan al desinstalar la Aplicación, salvo las posibles copias conservadas en las copias de seguridad del dispositivo.

Las puntuaciones pendientes de sincronización se conservan hasta que se sincronizan, hasta su posible caducidad o hasta que se elimina la Aplicación.

Las preferencias relativas al consentimiento publicitario se gestionan mediante UMP y sus sistemas asociados, de acuerdo con los criterios de conservación aplicables y las condiciones de los proveedores.

Los datos recopilados por los servicios publicitarios son conservados por Google y los demás proveedores que puedan intervenir, conforme a sus respectivas políticas de conservación y a las finalidades aplicables.

Las solicitudes de asistencia se conservan durante el tiempo necesario para atenderlas y, por regla general, durante un período no superior a **24 meses**, salvo que existan obligaciones legales o sea necesario proteger los derechos del Responsable del tratamiento.

La posible documentación administrativa o contable se conserva durante los períodos establecidos por la normativa aplicable.

Los datos gestionados de forma independiente por Apple y otros servicios externos se conservan según los criterios establecidos por los respectivos proveedores.

## 12. Derechos de los interesados

En los supuestos previstos en los artículos 15 a 22 del RGPD, los interesados podrán ejercer sus derechos de acceso, rectificación, supresión, limitación del tratamiento, oposición y portabilidad de los datos.

Las solicitudes podrán enviarse a la dirección de correo electrónico indicada en la sección **Responsable del tratamiento**.

El Responsable del tratamiento no puede acceder de forma remota a los datos almacenados exclusivamente en el espacio de almacenamiento local de la Aplicación. La desinstalación de la Aplicación normalmente implica la eliminación de los datos presentes en su contenedor local, salvo las posibles copias conservadas en las copias de seguridad del dispositivo.

Las solicitudes relativas a información seudonimizada de otros jugadores, almacenada localmente en los dispositivos de los usuarios, se evaluarán teniendo en cuenta las posibilidades técnicas de identificación e intervención sobre los datos correspondientes, respetando los derechos establecidos por la normativa aplicable.

Las preferencias relativas al consentimiento publicitario pueden gestionarse mediante la función **Preferencias de anuncios**, disponible en los ajustes de la Aplicación cuando corresponda.

Para los datos gestionados de forma independiente por Game Center, la App Store u otros servicios de Apple, los interesados podrán utilizar las herramientas proporcionadas por Apple. Del mismo modo, para los tratamientos realizados por proveedores publicitarios, podrán utilizarse sus respectivas herramientas de gestión de la privacidad.

Los interesados también tienen derecho a presentar una reclamación ante la **Autoridad Italiana de Protección de Datos (Garante per la protezione dei dati personali)**, de conformidad con el artículo 77 del RGPD.

## 13. Menores de edad

Girostella no requiere que los usuarios proporcionen datos de identidad civil y no ofrece funciones de chat, mensajería ni herramientas que permitan publicar contenidos libremente.

El uso de Game Center, la App Store y las compras por parte de menores está sujeto a los ajustes de la cuenta de Apple, las funciones familiares y las restricciones proporcionadas por Apple.

Cualquier tratamiento de datos publicitarios relativos a menores está sujeto a las restricciones establecidas por la normativa aplicable y a la configuración adoptada por los servicios publicitarios utilizados por la Aplicación.

Si el Responsable del tratamiento recibe, a través del servicio de asistencia, datos personales de un menor que no sean necesarios para atender la solicitud, dichos datos se eliminarán cuando no existan otros motivos legítimos para conservarlos.

## 14. Seguridad, elaboración de perfiles y decisiones automatizadas

Los datos locales de la Aplicación se almacenan dentro del entorno aislado («sandbox») proporcionado por iOS.

La Aplicación utiliza, cuando corresponde, identificadores seudonimizados para limitar el almacenamiento de información directamente atribuible a otros jugadores.

Las comunicaciones con Game Center y la App Store utilizan los frameworks y sistemas de seguridad proporcionados por Apple.

El Responsable del tratamiento adopta medidas razonables y proporcionadas para proteger los datos personales frente al acceso no autorizado, la pérdida o la alteración.

Girostella no elabora de forma autónoma perfiles publicitarios de los jugadores ni adopta decisiones automatizadas que produzcan efectos jurídicos o efectos significativamente similares sobre los usuarios en el sentido del artículo 22 del RGPD.

Los proveedores publicitarios pueden tratar datos para la selección, personalización o medición de anuncios, de acuerdo con las finalidades y bases jurídicas aplicables.

## 15. Modificaciones de esta política de privacidad y contacto

La presente política de privacidad podrá actualizarse en caso de modificaciones de la Aplicación, de los servicios utilizados o de la normativa aplicable.

La versión actualizada se publicará en la misma dirección e indicará su fecha de actualización. En caso de cambios importantes, podrá mostrarse un aviso dentro de la Aplicación.

Para solicitar información, presentar consultas o ejercer los derechos relacionados con la protección de datos personales:

**[alessandro_penna@icloud.com](mailto:alessandro_penna@icloud.com)**