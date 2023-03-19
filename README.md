# travel-insurance-pricing-calculator

## Setup Instruction
1. Clone the repo to your local machine
2. Open the folder in VSCode or any editor you prefer
### 1. Backend
1. Change directory to the `/backend` folder by running `cd /backend` command
2. Switch to your preferred Python 3 interpreter. 
3. Install dependencies by running `pip3 install -r requirements.txt` command
4. Run the server locally by running `uvicorn src.main:app --reload` command
5. Backend is using the `8000` port, located at `http://localhost:8000`
### 2. Frontend
1. Change directory to the `/frontend` folder by running `cd /frontend` command if you are at the root(`/`), run `cd ../frontend` if you are at the `/backend` directory
2. Install dependencies by running `npm install` command
3. Run the web app locally by running `npm run dev` command
4. Backend is using the `5173` port, located at `http://localhost:5173`

### Improvements to be done
- Write test cases to validate the premium calculation
