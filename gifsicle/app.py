import os
import subprocess
import sys
import argparse

__GIF_EXE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "asset", "gifsicle.exe"))


def _getsize(fname):
    # Check if file exists before getting size
    if not os.path.exists(fname):
        return "N/A"
    return "{} MB".format(round(os.stat(fname).st_size/1024/1024, 2))


def _gifcall(args):
    subprocess.call([__GIF_EXE] + args)


def _get_output_filename(input_file, suffix="_o"):
    """Generates an output filename based on the input file."""
    dirname = os.path.dirname(input_file)
    basename = os.path.basename(input_file)
    fname, ext = os.path.splitext(basename)
    return os.path.join(dirname, f"{fname}{suffix}{ext}")


def gif_run():
    """
    Run gifsicle
    """
    parser = argparse.ArgumentParser(description='A Python wrapper for gifsicle.')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Optimize command
    parser_optimize = subparsers.add_parser('optimize', help='Optimize a GIF file.')
    parser_optimize.add_argument('input_file', help='The GIF file to optimize.')
    parser_optimize.add_argument('-o', '--output', help='The output file.')
    parser_optimize.add_argument('-O3', action='store_true', help='Use optimization level 3.')


    # Resize command
    parser_resize = subparsers.add_parser('resize', help='Resize a GIF file.')
    parser_resize.add_argument('input_file', help='The GIF file to resize.')
    parser_resize.add_argument('--width', type=int, help='The new width.')
    parser_resize.add_argument('--height', type=int, help='The new height.')
    parser_resize.add_argument('-o', '--output', help='The output file.')

    # Scale command
    parser_scale = subparsers.add_parser('scale', help='Scale a GIF file.')
    parser_scale.add_argument('input_file', help='The GIF file to scale.')
    parser_scale.add_argument('--factor', type=float, help='The scaling factor.')
    parser_scale.add_argument('-o', '--output', help='The output file.')

    args = parser.parse_args()

    if not args.command:
        _gifcall(['-h'])
        sys.exit(0)

    input_file = args.input_file
    output_file = args.output or _get_output_filename(input_file)

    gif_args = [input_file, '-o', output_file]

    if args.command == 'optimize':
        if args.O3:
            gif_args.insert(0, '-O3')
        else:
            gif_args.insert(0, '-O2')
        _gifcall(gif_args)
        print(f"Size optimized from {_getsize(input_file)} to {_getsize(output_file)}")

    elif args.command == 'resize':
        if not args.width and not args.height:
            parser.error('At least one of --width or --height must be specified for resize.')

        resize_arg = ''
        if args.width:
            resize_arg += f'{args.width}'
        resize_arg += 'x'
        if args.height:
            resize_arg += f'{args.height}'

        gif_args.extend(['--resize', resize_arg])
        _gifcall(gif_args)
        print(f"Resized to {args.width}x{args.height}. New size: {_getsize(output_file)}")

    elif args.command == 'scale':
        if not args.factor:
             parser.error('--factor must be specified for scale.')
        gif_args.extend(['--scale', str(args.factor)])
        _gifcall(gif_args)
        print(f"Scaled by a factor of {args.factor}. New size: {_getsize(output_file)}")


if __name__ == "__main__":
    gif_run()
