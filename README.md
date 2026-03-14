# theo-website-gcp

This repo is the GCP / Debian version of the original `theo-website` AWS repo.

## What changed

- Replaced AWS IMDSv2 metadata calls with GCP metadata server calls.
- Replaced Amazon Linux 2023 `dnf` setup with Debian `apt-get`.
- Kept the same Flask route structure:
  - `/`
  - `/metadata`
- Kept the same static image and page layout.
- Uses `gunicorn` behind `nginx` on a default GCP Debian VM.
- Uses `sudo` throughout the startup script.
- Startup script now clones this repo, not the original AWS repo.

## Metadata fields returned

`/metadata` returns:

- Instance Name
- Instance Private IP Address
- Availability Zone
- Project ID
- VPC Network

## Local run

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python app.py
```

Then open `http://SERVER_IP:8080`.

## GCP VM startup

Use `startup.sh` as the startup script on a Debian-based Compute Engine VM.
Make sure the VM allows inbound TCP/80.
