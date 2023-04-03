from website import create_app

#check for bitly thing...


app = create_app()

# @app.route('/')
# def home():
#     return {"name":"apoorv"}


if __name__=="__main__":
    app.run(debug=True)