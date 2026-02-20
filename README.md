

sudo systemctl start postgresql

cd project/perp

python3 -m venv venv

source venv/bin/activate

uvicorn app.main:app --reload --port 8081

( we are using port 8081 because 8080 is being used by postgresql)

visit : (http://127.0.0.1:8081/docs)
