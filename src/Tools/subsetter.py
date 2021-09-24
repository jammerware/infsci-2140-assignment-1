import time


def write_n_from(in_path, out_path, delimiter, n=100000):
    count = 0

    with open(in_path, 'r', encoding="utf-8") as file_in:
        with open(out_path, 'w+', encoding="utf-8") as file_out:
            for read_line in file_in.readlines():
                file_out.write(f'{read_line}')

                if read_line.strip() == delimiter:
                    count += 1

                    if count % 1000 == 0:
                        print('count:', count)
                    if count >= n:
                        break


start_time = time.time()
write_n_from(
    in_path='E:/School/Grad/infsci-2140/assignment-1/data/output/docset.trecweb',
    out_path='E:/School/Grad/infsci-2140/assignment-1/data/output/docset.100k.trecweb',
    delimiter='</DOC>',
    n=100000)
print('time', time.time() - start_time)
