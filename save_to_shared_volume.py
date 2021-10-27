def df__save_to_shared_volume(df, file_name: str, workspaceName: str = "default", dataset_type: str = "scoring"):

    dataset_types = {
        "scoring": "prediction",
        "training": "training"
    }

    dataset_type = dataset_types[dataset_type]

    if not len(file_name):
        import uuid
        file_name = f"dataset-{str(uuid.uuid4())}.csv"

    if not file_name.endswith(".csv"):
        file_name = f"{file_name}.csv"

    path = f"dataroot/projects/{workspaceName}/datasets/{dataset_type}/{file_name}"

    from optimus.helpers.functions import path_is_local, prepare_path_local
    if path_is_local(path):
        prepare_path_local(path)

    df.save.csv(path)
    return df