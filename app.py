from __future__ import annotations

from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

METADATA_ROOT = "http://metadata.google.internal/computeMetadata/v1"
METADATA_HEADERS = {"Metadata-Flavor": "Google"}
METADATA_TIMEOUT = 2


@app.route('/')
def home():
    return render_template('index.html')


def get_metadata(path: str) -> str:
    """Fetch a metadata field from the GCP metadata server."""
    url = f"{METADATA_ROOT}/{path.lstrip('/')}"
    response = requests.get(url, headers=METADATA_HEADERS, timeout=METADATA_TIMEOUT)
    response.raise_for_status()
    return response.text.strip()


def short_name(value: str) -> str:
    """Return the last path segment for values like zones/us-west1-a or full URLs."""
    return value.rstrip('/').split('/')[-1]


@app.route('/metadata')
def metadata():
    try:
        instance_name = get_metadata('instance/name')
        private_ip = get_metadata('instance/network-interfaces/0/ip')
        zone = short_name(get_metadata('instance/zone'))
        project_id = get_metadata('project/project-id')
        vpc_network = short_name(get_metadata('instance/network-interfaces/0/network'))

        return jsonify(
            {
                'Instance Name': instance_name,
                'Instance Private IP Address': private_ip,
                'Availability Zone': zone,
                'Project ID': project_id,
                'VPC Network': vpc_network,
            }
        )
    except requests.RequestException as exc:
        return (
            jsonify(
                {
                    'error': 'Unable to retrieve GCP metadata.',
                    'details': str(exc),
                }
            ),
            500,
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
