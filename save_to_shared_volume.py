def df__save_to_shared_volume(df, file_name: str, workspace_name: str = "default", dataset_type: str = "scoring"):

    directories = {
        "scoring": "prediction",
        "training": "training"
    }

    directory = directories[dataset_type]

    if not len(file_name):
        file_name = workspace_name
        if dataset_type == "training":
            from datetime import datetime
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_name = f"{file_name}-{now}"

    if not file_name.endswith(".csv"):
        file_name = f"{file_name}.csv"


    if dataset_type == "scoring":
        from datetime import datetime
        now = datetime.now().strftime("%Y-%m-%d")
        directory = f"{directory}/{now}"

    path = f"dataroot/projects/{workspace_name}/datasets/{directory}/{file_name}"


    from optimus.helpers.functions import path_is_local, prepare_path_local
    if path_is_local(path):
        prepare_path_local(path)

    df.save.csv(path)
    return df