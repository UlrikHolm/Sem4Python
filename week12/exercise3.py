import re


# Lav en flask server, hvor du åbner minimum 2 endpoints:
# - GET : returner data omkring antallet af crimes i en given periode 
# (giv to datoer med som query-param i URL'en)
# - POST : returner den totale mængde af "burglaries" i januar, men returner kun data, 
# hvis request.body indeholder et json objekt med key-value {"key":"secret"}

