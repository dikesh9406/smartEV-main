from app import app, create_tables

create_tables()
@app.route('/')
def home():
    return "Hello, Flask!"
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    # app.run(debug=True)