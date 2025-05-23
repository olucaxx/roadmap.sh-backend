from setuptools import setup

setup(
    name="github-activity",
    version="0.1.0",
    packages=["github_activity"],
    entry_points={
        "console_scripts": [
            "github-activity=github_activity.main:main"
        ]
    },
)