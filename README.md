# theo-website-gcp

This is a GCP-ready Debian version of the original AWS EC2 metadata demo.

## What changed

- Replaced AWS IMDSv2 calls with GCP metadata server calls.
- Replaced AL2023 `dnf` steps with Debian `apt-get`.
- Uses `gunicorn` behind `nginx` instead of running the Flask dev server on port 80.
- Startup script uses `sudo` throughout and is safe for the default Debian image on Compute Engine.

## Metadata fields returned

`/metadata` now returns:

- Instance Name
- Instance Private IP Address
- Availability Zone
- Project ID
- VPC Network

## Files

- `app.py` - Flask app updated for GCP metadata
- `startup.sh` - self-contained GCP startup script for a Debian VM
- `templates/index.html` - original page kept intact
- `static/styles.css` - original stylesheet kept intact

## Run locally on a Debian or Ubuntu host

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python app.py
```

Then open `http://SERVER_IP:8080`.

## On GCP

Use `startup.sh` as the VM startup script and allow inbound TCP/80.
# theo-website-gcp
