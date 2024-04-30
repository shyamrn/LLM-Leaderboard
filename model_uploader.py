from huggingface_hub import HfApi

username = "shyamieee"
modelname = "Maverick-v2.0"

api = HfApi(token="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")

api.create_repo(
    repo_id=f'{username}/{modelname}',
    repo_type="model"
)

api.upload_folder(
    repo_id=f'{username}/{modelname}',
    folder_path="generated models/maverick_v2_folder"
)
