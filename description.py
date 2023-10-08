Instruction_uploading_database = """
            1. **Database Name**:
            - Enter the name of the database where the table will be saved. If a database with the same name already exists, it will be replaced.

            2. **Table Names**:
            - List the names of the tables you would like to save. You can save multiple tables at once by separating them with commas.

            3. **Table Schemas**:
            - Add the schema for each individual table. Each schema should be provided as a dictionary. Use commas to separate different schemas for different tables.

            4. **File Upload**:
            - Upload the respective files. Accepted file types include: CSV, XLS, XLSX, XLSM, XLSB.

            5. **Processing**:
            - Click on "Process File" to begin the operation.

        """

Instruction_loading_database = """
        1. **Database Location**:
        - The database should be located in the same path as the `app.py` file and should have a `.sqlite` extension.

        2. **Selecting a Database**:
        - First, select a database from the database drop-down menu. Afterward, a list of tables will be displayed, which you can query.

        """


App_description = """
        # Text2SQL Database Query Tool

        **Description:**

        Text2SQL Database Query Tool is a user-friendly web application that simplifies database management and SQL querying. With this app, you can effortlessly create and manage SQLite databases, upload and process data from various file formats (e.g., CSV, Excel), and execute SQL queries without writing a single line of SQL code.

        **Key Features:**

        1. **Database Creation:** Easily create SQLite databases with a user-defined name. If a database with the same name already exists, it will be replaced.

        2. **Table Management:** Define table names and schemas using a simple interface. You can create multiple tables and specify column data types effortlessly.

        3. **Data Upload:** Upload data files in CSV, Excel (XLS, XLSX, XLSM, XLSB) formats. The app supports multiple file uploads.

        4. **SQL Querying:** Seamlessly execute SQL queries by typing them in the chat interface. The app uses Langchain and OpenAI to understand and respond to your queries.

        5. **Database Loading:** Connect to pre-existing databases located in the same directory as the app. You can select a database and query its tables.

        Text2SQL Database Query Tool is a powerful yet user-friendly solution for managing and querying databases, making it ideal for both beginners and experienced users.

        Explore the app and simplify your database tasks today!

        """

todo_warning = """
        **To-Do List**
        1.  Fix the loading dataset problem: Change the prompt so that it includes the table name as input. This will make the model more focused.

        2.  Add the functionality to output a table: Instead of a descriptive explanation when required.

        3.  Add the functionality to visualize the data: Using simple plots.

        4.  Add the functionality to hook up to a web-based database.

        5.  Implement a better output parser/prompt: To avoid LLM hallucination.

        **Warning**
        1.  Cost Warning: The cost will stack quickly because we run an agent, and the token limit can be reached very fast.

        2.  Token Limit: You could use LLM available on Hugging Face, but it has a very small token limit.                 
        """