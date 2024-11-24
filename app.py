import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent(interval=1)
    mem_metric = psutil.virtual_memory().percent
    disk_metric = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    network_metric = (net_io.bytes_sent + net_io.bytes_recv) / (1024 * 1024)  # Total network traffic in MB
    message = None

    if cpu_metric > 80 or mem_metric > 80:
        message = "High CPU or Memory Detected, scale up!!!"

    return render_template(
        "index.html",
        cpu_metric=cpu_metric,
        mem_metric=mem_metric,
        disk_metric=disk_metric,
        network_metric=network_metric,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
