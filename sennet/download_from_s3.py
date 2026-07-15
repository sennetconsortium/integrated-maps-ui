#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
import json
import os


def set_access_keys(access_key_id, secret_access_key):
    os.system(f'aws configure set aws_access_key_id "{access_key_id}"')
    os.system(f'aws configure set aws_secret_access_key "{secret_access_key}"')


def download_s3_file(file, uuid):
    bucket_path = f"s3://sn-data-products/{uuid}/"
    os.system(
        f'aws s3 cp "{bucket_path}{file}" /opt/pipeline_outputs/"{file}"'
    )


def download_s3_files(file_list, uuid):
    for file in file_list:
        if file:
            download_s3_file(file, uuid)


def download_shiny(uuid):
    bucket_path = f"s3://sn-data-products/{uuid}/shiny/"
    os.system(f'aws s3 cp "{bucket_path}" "/opt/shiny-server/{uuid}/" --recursive')


def main(
    uuid,
    assay,
    access_key_id,
    secret_access_key,
):
    set_access_keys(access_key_id, secret_access_key)
    metadata = f"{uuid}.json"
    if assay == "rna":
        umap = f"{uuid}.png"
        download_shiny(uuid)
    elif assay == "multiome":
        umap = f"{uuid}_leiden_cluster_combined.png"
    else:
        umap == None
    file_list = [metadata, umap]
    download_s3_files(file_list, uuid)


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("uuid", type=str)
    p.add_argument("assay", type=str)
    p.add_argument("access_key_id", type=str)
    p.add_argument("secret_access_key", type=str)
    args = p.parse_args()

    main(
        args.uuid,
        args.assay,
        args.access_key_id,
        args.secret_access_key,
    )
