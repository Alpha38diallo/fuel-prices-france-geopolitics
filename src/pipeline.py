import subprocess
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Début du pipeline")

SCRIPTS = [
    "src/extract.py",
    "src/transform.py",
    "src/load.py",
    "src/analyze.py",
    "src/visualize.py"
]

for script in SCRIPTS:
    print(f"\nExécution : {script}")

    try:
        subprocess.run(
            ["python3", script],
            check=True
        )

        logging.info(f"{script} terminé")
        print(f"✅ {script} terminé")

    except subprocess.CalledProcessError as e:
        logging.error(f"Erreur dans {script}")
        print(f"❌ Erreur dans {script}")
        break

logging.info("Pipeline terminé")
print("\n🚀 Pipeline terminé.")