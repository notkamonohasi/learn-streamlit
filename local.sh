docker build -f ./Dockerfile-streamlit -t streamlit-test .
docker run -p 8080:8080 --env-file .env.local streamlit-test
