"""Convert midi to pdf using Lilypond."""
import music21
import sys
import subprocess


def main():
    """Convert music."""
    file_path = sys.argv[1]
    music = music21.converter.parse(file_path)
    music.write('lilypond', f'{file_path}.ly')
    subprocess.run(['lilypond', f'{file_path}.ly'])


if __name__ == '__main__':
    main()
