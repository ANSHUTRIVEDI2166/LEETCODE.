class FolderTree:
    # Every node in this tree represents a folder in the file system. Note that
    # internal nodes also represent folders (unlike Tries where internal nodes
    # may not actually represent a word). This is guaranteed by the problem
    # statement constraint "For any folder not at the root level, its parent
    # folder will also be in the input."
    def __init__(self):
        self.children = dict()
        # To be marked later.
        self.is_duplicate = False
    
    # Adds a folder specified by the given path into the tree.
    def add_folder(self, path: List[str]) -> None:
        node = self
        for p in path:
            if p not in node.children:
                node.children[p] = FolderTree()
            node = node.children[p]
    
    # Traverse the entire tree and mark all the duplicated nodes. We do this by
    # borrowing an idea from Merkle Trees, where we recursively compute the
    # hashes of the subtrees, and then do a hash-combine to compute the hash of
    # the root. We then use this hash value as a unique representation of a tree
    # instead of fully serializing all the contents of the subtrees.
    #
    # mark_duplicates returns the hash for the subtree rooted at `self`. It also
    # modifies the `seen` dictionary in place, which stores which Merkle hashes
    # we've already encountered before.
    def mark_duplicates(self, seen: dict[int, List['FolderTree']]) -> int:
        # Step 1: recursively evaluate the Merkle hashes of all the subtrees.
        subtree_hashes = []
        for key, node in self.children.items():
            h = node.mark_duplicates(seen)
            subtree_hashes.append(hash((key, h)))
        # Sorting makes sure that we don't get differences in hashes due to
        # differences in the relative ordering of the subtrees.
        subtree_hashes.sort()
        # The below value `h` is now our hash representation of the entire
        # subtree rooted at `self`.
        h = hash(tuple(subtree_hashes))
        # Leaf nodes always hash to the same value (i.e. hash of the empty
        # tuple) and we are supposed to ignore them.
        if h == hash(tuple()):
            return h
        # Detect duplicates and update the `seen` records.
        if h not in seen:
            seen[h] = [self]
        else:
            self.is_duplicate = True
            if len(seen[h]) == 1:
                seen[h][0].is_duplicate = True
            seen[h].append(self)
        return h
    
    # Traverse the entire tree and remove all nodes marked as duplicated.
    def remove_duplicates(self) -> None:
        remove_keys = []
        for key, node in self.children.items():
            if node.is_duplicate:
                remove_keys.append(key)
            else:
                node.remove_duplicates()
        for key in remove_keys:
            self.children.pop(key)
    
    # Traverse the entire tree and return all folder paths present in the tree
    # as a list.
    def list_all(self) -> List[List[str]]:
        result = []
        for key, node in self.children.items():
            subpaths = node.list_all()
            for subpath in subpaths:
                result.append([key] + subpath)
            result.append([key])
        return result


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = FolderTree()
        for path in paths:
            tree.add_folder(path)
        
        tree.mark_duplicates({})
        tree.remove_duplicates()

        return tree.list_all()
