## 树的定义

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left,self.right = None,None
```

## 树的遍历

### 1.前序（Pre-order）

根-左-右：对于树中任意节点来说，先打印这个节点，再打印左子树，最后打印右子树。

```python
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

```

### 2.中序（In-order）

左-根-右：先打印左子树，再打印节点本身，最后打印右子树。



```python
def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

```

### 3.后序（Post-order）

左-右-根：先打印左子树，在打印右子树，最后打印节点本身。

```python
def postorder(self, root):
    if root:
        self.preorder(root.left)
        self.perorder(root.right)
        self.traverse_path.append(root.val)

```

### 前中后序遍历模版

```python
class Solution:
    def inorderTraversal(self,root):
        res = []
        stack = []
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

        # # 前序，相同模板
        # while stack or root:
        #     while root:
        #         res.append(root.val)
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     root = root.right
        # return res

        # # 后序，相同模板
        # # 实际遍历顺序为 根->右->左 翻转之后为左->右->根
        # while stack or root:
        #     while root:
        #         res.append(root.val)
        #         stack.append(root)
        #         root = root.right
        #     root = stack.pop()
        #     root = root.left
        # return res[::-1]
```

### N叉树遍历

```python
# N叉树通用递归模板
class Solution:
    def preorder(self, root):
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res
```

## 堆heap

意义：可以迅速找到一堆数中的最大或者最小值的数据结构（优先级）

根结点最大的堆叫大顶堆或大根堆，根结点最小的堆叫做小顶堆或小根堆。

二叉树堆（顶堆）：1.一棵**完全二叉树**。2.树中任意节点的值总是>=子节点的值

假设是大顶堆，常见操作：

Find-max: O(1)

Delete-max:O(logN)

Insert(create):O(logN)orO(!)

节点关系：

1. 根节点（顶堆元素）是：a[0]
2. 索引为i的左孩子的索引是（2*i+1）
3. 索引为i的右孩子的索引是（2*i+1）
4. 索引为i的父节点的索引是floor(( i - 1) / 2)



#### Insert

1.新元素一律先插入到堆的尾部

2.依次向上调整整个堆的结构

