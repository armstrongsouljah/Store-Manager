from flask import Blueprint

bp = Blueprint('api', __name__)  # needed to enable versioning of my api


welcome_message = """
   <!DOCTYPE html>
     <html>
       <head>
         <title>Store Manager API</title>
         <style type='text/css'>
           *{
               margin:0;
               padding:0;
           }
           body{
               width:80%;
               margin:0 auto;
           }
           .main-container{
               margin-top:45px;
           }
           h2{
               font-size:16pt;
               color:orange;
               text-align:center;
           }
           a{
               text-decoration:none;
           }
         </style>
       </head>
       <body>
         <div class='main-content'>
           <h2>Store Manager</h2>
              Currently supported endpoints <br>
              <a href='/api/v1/products'>products</a>
         </div>
       </body>
     </html>
"""
