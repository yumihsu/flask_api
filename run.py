# utf-8

from app import  app

@app.route('/')
def index():
    return "Falsk API Started"

if __name__=='__main__':
    app.run(host = '0.0.0.0' , port = '3000' , debug = False)
