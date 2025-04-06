PROJECT_ID=streamlit-test-456006
STAGE=${1}
PROJECT_NAME=streamlit-test-${STAGE}
ENV_FILE=".env.local"

TAG=gcr.io/${PROJECT_ID}/${PROJECT_NAME}

if [ "$STAGE" = "prod" ]; then
    ENV_FILE=".env.prod"
elif [ "$STAGE" = "dev" ]; then
    ENV_FILE=".env.local"
else
    echo "stage $STAGE is invalid"
    exit 1
fi

get_env_vars() {
    if [[ ! -f "$ENV_FILE" ]]; then
        echo "Error: $ENV_FILE not found!" >&2
        return 1
    fi
    grep -v '^#' "$ENV_FILE" | xargs | sed 's/ /,/g'
}

gcloud config set project ${PROJECT_ID}
gcloud services enable run.googleapis.com
gcloud auth configure-docker

# macでbuildするときは--platform=linux/amd64が必須
docker build -f ./Dockerfile-streamlit --platform=linux/amd64 -t ${TAG} .

docker push ${TAG}
gcloud run deploy ${PROJECT_NAME} \
    --image ${TAG} \
    --platform managed \
    --region asia-northeast1 \
    --allow-unauthenticated \
    --set-env-vars=$(get_env_vars)
