# Text2SQL, A Sql-free-interaction-with-structure-data

Text2SQL Database Query Tool is a user-friendly web application for SQL querying. With this app, you can effortlessly create and manage SQLite databases, upload and process data from various file formats (e.g., CSV, Excel), and execute SQL queries without writing a single line of SQL code.

Explore the app and simplify your database tasks today!
## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [To-Do/Warnings](#To-Do/Warnings)
- [Contributing](#contributing)
- [License](#license)
- [Reference](#reference)

## Demo
A demo of the application:





## Features
- **Natural Language Interaction:** Users can communicate with the application using natural language, simplifying the interaction process.
- **Multi-File Format Support:** The application can handle various file formats, making it versatile for different data sources. Accepted file types include: CSV, XLS, XLSX, XLSM, XLSB.
- **Database Creation:** Users can create and save databases from their input.
- **Pre-Existing Database Integration:** The application supports the use of pre-existing .sqlite databases, allowing users to work with their existing data.
- **LangChain Agent:** The heart of the application, the LangChain Agent, is composed of several key components, including agents, tools, toolkits, and an agent executor. An agent is a component that has access to a suite of tools and can decide which tool to use based on the user's input. We used an "Action Agents", which is suitable for small tasks.


## How It Works
**Instruction for uploading file/creating database**:

            1. Database Name:
            - Enter the name of the database where the table will be saved. If a database with the same name already exists, it will be replaced.

            2. Table Names:
            - List the names of the tables you would like to save. You can save multiple tables at once by separating them with commas.

            3. Table Schemas:
            - Add the schema for each individual table. Each schema should be provided as a dictionary. Use commas to separate different schemas for different tables.

            4. File Upload:
            - Upload the respective files. Accepted file types include: CSV, XLS, XLSX, XLSM, XLSB.

            5. Processing:
            - Click on "Process File" to begin the operation.

**Instruction for loading a database**:

            1. Database Location:
            - The database should be located in the same path as the `app.py` file and should have a `.sqlite` extension.

            2. Selecting a Database:
            - First, select a database from the database drop-down menu. Afterward, a list of tables will be displayed, which you can query.


## Getting Started

### Prerequisites
- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [langchain](https://docs.langchain.com/docs/)

### Installation
1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/PC-FSU/text2Sql.git

2. Change to the project directory:

   ```bash
      cd text2Sql

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
   
4. Rename .my_env file to .env. Add your open API key (Huggingface key(optional)) to .env file.

   
### Usage

1. Run the Streamlit app:

   ```bash
      streamlit run app.py

2. Open a web browser and navigate to the local URL provided by Streamlit (e.g., http://localhost:8501).

3. Upload files, table name, and table schema. For more information read [How It Works](#how-it-works)

4. Chat with the AI chatbot by entering your query in the chat input.


### To-Do/Warnings.
**To-Do**:

        1.  Fix the loading dataset problem: Change the prompt so that it includes the table name as input. This will make the LLM model more focused.

        2.  Add the functionality to output a table, instead of a descriptive explanation when required.

        3.  Add the functionality to visualize the data: Using simple plots.

        4.  Add the functionality to hook up to web-based databases.

        5.  Implement a better output_parser/input_prompt: To avoid LLM hallucination.

**Warning**:

        1.  Cost Warning: The cost will stack quickly because we run an agent, and the token limit can be reached very fast.

        2.  Token Limit: You could use LLM available on Hugging Face, but it has a very small token limit.

        3.  This is very basic app. Please use with caution. It needs brainstorming and more feature to provide consistent result.                
       

### Contributing
Contributions are welcome! If you have any ideas, enhancements, bug fixes, or feature requests, please open an issue or submit a pull request.

## License

The Text2SQL App is released under the [MIT License](https://opensource.org/licenses/MIT).

## Reference
