# coding: utf8
import ffmpeg


class InfoGrabber:
    @staticmethod
    def get_info(file_path: str) -> dict:
        info = ffmpeg.probe(file_path)
        return info


if __name__ == '__main__':
    import json
    import os
    print(json.dumps(InfoGrabber.get_info('F:/Movies/preview.mp4'), indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':')))
    print(os.get_terminal_size())
