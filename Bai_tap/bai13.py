# Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng
# trắng, loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.
# Giả sử đầu vào là: hello world and practice makes perfect and hello world again
# Thì đầu ra là: again and hello makes perfect practice world
lines = [x for x in input("Nhap chuoi: ").split(' ')]
print()

# lines.sort()
print(lines)
kq = sorted(set(list(lines)))
print(" ".join(kq))