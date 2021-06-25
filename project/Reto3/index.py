# Una famosa empresa de zapatos tiene una fanpage en facebook en donde publica todos los días posts con 
# promociones, su nivel de engagement es muy alto , pero los seguidores de la página no mucho. Ellos desean 
# un script el cual les permita invitar a las personas que le den like a su página solo si estos  han reaccionado 
# o comentado algunas de sus publicaciones en facebook.

# Las entradas del script serán las credenciales de la página y el link del posts, ejemplo de ejecución:
# python tucodigo.py user password link

import facebook as fb
import requests

access_token = "EAAMjNJCrfQYBADyA3MkzPYNRYAKAaEKtIbb81Cfi3D3ZAmQWjnH7iZCCWshcv4wMzAiYoH5nkqQizX5AxfQ6UmmFZCEgnaVAOfgncqTzkGoLwQ3ZCvA6Nn37qxNRTKzjA1kCA2UoUKDPNoLDj5iifsZBeypDXtb2CmQ85HltUiBWCx90ZCVHP1EklqQfJXsCLWrrZCugqSuDZBmSDHI0Wb64oqXYImvh89WSlASHWSVt4vZAAM32f44cj"

graph = fb.GraphAPI(access_token)
commentsIds = []
# url = www.facebook.com/universidadespiritusanto/posts/10159326471941670

comments = graph.get_connections(id="109354584316946_222156086370128", connection_name="comments")

for comment in comments["data"]:
    commentsIds.append(comment["id"])
# comments = graph.get_object(id="109354584316946_222156086370128")

url = "https://graph.facebook.com/109354584316946_222156086370128/feed?fields=message,comments.limit(10).summary(true){message,from,likes.limit(0).summary(true)}&access_token="+access_token+"/"
data = requests.get(url).json()

print(commentsIds) 
print(data)


