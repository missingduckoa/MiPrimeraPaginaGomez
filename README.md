# TuPrimeraPagina+Gomez

## Descripción
Este es un proyecto web desarrollado en Django que incluye herencia de plantillas, modelos y formularios.Aunque originalmente debía ser un blog (según entendí, esto era opcional), decidí enfocarlo en una página web cuyo objetivo es facilitar la adopción, publicación y solicitud de mascotas.

## NOTA IMPORTANTE
Le di más prioridad a la funcionalidad que al diseño visual. Por algunos errores que cometí y que, si los corrijo ahora, podrían causar conflictos, preferí dejarlos tal como están. La interfaz se ve completa, pero puede que hayan modelos de los que no hice uso, son adicionales/código adicional. 

## Cómo probar el proyecto
1. Abra GitBash o la terminal de su preferencia y ejecute
    git clone https://github.com/missingduckoa/MiPrimeraPaginaGomez.git
2. Cree y active el entorno virtual 
    python -m venv env (para crearlo)
    .\env\Scripts\activate (para activarlo)
3. Instale las dependencias
    pip install
----------------------- -------
asgiref                 3.8.1
asttokens               3.0.0
colorama                0.4.6
decorator               5.2.1
Django                  5.2
django-extensions       4.1
executing               2.2.0
ipython                 9.1.0
ipython_pygments_lexers 1.1.1
jedi                    0.19.2
matplotlib-inline       0.1.7
parso                   0.8.4
pip                     24.3.1
prompt_toolkit          3.0.51
pure_eval               0.2.3
Pygments                2.19.1
sqlparse                0.5.3
stack-data              0.6.3
traitlets               5.14.3
tzdata                  2025.2
wcwidth                 0.2.13
4. Antes de correr el servidor, aplique las migraciones
    python manage.py migrate
5. Finalmente, ejecute el servidor
    python manage.py runserver
    6. Deberia poder entrar a él mediante el siguiente: http://127.0.0.1:8000/

## Pruebe las funcionalidades del proyecto
 Usá los botones de la página para:
- Adoptar mascotas.
- Publicar mascotas en adopción.
- Solicitar adopciones.

# AUTOR
Proyecto realizado por: Sofia Gomez
