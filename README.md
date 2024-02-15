markdown
# Build Planner

## Summary
Build Planner is a web application that allows users to create building plans using annotations and shapes.

## Tech Stack Used

### Backend
- **Python Flask**: A lightweight web framework that is easy to use. While it lacks inbuilt tools, it can be compensated with external tools. Generally preferred to make Proof of Concepts (PoCs).
- **MongoDB**: Chosen for its ability to handle complex shape data. With each shape, parameters can be changed, and the application doesn't have heavy relationships. Using a NoSQL database like MongoDB is the best choice from both the developer experience and scalability perspectives. Backend and other data records will not be affected if more different shapes are added in the future. MongoDB is also scalable.

### Frontend (not the best)
- **HTML**
- **Canvas**: Utilized for drawing shapes on the web page.
- **JavaScript**: While Vue.js was suggested, the developer has used Canvas for the first time and is familiar with JavaScript. Vue.js or React.js could be considered for future improvements.

## Tests
- **Unittest**: Default testing framework for Python.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Change MongoDB connection link:**
   Replace `<mongo_connection_link>` with your MongoDB connection link in the `src/__init__.py` file (already have included remote db link for easy testing please don't miss use).

4. **Run the application:**
   ```bash
   python run.py
   ```

## Deployment

1. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Run Gunicorn:**
   ```bash
   gunicorn -b 0.0.0.0:8000 src.app:application
   ```
   This assumes that your Flask application object is named `application` and located in the `src` directory, and it will run on port 8000. Adjust the command according to your actual setup.

These commands should help you get started with running your Flask application and deploying it using Gunicorn. Adjust them based on your specific project structure and requirements.
```
