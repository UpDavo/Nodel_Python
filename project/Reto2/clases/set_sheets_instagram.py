# Extraer de Instagram TODOS los comentarios del siguiente post:
# https://www.instagram.com/p/B166OkVBPJR/
# Este post tiene alrededor de 1480 comentarios y se deberá extraer
# también los comentarios de los comentarios.
# El dataframe de salida deberá contener los siguientes campos:
# Post,Caption,Date,likesComment,IdFatherComment,IdChildComment,Username
# IdFatherComment es el id de un comentario directo al posts y
# IdChildComment es el id de un comentario hecho sobre otro comentario

from instagram_private_api import Client, ClientCompatPatch
from .google_sheets_test import google_sheets_test
import pandas as pd
import json

user_name = 'nodel_test_2'
password = '12x3x4x5'
media_id = "2124266262036279889_297604134"

instanciaSheets = google_sheets_test("instagram comments")

class set_sheets_instagram:
    def __init__ (self):
        self.user_name = user_name
        self.password = password
        self.media_id = media_id
        self.api = Client(user_name, password)

    def getData(self):
        
        df_template = {
            "post": [],
            "caption": [],
            "date": [],
            "likesComment": [],
            "idFatherComment": [],
            "idChildComment": [],
            "username":[],
        }
        
        results = self.api.media_n_comments(media_id, n=250)

        for objetoBig in results:
        
            likeComments = 0
            childId = 0
            fatherCommentId = self.media_id
            replies = self.api.comment_replies(self.media_id,objetoBig["pk"])   
            
            if "comment_like_count" in objetoBig.keys():
                likeComments = objetoBig["comment_like_count"]
            
            df_template["post"].append(self.media_id)
            df_template["caption"].append(objetoBig["text"])
            df_template["date"].append(objetoBig["created_at"])
            df_template["likesComment"].append(likeComments)
            df_template["idFatherComment"].append(fatherCommentId)
            df_template["idChildComment"].append(objetoBig["pk"])
            df_template["username"].append(objetoBig["user"]["username"])
            
            if len(replies['child_comments']):
                for objetoLow in replies["child_comments"]:
                    
                    if "comment_like_count" in objetoLow.keys():
                        likeComments = objetoLow["comment_like_count"]
                    
                    df_template["post"].append(self.media_id)
                    df_template["caption"].append(objetoLow["text"])
                    df_template["date"].append(objetoLow["created_at"])
                    df_template["likesComment"].append(likeComments)
                    df_template["idFatherComment"].append(objetoBig["pk"])
                    df_template["idChildComment"].append(objetoLow["pk"])
                    df_template["username"].append(objetoLow["user"]["username"])
        
        df = pd.DataFrame(df_template)
        
        
        return [df.columns.values.tolist()]+df.values.tolist()
    
    def ingresarTablaGoogleSheets(self, worksheet, nameWorksheet, dataFrame):
                instanciaSheets.deleteWorksheet(worksheet)
                instanciaSheets.createWorksheet(nameWorksheet)
                instanciaSheets.writeWorksheet(dataFrame, worksheet)
                return "ok"


