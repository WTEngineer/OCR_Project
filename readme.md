## Building the Executable

To build the executable for the backend server using PyInstaller, follow these steps:

1. Ensure you have PyInstaller installed. If not, you can install it using pip:

```sh
pip install pyinstaller
```

2. Navigate to the directory containing the `server.py` file:

```sh
cd ./server
```

3. Run PyInstaller to create the executable:

```sh
pyinstaller --onefile server.py
```

4. The executable will be created in the `dist` directory within the `server` directory.

5. You can now run the executable from the `dist` directory:

```sh
./dist/server
```

This process will package your backend server into a standalone executable that can be easily distributed and run on other systems.

## Setting Up the Frontend

To set up the frontend using Electron, follow these steps:

1. Ensure you have Node.js and npm installed. If not, you can download and install them from [Node.js official website](https://nodejs.org/).

2. Navigate to the directory containing your Electron project:

```sh
cd /path/to/electron/project
```

3. Install the necessary dependencies:

```sh
npm install
```

4. Start the Electron application:

```sh
npm start
```

This process will set up and run your Electron-based frontend application.

## Combining Backend and Frontend

To combine the backend and frontend, you need to ensure that the backend server is running and accessible by the frontend application. You can start the backend server executable and then run the Electron application as described above.

1. Start the backend server executable:

```sh
./server/dist/server
```

2. In a new terminal, navigate to your Electron project directory and start the frontend:

```sh
cd /path/to/electron/project
npm start
```

Your Electron frontend should now be able to communicate with the backend server.
