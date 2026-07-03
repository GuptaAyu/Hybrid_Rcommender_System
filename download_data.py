import os
from huggingface_hub import hf_hub_download

FILES = [
    "cleaned_data.csv",
    "collab_filtered_data.csv",
    "interaction_matrix.npz",
    "track_ids.npy",
    "transformed_data.npz",
    "transformed_hybrid_data.npz"
]

REPO_ID = "AyuGupta08/spotify-hybrid-data"


def download_dataset():
    os.makedirs("data", exist_ok=True)

    for file in FILES:
        local_path = os.path.join("data", file)

        if os.path.exists(local_path):
            print(f"{file} already exists.")
            continue

        print(f"Downloading {file}...")

        downloaded_file = hf_hub_download(
            repo_id=REPO_ID,
            repo_type="dataset",
            filename=file
        )

        # Copy the downloaded file into data/
        with open(downloaded_file, "rb") as src:
            with open(local_path, "wb") as dst:
                dst.write(src.read())

    print("All files downloaded successfully.")


if __name__ == "__main__":
    download_dataset()