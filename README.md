# shopping-cart
Integração do banco MongoDB para o projeto shopping-cart do LuizaCode

## libs
* motor = Driver Python assíncrono para MongoDB
* pydantic = Validação de dados para Python 

## Environment
| name_env | value |
|------------|------------|
|DATABASE_URI|connection string Atlas|

## Install
* Create venv
    ```
    $ virtualenv venv --python=3.10
    ```
    Linux
    ```
    $ source venv/bin/activate
   ```
   Windows
    ```
    $ .\venv\Scripts\activate
   ```
* Install requirements
     ```
     $ pip install -r requirements.txt
     ```
* Run
  ```
  $ python main.py
   ```
  
