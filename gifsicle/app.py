import os
import subprocess
import sys

__GIF_EXE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "asset", "gifsicle.exe"))


class Gif():
    def __init__(self, ):
        pass


def _getsize(fname):
    return "{} MB".format(round(os.stat(fname).st_size/1024/1024, 2))


def _gifcall(args):
    subprocess.call([__GIF_EXE] + args)


def _help():
    args = ["-h"]
    _gifcall(args)


def main():
    _help


def gif_run():
    """
    Run gifsicle 

    example usage :

    gif  - This will print the help

    gif -O gif_file_name.gif optimises the given give file



    """
    args = sys.argv[1:]
    # if no args
    if not args:
        _help()
    else:
        args_str = " ".join(args)
        if ".gif" in args_str.lower():
            gif_file = [arg for arg in args if arg.lower().endswith(".gif")][0]
            #if out file is not sprecified add the extra args
            if "-o" not in args:
                gif_fname = os.path.basename(gif_file)
                gif_fname = os.path.splitext(gif_fname)[0]
                outgif = os.path.join(os.path.dirname(
                    gif_file), "{}_o.gif".format(gif_fname))
                extra_args = ["-o", outgif]
                _gifcall(args + extra_args)

                #if optimize, report size
                if "-O" in args:
                    print("Size optimized from {} to {}".format(
                        _getsize(gif_file), _getsize(outgif)))
            else:
                _gifcall(args)
        else:
            _help()


if __name__ == "__main__":
    # main()
    gif_run()
