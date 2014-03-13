import random  # for the eventual if 'name' == __main__ hypotheticals.
import time


class BSTree(object):
    """This is a search tree"""
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        """will insert the value val into the BST.  If val is already present,
        it will be ignored
        """
        if self.value is None:
            self.value = value
        else:
            if value > self.value:
                if self.right is None:
                    self.right = BSTree(value)
                else:
                    self.right.insert(value)
            if value < self.value:
                if self.left is None:
                    self.left = BSTree(value)
                else:
                    self.left.insert(value)
            else:
                return

    def contains(self, val):
        """will return True if val is in the BST, False if not"""
        try:
            if val == self.value:
                return True
            elif val > self.value:
                return self.right.contains(val)
            elif val < self.value:
                return self.left.contains(val)
        except AttributeError:
            return False

    def size(self):
        """will return the integer size of the BST (equal to the total number
            of values stored in the tree), 0 if the tree is empty."""
        total = 0
        if not self.value:
            return total
        else:
            total += 1
        if self.left:
            total += self.left.size()
        if self.right:
            total += self.right.size()
        return total
        # this is from Stephen's code; refactored my original work to it.

    def depth(self):
        """will return an integer representing the total number of levels in
        the tree"""
        total = 0
        if not self.value:
            return total
        else:
            left_total = self.left.depth() if self.left else 0
            right_total = self.right.depth() if self.right else 0
            return max(left_total, right_total) + 1
            # this comes from our in-class code breakdown.

    def balance(self):
        """Will return an positive or negative integer that represents how
           well-balanced the tree is. Positive value means the tree is right-
           heavy; negative means it is left-heavy. Balanced tree = 0."""
        if not self.value:
            return 0
        else:
            return self.right.depth() - self.left.depth()

    def in_order(self):
        '''returns a generator that will return the values in the tree using
        in-order traversal, one at a time.'''
        if self.left:
            for val in self.left.in_order():
                yield val
        yield self.value
        if self.right is not None:
            for val in self.right.in_order():
                yield val

    def pre_order(self):
        '''returns a generator that will return the values in the tree using
        pre-order traversal, one at a time.'''
        pass

    def post_order(self):
        '''returns a generator that will return the values in the tree using
        post_order traversal, one at a time.'''
        pass

    def breadth_first(self):
        '''returns a generator that will return the values in the tree using
        breadth-first traversal, one at a time.'''
        pass

    # def delete(self, value):
    #     """remove val from the tree if present, if not present this method is a
    #     no-op. Return None in all cases"""
    #     pass
    #     # need to account for three cases:
    #     # if it's a leaft (no self.left or self.right)
    #     if not self.left.value and not self.right.value:
    #         pass
    #     # if it's got self.left.
    #     if not self.right:
    #         pass
    #     # if it's got self.right.
    #     if not self.left:
    #         pass
    #     return None

    # the below is all from Cris Ewing; required for this file.
    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.value is None else (
            "\t%s;\n%s\n" % (
                self.value,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)

if __name__ == '__main__':
    ordered_tree = BSTree()
    random_tree = BSTree()
    for num in range(900):
        ordered_tree.insert(num)
        random_tree.insert(random.choice(range(2000)))
    first_time = time.time()
    ramdom_has = random_tree.contains(900)
    second_time = time.time()
    ordered_has = ordered_tree.contains(900)
    third_time = time.time()
    print 'Random: %r sec.' % (second_time-first_time)
    print 'Ordered: %r sec.' % (third_time-second_time)
