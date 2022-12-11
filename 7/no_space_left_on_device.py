SIZE_THRESHOLD = 1e5
TOTAL_DISK_SPACE = 7e7
SPACE_REQUIRED = 3e7

dirs = {}
cur_dir = None
dir_sizes = {}


def new_dir(name, parent_path=None):
    return {
        "name": name,
        "files": [],
        "path": (parent_path or []) + [name],
        "children": {},
    }


def new_file(name, size, dir_path):
    return {
        "name": name,
        "size": size,
        "dir_path": dir_path,
    }


def handle_ls_line(line):
    global cur_dir
    match line:
        case ["dir", dir_name]:
            if not dir_name in cur_dir["children"]:
                cur_dir["children"][dir_name] = new_dir(
                    dir_name, parent_path=cur_dir["path"])
        case [size, file_name] if size.isdigit():
            dir_file = new_file(file_name, int(size), cur_dir["path"])
            cur_dir["files"].append(dir_file)
        case _:
            print(f"Unrecognized ls line: {line}")


def dir_from_path(path):
    if not path:
        return None

    d = dirs
    for name in path:
        d = d["children"][name] if "children" in d else d[name]
    return d


def parent_dir(d):
    return dir_from_path(d["path"][:-1]) if len(d["path"]) > 1 else None


def handle_cmd(cmd_input):
    global dirs
    global cur_dir
    match cmd_input:
        case ["cd", *args]:
            arg_dir = args[0]
            if not cur_dir:  # Create the root dir
                dirs[arg_dir] = new_dir(arg_dir)
                cur_dir = dirs[arg_dir]
                return
            if arg_dir == "..":  # Go up one dir
                cur_dir = parent_dir(cur_dir)
            elif arg_dir == "/":
                cur_dir = dirs["/"]
            else:  # Create a new dir and move to it
                cur_dir["children"][arg_dir] = new_dir(
                    arg_dir, parent_path=cur_dir["path"])
                cur_dir = cur_dir["children"][arg_dir]
        case ["ls"]:
            return
        case _:
            print(f"Unrecognized command input: {cmd_input}")


def dir_path_str(d):
    return "/".join(d["path"])[1:]


def dir_size(d):
    path_str = dir_path_str(d)
    if path_str in dir_sizes:
        return dir_sizes[path_str]

    dir_sizes[path_str] = sum(f["size"] for f in d["files"]) + \
        sum(dir_size(child) for child in d["children"].values())

    return dir_sizes[path_str]


def dir_list(d):
    return [d] + [dir_list(child) for child in d["children"].values()]


def populate_dirs():
    with open("input.txt", "r") as f:
        for line in f.read().splitlines():
            if line.startswith("$"):
                handle_cmd(line.split()[1:])
            else:
                handle_ls_line(line.split())


def solve():
    populate_dirs()
    root_size = dir_size(dirs["/"])
    sizes = dir_sizes.values()
    sum_sizes = sum(size for size in sizes if size <= SIZE_THRESHOLD)
    print(f"Solution #1: {sum_sizes}")
    space_available = TOTAL_DISK_SPACE - root_size
    space_needed = SPACE_REQUIRED - space_available
    smallest_big_enough_size = next(
        (size for size in sorted(sizes) if size >= space_needed)
    )
    print(f"Solution #2: {smallest_big_enough_size}")


solve()
