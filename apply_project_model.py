import requests
import json

def df__apply_project_model(df, cols="*", output_col: str = "new_col", project_json_path: str = None):

    if project_json_path.startswith("http"):
        project_json = requests.get(project_json_path).json()
    else:
        with open(project_json_path, "r") as f:
            project_json = json.load(f)

    model_path = project_json.get("fullModelPath")
    model = op.load.model(model_path)

    cols = df.cols.names(cols)
    new_df = df.cols.select(cols)
    
    new_df = model.predict_proba(new_df, output_col=output_col)

    return new_df