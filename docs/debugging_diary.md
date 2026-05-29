# Debugging Diary

## Issue 1: Python Module Import Failure

Problem:
The training and testing scripts could not locate project modules and produced a ModuleNotFoundError for the src package.

Root Cause:
The project root directory was not included in the Python module search path.

Resolution:
Scripts were executed using:

PYTHONPATH=. python src/models/train.py

This ensured the project root was available during execution.

---

## Issue 2: Scikit-Learn Import Failure

Problem:
The training pipeline failed with an ImportError related to sklearn internal modules.

Root Cause:
The virtual environment contained an inconsistent scikit-learn installation.

Resolution:
The package was reinstalled and the virtual environment dependencies were refreshed. The training pipeline executed successfully afterward.

---

## Issue 3: Docker Runtime Failure

Problem:
The Docker container failed to start and reported that uvicorn could not be found.

Root Cause:
Docker image caching and runtime issues caused required dependencies to be unavailable inside the container.

Resolution:
Docker images and caches were cleared using docker system prune, the image was rebuilt without cache, and the container was successfully started.

---

## Lessons Learned

Environment consistency, dependency management, and container validation are critical for production-grade ML services. Automated testing and container verification helped identify issues early.
