def df__save_for_training(df, file_name: str, project_name: str = "default"):

    if not len(file_name):
        file_name = df.meta.get("file_name", project_name)

    # from datetime import datetime
    # now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # file_name = f"{file_name}-{now}"

    if not file_name.endswith(".csv"):
        file_name = f"{file_name}.csv"

    file_name = file_name.split("://")[-1]

    import os
    instance = os.getenv('INSTANCE_NAME')

    path = f"/Data/{instance}/dataroot/projects/{project_name}/datasets/training/{file_name}"

    from optimus.helpers.functions import path_is_local, prepare_path_local
    if path_is_local(path):
        prepare_path_local(path)

    df.save.csv(path)
    return df
