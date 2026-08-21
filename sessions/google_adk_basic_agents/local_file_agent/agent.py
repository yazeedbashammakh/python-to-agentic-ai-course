
from google.adk.agents import Agent
from local_file_agent.file_manage_tools import list_files_in_directory, read_file_contents, write_file_contents


root_agent = Agent(
    name="knowledge_assistant",
    model="gemini-2.5-flash",
    instruction=(
        "You are my knowledge assistant. Whatever information I provide to you, you summarise it, structure it and then place in local files in markdown format a well structured manner." 
        "Maintain one file which is like content index file, which contains the list of all files and their content summaries."
        "Always make sure to update the content index file whenever you create or modify any files."
        "Before searching all the files, always check the content index file to find the most relevant files to search in."
        "Use the list_files_in_directory, read_file_contents, write_file_contents tools to interact with local files when asked. "
        "Always provide clear and concise information about the file operations."
    ),
    tools=[read_file_contents, write_file_contents, list_files_in_directory]
)

