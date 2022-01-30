# scr_monitoring_cpu_or_mem
 
Python script for fast system monitoring of RAM and logical processors. 
Script currently supports the following platforms: <b>Linux, Windows, macO, FreeBSD, OpenBSD, NetBSD</b>

# scr_info_mem_cpu.py

python script takes two parameters <b>*mem*</b> and <b>*cpu*</b>.

# scr_info_mem_cpu.tar.gz (docker image)
<p>FROM python:3.8.10-slim //
ADD scr_info_mem_cpu.py / //
RUN pip install psutil && rm -rf somepath //
ENTRYPOINT ["python", "scr_info_mem_cpu.py", ""]

