## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Configura las variables de entorno en el archivo `.env`.

2. Ejecuta el script principal:
    ```sh
    python separe.py
    ```

## Contribución

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT.

## Estructura del proeycto

G:.
│   .env
│   test.py
│   get_and_set_env.py
│   get_Data.py
│   get_Date.py
│   clean_Data.py
│   EDA.py
│   clasification_Model.py
│   separe.py
│   svm.py
│   download_kaggle_dataset.py
│   run_cmd_file.py
│   set_api_values.py
│   requirements.txt
│   call_json.py
│   csv_to_sql.py
│   .project
│   sentiment_dfs.db
│   README.md
│
├───__pycache__
│       import_Libraries.cpython-312.pyc
│       api_Call.cpython-312.pyc
│       get_Data.cpython-312.pyc
│       get_Date.cpython-312.pyc
│       clean_Data.cpython-312.pyc
│       EDA.cpython-312.pyc
│       separe.cpython-312.pyc
│       svm.cpython-312.pyc
│       download_kaggle_dataset.cpython-312.pyc
│       set_language.cpython-312.pyc
│       set_api_values.cpython-312.pyc
│       get_and_set_env.cpython-312.pyc
│       call_json.cpython-312.pyc
│       csv_to_sql.cpython-312.pyc
│
├───data
│       news_sentiment_analysis.csv
│       financial_phrase_bank_pt_br.csv
│       df_total.csv
│
├───cmd
│       example.cmd
│       installPortuguese.cmd
│       installEnglish.cmd
│       installSpanish.cmd
│       installChinese.cmd
│       installGerman.cmd
│       isntallItalian.cmd
│       installFranch.cmd
│       installDutch.cmd
│       cmdImportDependences.cmd
│
├───test_phrases
│       en.sh
│       en.json
│       es.json
│       de.json
│       it.json
│       nl.json
│       zh.json
│       pt.json
│       fr.json
│
└───result_data
        dataTraining.csv
        sentiment_dfs.csv
        ControlPanel-Sentimient.pbix
        APiData.csv
        KaggleData.csv


G:.
│   .env
│   test.py
│   get_and_set_env.py
│   get_Data.py
│   get_Date.py
│   clean_Data.py
│   EDA.py
│   clasification_Model.py
│   separe.py
│   svm.py
│   download_kaggle_dataset.py
│   run_cmd_file.py
│   set_api_values.py
│   requirements.txt
│   call_json.py
│   csv_to_sql.py
│   .project
│   sentiment_dfs.db
│   README.md
│
├───__pycache__
│       import_Libraries.cpython-312.pyc
│       api_Call.cpython-312.pyc
│       get_Data.cpython-312.pyc
│       get_Date.cpython-312.pyc
│       clean_Data.cpython-312.pyc
│       EDA.cpython-312.pyc
│       separe.cpython-312.pyc
│       svm.cpython-312.pyc
│       download_kaggle_dataset.cpython-312.pyc
│       set_language.cpython-312.pyc
│       set_api_values.cpython-312.pyc
│       get_and_set_env.cpython-312.pyc
│       call_json.cpython-312.pyc
│       csv_to_sql.cpython-312.pyc
│
├───data
│       news_sentiment_analysis.csv
│
├───cmd
│
├───test_phrases
│       en.sh
│       en.json
│       es.json
│       de.json
│       it.json
│       nl.json
│       zh.json
│       pt.json
│       fr.json
│
└───result_data
        dataTraining.csv
        sentiment_dfs.csv
        ControlPanel-Sentimient.pbix
        APiData.csv
        KaggleData.csv
