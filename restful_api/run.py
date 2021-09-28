from app import app

@app.route('/')
def index():
    return "restful_api_start"

if __name__=='__main__':
    app.run(host = '0.0.0.0' , port = '4000' , debug = True )
