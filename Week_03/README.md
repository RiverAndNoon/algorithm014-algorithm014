递归

递归模版

```python
def recursion(level, param1, param2, ...): 
    # recursion terminator 递归终止条件
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 处理当前逻辑层
    process(level, data...) 
    # drill down 下探到下一层
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed 清理当前层
```

思维要点

1. 抵制人肉递归
2. 找最近重复性
3. 数学归纳法思想

验证搜索二叉树，可以通过中序遍历递增的特点来验证ß

分治代码模版

```python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
		print_result 
		return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```



