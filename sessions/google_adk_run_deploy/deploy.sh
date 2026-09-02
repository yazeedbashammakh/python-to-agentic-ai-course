
# Set your Google Cloud Project ID
export GOOGLE_CLOUD_PROJECT="<your_project_id>" # Replace with your actual project ID

# Set your desired Google Cloud Location
export GOOGLE_CLOUD_LOCATION="us-central1" # Example location

# Set the path to your agent code directory
export AGENT_PATH="./tutor_agent" # Assuming capital_agent is in the current directory

# Set a name for your Cloud Run service (optional)
export SERVICE_NAME="tutor_agent-service"

# Set an application name (optional)
export APP_NAME="tutor_agent_app"


adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--with_ui \
$AGENT_PATH
