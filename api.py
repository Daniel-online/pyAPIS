from flask import Flask, render_template, request, redirect

app = Flask ("__name__")

stores = [
         {
             "name": "Loja 1",
             "item": [{"nome": "frios", "preco":10.5},{"nome": "embalados", "preço":20.45}, {"nome": "legumes", "preco":5}]
             },
         {
             "name": "Loja 2",
             "item": [{"nome": "assados", "preco":22}]    
             }
         ]
    
@app.get('/stores')
def get_stores():
  return {"stores": stores}
 

