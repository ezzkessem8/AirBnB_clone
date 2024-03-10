# AirBnB_clone

This is a simplified version of the AirBnB application backend, also known as "HBNB". It's designed to be a lightweight version of the real Airbnb application, focusing on the backend data model and storage. It includes a command-line interface (CLI) for interacting with the data.
README.md

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your_username/AirBnB_clone.git
   ```
2. Run the console:
   ```bash
   ./console.py
   ```
Using the Command Interpreter
The command interpreter allows you to interact with the data models using various commands. Here are some basic commands you can use:

-create: Create a new instance of a class
show: Show details of a specific instance
-destroy: Delete a specific instance
-all: Show details of all instances of a class
-update: Update attributes of a specific instance

## Examples 
  ```bash
(create) BaseModel
(show) BaseModel 1234-1234-1234
(destroy) BaseModel 1234-1234-1234
(all) BaseModel
(update) BaseModel 1234-1234-1234 name "New Name"
  ```
