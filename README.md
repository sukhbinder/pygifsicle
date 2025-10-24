# PYGIFSICLE
A Python wrapper for the Gifsicle command-line tool.

This package provides a convenient way to use Gifsicle from Python, with a user-friendly command-line interface for common operations.

# Installation
```bash
pip install pygifsicle
```

# Usage
The command-line interface provides three subcommands for common Gifsicle operations:

## `optimize`
Optimize a GIF file to reduce its size.

```bash
pygifsicle optimize <input_file> [-o <output_file>] [-O3]
```

**Arguments:**
*   `input_file`: The GIF file to optimize.
*   `-o, --output`: The output file. If not specified, a new file with the `_o` suffix will be created.
*   `-O3`: Use optimization level 3 (slower, but better results).

**Example:**
```bash
pygifsicle optimize my_animation.gif -O3
```

## `resize`
Resize a GIF file to the specified dimensions.

```bash
pygifsicle resize <input_file> [--width <w>] [--height <h>] [-o <output_file>]
```

**Arguments:**
*   `input_file`: The GIF file to resize.
*   `--width`: The new width.
*   `--height`: The new height.
*   `-o, --output`: The output file. If not specified, a new file with the `_o` suffix will be created.

**Example:**
```bash
pygifsicle resize my_animation.gif --width 200
```

## `scale`
Scale a GIF file by a given factor.

```bash
pygifsicle scale <input_file> --factor <f> [-o <output_file>]
```

**Arguments:**
*   `input_file`: The GIF file to scale.
*   `--factor`: The scaling factor.
*   `-o, --output`: The output file. If not specified, a new file with the `_o` suffix will be created.

**Example:**
```bash
pygifsicle scale my_animation.gif --factor 0.5
```
