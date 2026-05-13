from pathlib import Path

import yaml


def test_sigma_files_parse_and_include_core_metadata() -> None:
    sigma_dir = Path(__file__).resolve().parent.parent / "sigma"
    sigma_files = list(sigma_dir.glob("*.yml"))
    assert sigma_files, "Expected at least one Sigma rule in the sigma/ directory"

    for sigma_file in sigma_files:
        payload = yaml.safe_load(sigma_file.read_text(encoding="utf-8"))
        assert payload.get("title"), f"Missing title in {sigma_file.name}"
        assert payload.get("id"), f"Missing id in {sigma_file.name}"
        assert payload.get("logsource"), f"Missing logsource in {sigma_file.name}"
        assert payload.get("detection"), f"Missing detection in {sigma_file.name}"
        assert payload.get("level"), f"Missing level in {sigma_file.name}"
