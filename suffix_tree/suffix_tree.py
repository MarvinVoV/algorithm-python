
class SuffixNode:
    def __init__(self, suffix_link=None):
        self.children = {}
        if suffix_link is not None:
            self.suffix_link = suffix_link
        else:
            self.suffix_link = self

    def add_link(self, c, v):
        """ link this node to node v via string c """
        self.children[c] = v


def build_suffix_trie(s):
    """ Construct a suffix trie."""
    assert len(s) > 0

    # explicitly build the two-node suffix tree
    root = SuffixNode()  # the root node
    longest = SuffixNode(suffix_link=root)
    root.add_link(s[0], longest)

    # for every character left in the string
    for c in s[1:]:
        current = longest
        previous = None
        while c not in current.children:
            # create new node r1 with transition Current -c->r1
            r1 = SuffixNode()
            current.add_link(c, r1)
            # if we came from some previous node, make that
            # node's suffix link point here
            if previous is not None:
                previous.suffix_link = r1
            # walk down the suffix links
            previous = r1
            current = current.suffix_link
        # make the last suffix link
        if current is root:
            previous.suffix_link = root
        else:
            previous.suffix_link = current.children[0]

        # move to the newly added child of the longest path (which is the new longest path)
        longest = longest.children[c]
    return root

if __name__ == '__main__':
    root = build_suffix_trie('aba')
    print(root)


