# Import
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Initialize the FastAPI
app = FastAPI()


# Adding Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")






# Route - '/'
# Method - GET
# An Home route for basic checks
@app.get("/")
def read_root():
    return {"message": "Hello from Sujay"}





# Route - '/upload/'
# Method - POST
# To upload the selected column csv file 
@app.post("/upload/")
async def upload_csv(file: UploadFile):
    try:
        # Read the compressed data from the uploaded file
        csv_data = await file.read()
        csv_string = csv_data.decode('utf-8')

        # Read the CSV data into a DataFrame
        df = pd.read_csv(StringIO(csv_string))

        # Data Processing - Null Values (A type of Filter)
        df = df.drop(0,axis=0)
        df = df.drop(len(df),axis=0)
        df = df.dropna(axis=1)
        print(df)
        df = df.astype('int')
        numeric_columns = df.select_dtypes(include=[float, int])
        integer_columns = df.select_dtypes(include=[int])

        # Conditions for Plotting
        if numeric_columns.empty:
            return {"error": "No numeric columns found in the CSV data."}
        sns.pairplot(data=df, vars=integer_columns.columns)
        plt.title("Pair Plot of Integer Columns")
        plt.savefig("assets/images/pair_plot.png")
        return {"columns": 'Received Thank You'}

    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the CSV file."}
