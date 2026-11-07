# smartfarming — DigitalTwin-Agri (Combined Upload)

> **This repository is the original combined upload of the DigitalTwin-Agri
> project.** Everything in it also lives — in cleaner, canonical form — in
> the dedicated repositories below. Start there; this repo is kept as the
> historical snapshot of how the project was first assembled.

**Canonical homes:**

- 📊 **[DIGITALTWIN_ML](https://github.com/PrabhashNandan78/DIGITALTWIN_ML)**
  — the machine-learning side: groundnut yield modelling notebooks
  (2000–2024 weather/yield data), synthetic dataset generation, ML
  baselines and the hybrid physics + ML digital-twin feedback model.
- 🌱 **[TWIN](https://github.com/PrabhashNandan78/TWIN)** — the simulation
  engine: plant-level farm, plant, sensor and decision-support twins.
- 🦴 **[DT_ENGINE_SKELETON](https://github.com/PrabhashNandan78/DT_ENGINE_SKELETON)**
  — the early engine prototype/snapshot that TWIN superseded.

Together they are the code behind the IEEE paper *"DigitalTwin-Agri: A
Hybrid Digital Twin Framework for Next-Generation Smart Agriculture"* by
Prabhash Nandan.

## What is in this snapshot

| Path | Contents |
|---|---|
| `digitaltwin_ml/` | A copy of the notebooks and datasets now canonical in DIGITALTWIN_ML. |
| `twin(1)/` | A copy of the engine tree now canonical in TWIN (this copy additionally contains the `Visualization/` package that some TWIN scripts import). |
| `DT_engine_skeleton/` | A copy of the early engine prototype now canonical in DT_ENGINE_SKELETON. |
| `smartfarming` | An empty placeholder file from the original upload, kept as-is. |

The two zip archives that were originally committed alongside their
extracted folders (`DT_engine_skeleton.zip`, `twin(1).zip`) were removed in
the portfolio-optimization cleanup — the extracted folders beside them
contain the same project files.
