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
        download_s3_file(file, uuid)


def download_shiny(uuid):
    bucket_path = f"s3://sn-data-products/{uuid}/shiny/"
    os.system(f'aws s3 cp "{bucket_path}" "/opt/shiny_server/{uuid}/" --recursive')


def get_uuid(metadata_json):
    with open(metadata_json) as json_file:
        metadata = json.load(json_file)
    uuid = metadata["Data Product UUID"]
    return uuid


def main(
    uuid,
    access_key_id,
    secret_access_key,
):
    set_access_keys(access_key_id, secret_access_key)
    metadata = f"{uuid}.json"
    umap = f"{uuid}.png"
    file_list = [metadata, umap]
    download_s3_files(file_list, uuid)
    download_shiny(uuid)


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("uuid", type=str)
    p.add_argument("access_key_id", type=str)
    p.add_argument("secret_access_key", type=str)
    args = p.parse_args()

    main(
        args.uuid,
        args.access_key_id,
        args.secret_access_key,
    )