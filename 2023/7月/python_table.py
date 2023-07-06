import pandas as pd

#利用正则表达式将数据提取出来，然后分成
data = [
    ["hx-node1", "linstordb", "lvm-thick-n0", 0, 1010, "/dev/drbd1010", "516 MiB", "InUse", "UpToDate"],
    ["hx-node2", "linstordb", "lvm-thick-n0", 0, 1010, "/dev/drbd1010", "516 MiB", "Unused", "UpToDate"],
    ["hx-node3", "linstordb", "lvm-thick-n7", 0, 1010, "/dev/drbd1010", "516 MiB", "", "Unknown"],
    ["hx-node1", "LUN01", "lvm-thick-n0", 0, 1004, "/dev/drbd1004", "30.01 GiB", "Unused", "UpToDate"],
    ["hx-node1", "LUN01", "lvm-thick-n0", 1, 1005, "/dev/drbd1005", "30.01 GiB", "Unused", "UpToDate"],
    ["hx-node2", "LUN01", "lvm-thick-n0", 0, 1004, "/dev/drbd1004", "30.01 GiB", "Unused", "UpToDate"],
    ["hx-node2", "LUN01", "lvm-thick-n0", 1, 1005, "/dev/drbd1005", "30.01 GiB", "Unused", "UpToDate"],
    ["hx-node3", "LUN01", "DfltDisklessStorPool", 0, 1004, "/dev/drbd1004", "", "", "Unknown"],
    ["hx-node3", "LUN01", "DfltDisklessStorPool", 1, 1005, "/dev/drbd1005", "", "", "Unknown"],
    ["hx-node1", "LUN02", "lvm-thick-n0", 0, 1006, "/dev/drbd1006", "80.02 GiB", "Unused", "UpToDate"],
    ["hx-node2", "LUN02", "lvm-thick-n0", 0, 1006, "/dev/drbd1006", "80.02 GiB", "InUse", "UpToDate"],
    ["hx-node3", "LUN02", "DfltDisklessStorPool", 0, 1006, "/dev/drbd1006", "", "", "Unknown"],
    ["hx-node1", "LUN04", "lvm-thick-n0", 0, 1008, "/dev/drbd1008", "30.01 GiB", "InUse", "UpToDate"],
    ["hx-node2", "LUN04", "lvm-thick-n0", 0, 1008, "/dev/drbd1008", "30.01 GiB", "Unused", "UpToDate"],
    ["hx-node3", "LUN04", "DfltDisklessStorPool", 0, 1008, "/dev/drbd1008", "", "", "Unknown"],
    ["hx-node1", "LUN05", "lvm-thick-n0", 0, 1009, "/dev/drbd1009", "30.01 GiB", "Unused", "UpToDate"],
    ["hx-node2", "LUN05", "lvm-thick-n0", 0, 1009, "/dev/drbd1009", "30.01 GiB", "Unused", "UpToDate"],
    ["hx-node3", "LUN05", "DfltDisklessStorPool", 0, 1009, "/dev/drbd1009", "", "", "Unknown"],
    ["hx-node1", "LUN81", "lvm-thick-n0", 0, 1003, "/dev/drbd1003", "10.00 GiB", "Unused", "UpToDate"],
    ["hx-node2", "LUN81", "lvm-thick-n0", 0, 1003, "/dev/drbd1003", "10.00 GiB", "Unused", "UpToDate"],
    ["hx-node3", "LUN81", "DfltDisklessStorPool", 0, 1003, "/dev/drbd1003", "", "", "Unknown"],
    ["hx-node1", "r1", "lvm-thick-n0", 0, 1011, "/dev/drbd1011", "2.00 GiB", "InUse", "UpToDate"],
    ["hx-node2", "r1", "lvm-thick-n0", 0, 1011, "/dev/drbd1011", "2.00 GiB", "Unused", "UpToDate"],
    ["hx-node3", "r1", "DfltDisklessStorPool", 0, 1011, "/dev/drbd1011", "", "", "Unknown"],
    ["hx-node1", "r2", "lvm-thick-n0", 0, 1012, "/dev/drbd1012", "10.00 GiB", "Unused", "UpToDate"],
    ["hx-node2", "r2", "lvm-thick-n0", 0, 1012, "/dev/drbd1012", "10.00 GiB", "InUse", "UpToDate"],
    ["hx-node3", "r2", "DfltDisklessStorPool", 0, 1012, "/dev/drbd1012", "", "", "Unknown"]
]

columns = ["Node", "Resource", "StoragePool", "VolNr", "MinorNr", "DeviceName", "Allocated", "InUse", "State"]

df = pd.DataFrame(data, columns=columns)

pattern = r"linstordb|LUN\d{2}|r[1,2]"  # 正则表达式模式
count = df["Resource"].str.count(pattern).sum()
print("出现次数:", count)

# 使用筛选条件
filtered_df = df[(df["Node"] == "hx-node1") & (df["StoragePool"] == "lvm-thick-n0")]

# 输出筛选结果
print(filtered_df)
