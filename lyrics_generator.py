# with open('/Users/admin/desktop/strings.js', 'r') as content_file:
#     content = content_file.read()
# print(content)
# import os
# onlyfiles = os.listdir('/Users/admin/desktop/')

lines = [line.rstrip('\n') for line in open('/Users/admin/desktop/archer.lrc')]
# print(lines)
index = 0


def get_millisec(time_str):
    """Get Milliseconds from minutes."""
    m, sms = time_str.split(':')
    s, ms = sms.split('.')
    return int(m) * 60000 + int(s) * 1000 + int(ms) * 10


for index, value in enumerate(lines):
    if "[00:" in value:
        index = index
        break

# print(index)
newlines = lines[index:]
# print(newlines)

# f = open("lyrics.js", "w+")

for index, value in enumerate(newlines):
    msec = get_millisec(value[1:9])
    # print(msec)
    # print(value[1:9])
    lyric = value[10:]
    # print(lyric)
    print("{ time: " + str(msec) + ", callback: () => this.setState({ lyric: \"" + lyric + "\" }),},\n")
    # f.write("{ time: %s, callback: () => this.setState({ lyric: %s }),},\n" % msec % lyric)

# f.close()

