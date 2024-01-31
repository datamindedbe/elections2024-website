# script to populate setup the chromadb data and populate it
# once off script
import glob
import pathlib
from src.vector_store import VectorCollection
from src.aws import list_s3_files, read_txt_from_s3

from config import AGREEMENTS_PATH, DECISIONS_S3_BUCKET, DECISIONS_S3_PREFIX_CLEAN

# set these flags to true to re-/initialize the vector collections from scratch
# note that this will take a while
REPROCESS_AGREEMENTS = False
REPROCESS_DECISIONS = False

if REPROCESS_AGREEMENTS:
    agreements_collection = VectorCollection(name="agreements", metadata={"hnsw:space": "cosine"})
    print("Adding agreements")
    for id_n, txtfile in enumerate(glob.glob(AGREEMENTS_PATH+'*.txt')):
        with open(txtfile) as f:
            data = f.read()
        filepath = pathlib.Path(txtfile)
        print(f"Processing {filepath.stem}")

        agreements_collection.add_item(
            document=data,
            metadata={"source": "regeerakkoord2019"},
            id=f"{txtfile}" #use the name of the file as it id
        )

if REPROCESS_DECISIONS:
    decisions_collection = VectorCollection(name="decisions", metadata={"hnsw:space": "cosine"})
    file_list = list_s3_files(bucket_name=DECISIONS_S3_BUCKET, prefix=DECISIONS_S3_PREFIX_CLEAN)
    print(file_list[:10])
    print(f"{len(file_list)} cleaned files on s3 to embed")
    for file_key in file_list:
        if file_key.endswith('.txt'):
            contents = read_txt_from_s3(DECISIONS_S3_BUCKET, file_key)
            filepath = pathlib.Path(file_key)
            print(f"Processing {filepath.stem}")
            if contents:
                decisions_collection.add_item(
                    document=contents,
                    metadata={"source": "besluiten"},
                    id=f"{file_key}"
                )