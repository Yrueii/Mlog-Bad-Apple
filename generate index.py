from pathlib import Path
base = Path(__file__).parent

workers = 36
input = './output'
filename ='boutput'
index = 0
import os

proc_index_data = {f'proc{i}': [] for i in range(1,workers + 1)}

for file_index in range(1,710):
    with open(f"{base}/{input}/{filename}{file_index}.txt", "r") as f:
        data = f.read()
        arr_index = []
        data = data[1:-1]
        # print(data)
        print("data length: ", len(data))

        frame_arr = []
        char_i = 0
        for char in data:
            char_i += 1
            if char == "#":
                if not frame_arr or frame_arr[-1] != char_i:
                    frame_arr.append(char_i + 1)

        print(frame_arr)

        for i, frame in enumerate(frame_arr):
            size = frame - (frame_arr[i-1] if i != 0 else 0)
            temp_arr = [frame - size]
            # print(temp_arr)
            # print(size)
            dis = size // (workers)
            
            if dis % 2:
                dis = dis - 1
            # print(dis)

            # print(frame - size, size)
            for ii in range(1,workers+1):
                offset = dis * ii + (frame - size)

                x = False
                while True:
                    x = ord(data[offset]) - 93
                    if x == 0:
                        break
                    offset -= 1
                
                temp_arr.append(offset)
                if ii == workers:
                    temp_arr.append(frame)
            arr_index.append(temp_arr)
        
        # print(arr_index)
        # print(len(arr_index))
        # for arr in arr_index:
        #     print(ord(data[arr]) - 93)
        # print(offset)
        # print(data[offset])
        # print(data[offset+1])

        # print(ord(data[offset]) - 93)
        # print((ord(data[offset+1]) - 93) // 2)
        # print((ord(data[offset+1]) - 93) % 2)
        # break

        # index_code = ''
        for proc in range(1,workers+1):
            print(f"proc{proc}: {', '.join(str(item[proc-1]) + '|' + str(item[proc]) for item in arr_index)}")
            # print(f"{','.join(str(item[proc-1]) + str(item[proc]) for item in arr_index)}")
            # index_data = ''
            for item in arr_index:
                first = chr(item[proc-1] + 93)
                second = chr(item[proc] + 93)
                proc_index_data[f'proc{proc}'].append(first + second)
            
            # index_code += f'set proc{proc} "{index_data}"\n'

            # for char in index_data:
            #     print(ord(char))
        


        if file_index == 704:
            break
        # proc_index = 0
        # for item in arr_index:
        #     proc_index += 1
proc_index_data = {k: ''.join(v) for k, v in proc_index_data.items()}

with open(f"{base}/{input}/1proc_index_table.txt", "w+") as out:
    for k, v in proc_index_data.items():
        out.write(f"set {k} \"{v}\"\n")
        # temp = ''
        # for char in v:
        #     temp += str(ord(char) - 93) + ("|")
        # print(temp)