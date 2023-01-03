import time


def main():
    time_start = time.time()

    file_out = open('../docs/README.md', 'w', encoding='utf-8')

    file_template = open('../sources/template.md', 'r', encoding='utf-8')

    line = file_template.readline()
    while line:
        if line.startswith('{{main_content}}'):
            generateMainContent(file_out)
        else:
            file_out.write(line)
        line = file_template.readline()

    file_out.close()
    file_template.close()

    time_end = time.time()

    print(f'Generated Markdown in {round(time_end - time_start, 2)} s')


def generateMainContent(file_out):
    file_in = open('../sources/theotokarion.txt', 'r', encoding='utf-8')

    line = file_in.readline()

    ode = False
    evening = False

    while line:
        line = line.rstrip()
        if line.startswith('Ode'):
            line = '#### ' + line
            ode = True
            evening = False
        elif line.endswith('Prosomia'):
            line = '#### ' + line
            ode = True
            evening = False
        elif line.endswith('Kathisma'):
            line = '#### ' + line
            ode = True
            evening = False
        elif line.endswith('Evening'):
            line = '### ' + line
            ode = False
            evening = True
        elif line.endswith('Tone'):
            line = '## ' + line
            ode = False
            evening = False
        elif ode and len(line) > 0:
            line = f'<p class="ode">{line}</p>'
        elif evening and len(line) > 0:
            line = f'<p class="evening-subtitle">{line}</p>'

        line += '\n'

        file_out.write(line)
        line = file_in.readline()

    file_in.close()


if __name__ == "__main__":
    main()

# Title
# Tone
# Day
# ode
