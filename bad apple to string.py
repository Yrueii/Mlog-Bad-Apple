import cv2

video_path = "./input/untitled.mp4"
output_file = "./output/output.txt"
file_len = 0
write = False
exit = False
output_file_index = 0
block = 0
max_resolution_x = 512

cap = cv2.VideoCapture(video_path)

output_filename = "boutput"
encoding_version = 3

if encoding_version == 0:
    seperator ="#####"
    ALPHA_START = ord('$')   # 36
    BASE = 91                # from '!' (33) through '~' (33+93)
elif encoding_version == 1:
    seperator ="###"
    ALPHA_START = ord('$')   # 36
    BASE = 91                # from '!' (33) through '~' (33+93)
    seperator ="###"
    ALPHA_START = 93   # 36
    BASE = 91                # from '!' (33) through '~' (33+93)
elif encoding_version == 2:
    seperator ="#####"
    ALPHA_START = 93
    BASE = 55203
    TRIPLE_STATES = 513 * 513 * 2
elif encoding_version == 3:
    seperator ="##"
    ALPHA_START = 93
    BASE = 1030


def pack_triple(x, y, flag):
    return ((x * 513) + y) * 2 + flag

def encode4(t0, t1, t2, t3):
    n = 0
    for t in (t0, t1, t2, t3):
        n = n * TRIPLE_STATES + pack_triple(*t)

    chars = []
    for _ in range(5):
        chars.append(chr((n % BASE) + ALPHA_START))
        n //= BASE

    return ''.join(reversed(chars))

def encode_num(n: int) -> str:
    if not (0 <= n <= max_resolution_x):
        raise ValueError("out of range")
    high, low = divmod(n, BASE)
    return chr(high + ALPHA_START) + chr(low + ALPHA_START)
    # result = n - BASE
    # if result < 0:
    #     return chr(n + ALPHA_START) + chr(ALPHA_START)
    # else:
    #     return chr(BASE + ALPHA_START - 1) + chr(result + ALPHA_START)


def encodev2(a: int, b: int, flag: bool) -> str:
    if not (0 <= a <= 512 and 0 <= b <= 512):
        raise ValueError

    n = ((a * 513) + b) * 2 + int(flag)

    c1 = n // (BASE * BASE)
    n %= BASE * BASE
    c2 = n // BASE
    c3 = n % BASE

    return chr(c1 + ALPHA_START) + chr(c2 + ALPHA_START) + chr(c3 + ALPHA_START)

def encode514(a: int, b: int, flag: bool) -> str:
    packed = b * 2 + flag

    return chr(a + ALPHA_START) + chr(packed + ALPHA_START)


def decode(s: str):
    n = (
        (ord(s[0]) - ALPHA_START) * BASE * BASE +
        (ord(s[1]) - ALPHA_START) * BASE +
        (ord(s[2]) - ALPHA_START)
    )

    flag = n % 2
    n //= 2

    b = n % 513
    a = n // 513

    return a, b, bool(flag)

# print(decode("YuS"))
# exit()

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# for i in range(0,176):
#     print(encode_num(i))
# print(encode_num(30))
# test = ord('A') + ord('%') - 36*2
# print(ord('A') - 36)
# print(ord('$') - 36)
# print(test)
# quit()
# looppp = 0
# cap.set(cv2.CAP_PROP_POS_FRAMES, 121 + 38 + 28)
frame_index = 50
while True:
    block += 1
    print(f"~~~~~~~~~~~~~~~~ [ {output_filename}{output_file_index}.txt ] ~~~~~~~~~~~~~~~~~~~")
    exit = False
    output_file_index += 1
    file_len = 0
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    first_seperator = False
    with open(f"./output/{output_filename}{output_file_index}.txt", "w+", encoding="utf-8") as out:
        out.write('"')
        while True:
            ret, frame = cap.read()
            if first_seperator:
                file_len += 3
                out.write(seperator)
            else:
                first_seperator = True
            frame = cv2.flip(frame, 0)

            height, width, _ = frame.shape

            arr = []
            data2 = ''

            for y in range(height):
                for x in range(width):
                    b, g, r = frame[y, x]
                    is_true = 1 if (r, g, b) > (127, 127, 127) else 0
                    if 'previous_is_true' not in locals():
                        previous_is_true = 1
                        write = True
                    else:
                        write = False

                    if previous_is_true != is_true or write or x == 0 or x >= max_resolution_x - 1:
                        # looppp += 1  
                        if encoding_version == 0:
                            data2 = f"{encode_num(x)}{encode_num(y)}{chr(is_true+32)}"
                        elif encoding_version == 1:
                            data2 = f"{encodev2(x, y, is_true)}"
                            if '\\n' in data2:
                                data2 = data2.replace('\\n', '\\\\n')
                        elif encoding_version == 2:
                            arr.append((x,y,is_true))
                            if len(arr) == 4:
                                data2 = f"{encode4(arr[0], arr[1], arr[2], arr[3])}"
                                # print(data2)
                                # print(f"{arr[0], arr[1], arr[2], arr[3]}")
                                arr.clear()
                        elif encoding_version == 3:
                            data2 = f"{encode514(x, y, is_true)}"
                            # print(data2, len(data2), x, y)
                        if data2:
                            out.write(data2)
                            file_len = out.tell()
                            data2 = ''
                    previous_is_true = is_true

                    # if file_len > 65500:
                    if file_len > 65500:
                        out.write('"')
                        exit = True
                        # exit()
                        break
                if exit == True:
                    break
            if exit == True:
                break

            frame_index += 1
            print(f"frame {frame_index}")

cap.release()
print("Done.")
