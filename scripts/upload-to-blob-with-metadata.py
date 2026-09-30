"""
Upload PDFs from a local folder to an Azure Blob container and set the
metadata fields that the Azure AI Search index expects:

    customMetaTitle   -> AZURE_SEARCH_TITLE_COLUMN / AZURE_SEARCH_FILENAME_COLUMN
    customMetaURL     -> AZURE_SEARCH_URL_COLUMN (public GitHub link for citations)
    customMetaPublic  -> optional flag field in the index

Requirements:
    pip install azure-storage-blob azure-identity
"""

import os
import sys
from urllib.parse import quote

from azure.storage.blob import BlobServiceClient, ContentSettings

# =============================================================================
# CONFIGURATION - replace the placeholder values
# =============================================================================

# Local folder that contains the PDFs to upload
LOCAL_FOLDER = r"C:\\Users\\Anshu.Singh\\Documents\\anshu-9470\\rag-counterfactual-dataset\\pdfs"

# Only files with these extensions are uploaded
ALLOWED_EXTENSIONS = (".pdf",)

# --- Storage authentication (choose ONE) -------------------------------------
# Option A: connection string (leave empty to use Option B)
STORAGE_CONNECTION_STRING = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Option B: Entra ID / managed identity (needs "Storage Blob Data Contributor")
STORAGE_ACCOUNT_NAME = "xxxxxxxxxxx"

# Target container (created if it does not exist)
CONTAINER_NAME = "xxxxxxxxxxxxxxx"

# Optional virtual folder inside the container, e.g. "counterfactual/" ("" = root)
BLOB_PREFIX = ""

# --- Metadata sources ---------------------------------------------------------
# Public GitHub folder where the same PDFs live. Each file's citation URL is
# built as: GITHUB_BASE_URL + "/" + <file name>
GITHUB_BASE_URL = "https://github.com/anshupacific/rag-counterfactual-dataset/blob/main/pdfs"

# Value written to customMetaPublic
META_PUBLIC_VALUE = "true"

# Friendly titles shown in citations. Files not listed here get a title
# generated from the file name (rag_test_world_capitals.pdf -> "World Capitals").
TITLE_OVERRIDES = {
    "rag_test_world_capitals.pdf": "World Capitals Reference Guide",
    "rag_test_famous_landmarks.pdf": "Famous Landmarks Location Guide",
    "rag_test_national_languages.pdf": "National Languages Reference Guide",
    "rag_test_world_currencies.pdf": "World Currencies Reference Guide",
    "rag_test_inventors_inventions.pdf": "Inventors and Inventions Reference Guide",
}

# Overwrite blobs that already exist
OVERWRITE = True

# =============================================================================


def get_service_client() -> BlobServiceClient:
    """Build the BlobServiceClient from a connection string or Entra ID."""
    if STORAGE_CONNECTION_STRING and not STORAGE_CONNECTION_STRING.startswith("<"):
        return BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)

    if STORAGE_ACCOUNT_NAME and not STORAGE_ACCOUNT_NAME.startswith("<"):
        from azure.identity import DefaultAzureCredential

        account_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
        return BlobServiceClient(account_url, credential=DefaultAzureCredential())

    sys.exit("Set STORAGE_CONNECTION_STRING or STORAGE_ACCOUNT_NAME at the top of the script.")


def build_title(file_name: str) -> str:
    """Use the override title, or derive a readable one from the file name."""
    if file_name in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[file_name]
    stem = os.path.splitext(file_name)[0]
    if stem.startswith("rag_test_"):
        stem = stem[len("rag_test_"):]
    return stem.replace("_", " ").replace("-", " ").title()


def build_url(file_name: str) -> str:
    """Build the public GitHub URL for a file (URL-encoded for spaces etc.)."""
    return f"{GITHUB_BASE_URL.rstrip('/')}/{quote(file_name)}"


def build_metadata(file_name: str) -> dict:
    """Metadata keys must match the field names used in the index/skillset."""
    metadata = {
        "customMetaTitle": build_title(file_name),
        "customMetaURL": build_url(file_name),
        "customMetaPublic": META_PUBLIC_VALUE,
    }
    # Blob metadata values must be ASCII
    for key, value in metadata.items():
        if not value.isascii():
            raise ValueError(f"Metadata '{key}' for {file_name} is not ASCII: {value!r}")
    return metadata


def collect_files(folder: str) -> list:
    if not os.path.isdir(folder):
        sys.exit(f"Folder not found: {folder}")
    files = sorted(
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ALLOWED_EXTENSIONS)
    )
    if not files:
        sys.exit(f"No {ALLOWED_EXTENSIONS} files found in {folder}")
    return files


def ensure_container(service: BlobServiceClient):
    container = service.get_container_client(CONTAINER_NAME)
    if not container.exists():
        container.create_container()
        print(f"Created container: {CONTAINER_NAME}")
    return container


def upload_files(container, files: list) -> int:
    uploaded = 0
    for file_name in files:
        local_path = os.path.join(LOCAL_FOLDER, file_name)
        blob_name = f"{BLOB_PREFIX}{file_name}"
        metadata = build_metadata(file_name)

        try:
            with open(local_path, "rb") as data:
                container.upload_blob(
                    name=blob_name,
                    data=data,
                    overwrite=OVERWRITE,
                    metadata=metadata,
                    content_settings=ContentSettings(content_type="application/pdf"),
                )
            uploaded += 1
            print(f"[OK]   {blob_name}")
            print(f"       title : {metadata['customMetaTitle']}")
            print(f"       url   : {metadata['customMetaURL']}")
        except Exception as exc:  # keep going if one file fails
            print(f"[FAIL] {blob_name}: {exc}")
    return uploaded


def verify(container):
    """List blobs with their metadata so you can confirm before indexing."""
    print("\nBlobs in container with metadata:")
    for blob in container.list_blobs(name_starts_with=BLOB_PREFIX or None, include=["metadata"]):
        meta = blob.metadata or {}
        print(f"- {blob.name}")
        for key in ("customMetaTitle", "customMetaURL", "customMetaPublic"):
            print(f"    {key}: {meta.get(key, '<missing>')}")


def main():
    files = collect_files(LOCAL_FOLDER)
    print(f"Found {len(files)} file(s) in {LOCAL_FOLDER}\n")

    service = get_service_client()
    container = ensure_container(service)

    uploaded = upload_files(container, files)
    print(f"\nUploaded {uploaded}/{len(files)} file(s) to '{CONTAINER_NAME}'.")

    verify(container)


if __name__ == "__main__":
    main()