"""LICENSE
Copyright 2020 Hermann Krumrey <hermann@krumreyh.com>

This file is part of ln-dl.

ln-dl is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ln-dl is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ln-dl.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

import os
from setuptools import setup, find_packages


if __name__ == "__main__":

    setup(
        name="ln-dl",
        version=open("version", "r").read(),
        description="A downloader for fan-translated "
                    "light novels and web novels",
        long_description=open("README.md", "r").read(),
        long_description_content_type="text/markdown",
        author="Hermann Krumrey",
        author_email="hermann@krumreyh.com",
        classifiers=[
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        ],
        url="https://gitlab.namibsun.net/namibsun/python/ln-dl",
        license="GNU GPL3",
        packages=find_packages(),
        scripts=list(map(lambda x: os.path.join("bin", x), os.listdir("bin"))),
        install_requires=[
            "bs4",
            "requests",
            "typing",
            "colorama",
            "puffotter",
            "sentry-sdk"
        ],
        include_package_data=True,
        zip_safe=False
    )
