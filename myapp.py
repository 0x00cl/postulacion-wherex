# metrics - Flask API that exposes machine CPU and RAM utilization
# Copyright (C) 2024  Tomás Gutiérrez L. (0x00)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    return {
        "cpu": {
            "percent": psutil.cpu_percent(interval=0.2),
            "times": psutil.cpu_times()._asdict(),
            "stats": psutil.cpu_stats()._asdict(),
        },
        "memory": {
            "virtual_mem": psutil.virtual_memory()._asdict(),
            "swap_mem": psutil.swap_memory()._asdict()
            }
        }
