
from setuptools import setup

if __name__ == "__main__":

    setup(
        name="budgeter",
        version="0.0.0",
        description="Basic budgeting software.",
        url="https://github.com/PeaWagon/Delta-Hacks-Budget-Planner",
        package_dir={"budgeter": "budgeter"},
        requires=["matplotlib"],
        )
