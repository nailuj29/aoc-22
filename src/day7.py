import utils
from pip._vendor.pyparsing import line

class Item():
    def __init__(self, name):
        self.name = name

class Directory(Item):
    def __init__(self, name):
        super().__init__(name)
        self.children = []
        
    def calc_size(self):
        sizes = map(lambda c: c.calc_size(), self.children)
        return sum(sizes)
    
    def get_all_sizes(self):
        all_folders = []
        child_dirs = filter(lambda c: type(c) == Directory, self.children)
        for child in child_dirs:
            dirs = child.get_all_sizes()
            for directory in dirs:
                all_folders.append(directory)
        all_folders.append(self.calc_size())
        
        return set(all_folders)
        
class File(Item):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        
    def calc_size(self):
        return self.size
    
def process_sh(data):
    lines = data.split("\n")
    root = Directory("/")
    cwd = root
    parents = []
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    cwd = parents.pop()
                elif parts[2] == "/":
                    cwd = root
                    parents = []
                else:
                    parents.append(cwd)
                    new_dir = Directory(parts[2])
                    cwd.children.append(new_dir)
                    cwd = new_dir
        elif parts[0] == "dir":
            # ignore directories, they'll be created when we cd into them
            pass
        else:
            cwd.children.append(File(parts[1], int(parts[0])))
            
    return root
         
def find_deletable(tree):
    deletable = []
    child_dirs = filter(lambda c: type(c) == Directory, tree.children)
    for child in child_dirs:
        dirs_to_delete = find_deletable(child)
        for directory in dirs_to_delete:
            deletable.append(directory)
    if tree.calc_size() <= 100000:
        deletable.append(tree)
        
    return set(deletable)
        
def day7p1(data):
    tree = process_sh(data)
    deletable = find_deletable(tree)
    sizes = map(lambda d: d.calc_size(), deletable)
    return sum(sizes)

def day7p2(data):
    tree = process_sh(data)
    sizes = tree.get_all_sizes()
    total_size = tree.calc_size()
    free_space = 70000000 - total_size
    eligible = filter(lambda s: free_space + s > 30000000, sizes)
    return min(eligible)

assert day7p1(utils.read(7, True)) == 95437
assert day7p2(utils.read(7, True)) == 24933642
print(day7p1(utils.read(7)))
print(day7p2(utils.read(7)))