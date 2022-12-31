import glob
import shutil

srcs = glob.glob("*/MQTT*Packet/src/*.c")

for src in srcs:
    shutil.copy2(src, "src")

