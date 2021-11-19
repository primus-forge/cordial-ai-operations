def df__save_for_scoring(df, file_name: str, workspace_name: str = "default"):

    if not len(file_name):
        file_name = df.meta.get("file_name", workspace_name)

    if not file_name.endswith(".csv"):
        file_name = f"{file_name}.csv"

    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d")

    import os
    instance = os.getenv('INSTANCE_NAME')

    path = f"/Data/{instance}/dataroot/projects/{workspace_name}/datasets/prediction/{now}/{file_name}"


    from optimus.helpers.functions import path_is_local, prepare_path_local
    if path_is_local(path):
        prepare_path_local(path)

    df.save.csv(path)
    return df
